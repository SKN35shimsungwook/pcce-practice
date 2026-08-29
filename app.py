# -*- coding: utf-8 -*-
"""PCCE 코딩 연습 (Streamlit) — 문제를 보고 함수를 작성해 자동 채점받는 연습 앱."""
import random

import streamlit as st

import db
import runner
from problems import CATEGORIES, PROBLEMS, PROBLEMS_BY_ID

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
    .setup-card{background:#FFFFFF;border:1px solid #D8DEE8;border-radius:12px;
               padding:20px 24px;margin-bottom:14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

COUNT_OPTIONS = [5, 10, 20, 30, 50, 100, 150]


@st.cache_resource
def get_con():
    return db.get_connection()


con = get_con()

ss = st.session_state
ss.setdefault("user", "")
ss.setdefault("stage", "setup")  # "setup" | "practice"
ss.setdefault("queue", None)
ss.setdefault("pos", 0)
ss.setdefault("session_label", "")
ss.setdefault("code_by_pid", {})
ss.setdefault("last_result_by_pid", {})


def problems_in(category):
    if category == "전체":
        return PROBLEMS
    return [p for p in PROBLEMS if p["category"] == category]


def start_session(category, count, shuffle=True):
    pool = problems_in(category)
    ids = [p["id"] for p in pool]
    if shuffle:
        random.shuffle(ids)
    if count is not None:
        ids = ids[:count]
    ss.queue = ids
    ss.pos = 0
    ss.session_label = f"{category} · {len(ids)}문제"
    ss.stage = "practice"


def open_single(pid):
    ss.queue = [pid]
    ss.pos = 0
    ss.session_label = "개별 문제"
    ss.stage = "practice"


def back_to_setup():
    ss.stage = "setup"
    ss.queue = None
    ss.pos = 0


# ---------- sidebar ----------
with st.sidebar:
    st.header("PCCE 코딩 연습")
    st.caption("문제를 읽고 solution 함수를 완성해 채점해보세요.")
    ss.user = st.text_input("닉네임 (풀이 기록 저장용)", value=ss.user, placeholder="예: 홍길동").strip()
    if not ss.user:
        ss.user = "guest"

    solved_ids = db.get_solved_ids(con, ss.user)
    st.divider()
    st.metric("해결한 문제", f"{len(solved_ids)} / {len(PROBLEMS)}")

    if ss.stage == "practice":
        st.divider()
        if st.button("연습 설정으로 돌아가기", width="stretch"):
            back_to_setup()
            st.rerun()

    st.divider()
    st.caption("문제 목록에서 바로 골라 풀 수도 있어요.")
    browse_cat = st.selectbox("카테고리 보기", ["전체"] + CATEGORIES, key="browse_cat")
    for p in problems_in(browse_cat):
        label = f"{'✅ ' if p['id'] in solved_ids else ''}{p['id']}. {p['title']}"
        if st.button(label, key=f"nav_{p['id']}", width="stretch"):
            open_single(p["id"])
            st.rerun()

# ---------- setup screen ----------
if ss.stage == "setup" or not ss.queue:
    st.title("PCCE 코딩 연습")
    st.caption("주제를 고르고 풀고 싶은 문제 수를 정한 뒤 연습을 시작하세요. 각 주제마다 30문제씩 준비되어 있습니다.")

    with st.container(border=True):
        st.subheader("연습 설정")
        category_choice = st.radio("주제 선택", ["전체"] + CATEGORIES, horizontal=True)
        available = len(problems_in(category_choice))
        st.caption(f"선택한 주제에 사용 가능한 문제: {available}개")

        count_choices = [c for c in COUNT_OPTIONS if c < available]
        count_labels = [str(c) for c in count_choices] + [f"전체 ({available})"]
        count_pick = st.radio("문제 수", count_labels, horizontal=True, index=len(count_labels) - 1)
        shuffle_choice = st.checkbox("문제 순서 섞기", value=True)

        if st.button("연습 시작", type="primary", width="stretch"):
            count = None if count_pick.startswith("전체") else int(count_pick)
            start_session(category_choice, count, shuffle=shuffle_choice)
            st.rerun()

    st.stop()

# ---------- practice screen ----------
total = len(ss.queue)
pid = ss.queue[ss.pos]
problem = PROBLEMS_BY_ID[pid]

st.progress((ss.pos) / total if total else 0, text=f"{ss.session_label} · {ss.pos + 1} / {total}")

nav_prev, nav_info, nav_next = st.columns([1, 3, 1])
if nav_prev.button("← 이전 문제", disabled=ss.pos == 0, width="stretch"):
    ss.pos -= 1
    st.rerun()
nav_info.markdown(f"<div style='text-align:center;padding-top:6px;'>{ss.pos + 1} / {total}</div>", unsafe_allow_html=True)
if nav_next.button("다음 문제 →", disabled=ss.pos >= total - 1, width="stretch"):
    ss.pos += 1
    st.rerun()

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
        total_cases = len(outcome["results"])
        db.record_submission(con, ss.user, pid, passed, total_cases, code)
        if passed == total_cases:
            solved_ids.add(pid)

result = ss.last_result_by_pid.get(pid)
if result:
    st.markdown("#### 채점 결과")
    if not result["ok"]:
        st.error(result["error"])
    else:
        results = result["results"]
        passed = sum(1 for r in results if r["passed"])
        total_cases = len(results)
        if passed == total_cases:
            st.success(f"통과! {passed} / {total_cases} 테스트케이스를 모두 통과했습니다.")
        else:
            st.warning(f"{passed} / {total_cases} 테스트케이스 통과")

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
