# -*- coding: utf-8 -*-
"""PCCE 코딩 연습 (Streamlit) — 문제를 보고 함수를 작성해 자동 채점받는 연습 앱."""
import streamlit as st

import db
import runner
from problems import CATEGORIES, DIFFICULTIES, PROBLEMS, PROBLEMS_BY_ID

st.set_page_config(page_title="PCCE 코딩 연습", page_icon="🐍", layout="wide")

st.markdown(
    """
    <style>
    .pill{display:inline-block;font-size:.75rem;font-weight:600;padding:2px 10px;
          border-radius:999px;background:#E6EDF7;color:#1F4E8C;margin-right:6px;}
    .pill-diff-하{background:#E4F3EC;color:#2F7D5D;}
    .pill-diff-중{background:#FBF2DD;color:#B9790E;}
    .pill-diff-상{background:#FBE7E5;color:#C23B33;}
    .pill-solved{background:#2F7D5D;color:white;}
    .case-pass{background:#E4F3EC;border:1px solid #2F7D5D;color:#2F7D5D;
               border-radius:8px;padding:8px 12px;margin-bottom:6px;font-size:.9rem;}
    .case-fail{background:#FBE7E5;border:1px solid #C23B33;color:#C23B33;
               border-radius:8px;padding:8px 12px;margin-bottom:6px;font-size:.9rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def get_con():
    return db.get_connection()


con = get_con()

ss = st.session_state
ss.setdefault("user", "")
ss.setdefault("current_pid", PROBLEMS[0]["id"])
ss.setdefault("code_by_pid", {})
ss.setdefault("last_result_by_pid", {})

# ---------- sidebar ----------
with st.sidebar:
    st.header("PCCE 코딩 연습")
    st.caption("문제를 읽고 solution 함수를 완성해 채점해보세요.")
    ss.user = st.text_input("닉네임 (풀이 기록 저장용)", value=ss.user, placeholder="예: 홍길동").strip()
    if not ss.user:
        ss.user = "guest"

    st.divider()
    cat_filter = st.multiselect("카테고리", CATEGORIES, default=CATEGORIES)
    diff_filter = st.multiselect("난이도", DIFFICULTIES, default=DIFFICULTIES)

    solved_ids = db.get_solved_ids(con, ss.user)
    st.divider()
    st.metric("해결한 문제", f"{len(solved_ids)} / {len(PROBLEMS)}")

    st.divider()
    filtered = [p for p in PROBLEMS if p["category"] in cat_filter and p["difficulty"] in diff_filter]
    for p in filtered:
        label = f"{'✅ ' if p['id'] in solved_ids else ''}{p['id']}. {p['title']}"
        if st.button(label, key=f"nav_{p['id']}", width="stretch"):
            ss.current_pid = p["id"]
            st.rerun()

# ---------- main ----------
problem = PROBLEMS_BY_ID.get(ss.current_pid, PROBLEMS[0])
pid = problem["id"]

diff_class = f"pill-diff-{problem['difficulty']}"
solved_badge = ' <span class="pill pill-solved">해결됨</span>' if pid in solved_ids else ""
st.markdown(
    f'<span class="pill">{problem["category"]}</span>'
    f'<span class="pill {diff_class}">난이도 {problem["difficulty"]}</span>'
    f"{solved_badge}",
    unsafe_allow_html=True,
)
st.title(f"{problem['id']}. {problem['title']}")
st.markdown(problem["description"])
st.caption(f"제약 조건: {problem['constraints']}")

st.markdown("#### 입출력 예시")
visible_cases = [tc for tc in problem["test_cases"] if not tc.get("hidden")]
example_rows = [
    {"입력": ", ".join(repr(a) for a in tc["args"]), "기댓값": repr(tc["expected"])}
    for tc in visible_cases
]
st.table(example_rows)

hidden_count = sum(1 for tc in problem["test_cases"] if tc.get("hidden"))
if hidden_count:
    st.caption(f"채점 시 공개 예시 외에 숨겨진 테스트케이스 {hidden_count}개가 추가로 사용됩니다.")

st.markdown("#### 코드 작성")
default_code = ss.code_by_pid.get(pid, problem["starter_code"])
code = st.text_area(
    "solution 함수를 완성하세요",
    value=default_code,
    height=280,
    key=f"editor_{pid}",
    label_visibility="collapsed",
)
ss.code_by_pid[pid] = code

col_run, col_reset = st.columns([1, 1])
run_clicked = col_run.button("채점하기", type="primary", width="stretch")
if col_reset.button("초기 코드로 되돌리기", width="stretch"):
    ss.code_by_pid[pid] = problem["starter_code"]
    st.rerun()

if run_clicked:
    with st.spinner("채점 중..."):
        outcome = runner.run_solution(code, problem["function_name"], problem["test_cases"])
    ss.last_result_by_pid[pid] = outcome

    if outcome["ok"]:
        passed = sum(1 for r in outcome["results"] if r["passed"])
        total = len(outcome["results"])
        db.record_submission(con, ss.user, pid, passed, total, code)
        if passed == total:
            solved_ids.add(pid)

result = ss.last_result_by_pid.get(pid)
if result:
    st.markdown("#### 채점 결과")
    if not result["ok"]:
        st.error(result["error"])
    else:
        results = result["results"]
        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        if passed == total:
            st.success(f"통과! {passed} / {total} 테스트케이스를 모두 통과했습니다.")
        else:
            st.warning(f"{passed} / {total} 테스트케이스 통과")

        for i, (tc, r) in enumerate(zip(problem["test_cases"], results), start=1):
            label = f"테스트 {i}" + (" (숨김)" if tc.get("hidden") else "")
            if r["passed"]:
                st.markdown(
                    f'<div class="case-pass">✔ {label} 통과</div>',
                    unsafe_allow_html=True,
                )
            else:
                detail = f"오류: {r['error']}" if r["error"] else f"실행 결과: {r['actual']!r} (기댓값: {tc['expected']!r})"
                args_text = "" if tc.get("hidden") else f" · 입력: {', '.join(repr(a) for a in tc['args'])}"
                st.markdown(
                    f'<div class="case-fail">✘ {label} 실패{args_text}<br>{detail}</div>',
                    unsafe_allow_html=True,
                )
