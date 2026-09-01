# 🐍 PCCE 코딩 연습

**PCCE(파이썬 코딩 전문가 인증시험)** 스타일 문제를 풀고, 코드를 제출하면 자동으로
채점해주는 연습용 Streamlit 웹앱이에요.

## 기능

- 난이도(하/중/상)와 문제 개수를 골라서 연습 세션 시작
- 문제별로 함수를 작성해서 제출 → **여러 테스트케이스**로 자동 채점 (통과/실패, 실제 출력값 확인)
- 사용자 이름별로 **풀이 기록이 SQLite에 저장**돼서, 이미 푼 문제는 "해결됨" 표시가 남음
- 사용자 코드는 **별도 프로세스에서 5초 타임아웃**을 걸고 실행해서, 무한루프 등으로 앱이
  멈추지 않도록 안전하게 채점

## 기술 스택

| 기술 | 역할 |
|---|---|
| **Streamlit** | 문제 목록, 코드 입력창, 채점 결과 화면 |
| **subprocess** | 사용자가 제출한 코드를 메인 앱과 분리된 별도 파이썬 프로세스에서 실행 (타임아웃 5초로 안전하게 격리) |
| **SQLite** (`sqlite3`) | 사용자별 풀이 기록 저장 |

## 파일 구조

```
pcce_practice/
├── app.py         # Streamlit 앱 진입점 (문제 선택 → 풀이 → 채점 화면 흐름)
├── problems.py     # 문제 목록/카테고리/테스트케이스 데이터
├── runner.py       # 사용자 코드를 별도 프로세스로 실행해 테스트케이스 채점
├── db.py            # SQLite로 풀이 기록 저장/조회
└── requirements.txt
```

## 코드 구성

`runner.py`는 사용자 코드를 문자열로 받아서, 아래처럼 테스트 실행용 스크립트를 조립한 뒤
**임시 파일로 저장해서 별도 파이썬 프로세스로 돌려요**:

```python
_RUNNER_TEMPLATE = """
import json, sys
{user_code}
_tests = json.loads({tests_json!r})
_results = []
for _t in _tests:
    ...
    _actual = {func_name}(*_t["args"])
    _entry["passed"] = _norm_actual == _t["expected"]
"""
```

메인 Streamlit 프로세스와 완전히 분리된 프로세스에서 실행하고 `TIMEOUT_SEC=5`로 강제 종료하기
때문에, 사용자가 무한루프나 위험한 코드를 제출해도 앱 자체는 멈추지 않아요.

## 실행하기

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 트러블슈팅

**윈도우에서 한글이 들어간 테스트케이스가 전부 실패로 채점됨**

- 원인: 사용자 코드를 실행하는 자식 프로세스(`subprocess.run`)가 윈도우의 콘솔 코드페이지로
  출력을 인코딩해서, `encoding="utf-8"`로 읽어도 한글 딕셔너리 문제 같은 테스트케이스에서
  깨진 값이 나와 채점이 어긋났어요.
- 해결: 자식 프로세스 환경변수에 `PYTHONIOENCODING=utf-8`, `PYTHONUTF8=1`을 강제로 심어줌.

```diff
+ child_env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
  proc = subprocess.run(
      [sys.executable, script_path],
      ...
      encoding="utf-8",
+     errors="replace",
+     env=child_env,
  )
```

**정답과 형태만 다른 출력(튜플 vs 리스트 등)이 오답으로 채점됨**

- 원인: 사용자 함수의 반환값을 기대값과 `==`로 직접 비교했는데, 파이썬 타입(튜플, 커스텀 객체 등)과
  JSON으로 저장된 기대값(리스트 등)의 타입이 달라서 값은 같아도 `==`가 `False`가 되는 경우가 있었음.
- 해결: 비교 전에 실제 출력값을 `json.dumps` → `json.loads`로 한 번 왕복시켜서 JSON 호환 형태로
  정규화한 뒤 비교.

```diff
- _entry["passed"] = _actual == _t["expected"]
+ try:
+     _norm_actual = json.loads(json.dumps(_actual, default=str))
+ except Exception:
+     _norm_actual = _actual
+ _entry["passed"] = _norm_actual == _t["expected"]
```

---

🤖 이 저장소의 README는 Claude Code와 함께 작성했어요.
