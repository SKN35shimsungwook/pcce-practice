# -*- coding: utf-8 -*-
"""사용자 코드를 별도 프로세스에서 실행해 테스트케이스를 채점하는 모듈."""
import json
import subprocess
import sys
import tempfile
import textwrap
import os

RESULT_START = "###PCCE_RESULT_START###"
RESULT_END = "###PCCE_RESULT_END###"
TIMEOUT_SEC = 5

_RUNNER_TEMPLATE = """
import json
import sys

{user_code}

_tests = json.loads({tests_json!r})
_results = []
for _t in _tests:
    _entry = {{"passed": False, "actual": None, "error": None}}
    try:
        _actual = {func_name}(*_t["args"])
        _entry["actual"] = _actual
        try:
            _norm_actual = json.loads(json.dumps(_actual, default=str))
        except Exception:
            _norm_actual = _actual
        _entry["passed"] = _norm_actual == _t["expected"]
    except Exception as _e:
        _entry["error"] = f"{{type(_e).__name__}}: {{_e}}"
    _results.append(_entry)

print("{start}")
print(json.dumps(_results, ensure_ascii=False, default=str))
print("{end}")
"""


def run_solution(user_code: str, function_name: str, test_cases: list) -> dict:
    """user_code 안의 function_name 함수를 test_cases로 채점한다.

    반환값: {"ok": bool, "results": [...], "error": str|None}
    results 각 항목: {"passed", "actual", "error"}
    """
    if function_name not in user_code:
        return {
            "ok": False,
            "results": [],
            "error": f"'{function_name}' 함수를 찾을 수 없습니다. 함수 이름을 확인하세요.",
        }

    tests_payload = [{"args": tc["args"], "expected": tc["expected"]} for tc in test_cases]
    script = _RUNNER_TEMPLATE.format(
        user_code=textwrap.indent(user_code, ""),
        tests_json=json.dumps(tests_payload, ensure_ascii=False),
        func_name=function_name,
        start=RESULT_START,
        end=RESULT_END,
    )

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as f:
        f.write(script)
        script_path = f.name

    child_env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    try:
        proc = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SEC,
            encoding="utf-8",
            errors="replace",
            env=child_env,
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "results": [],
            "error": f"실행 시간이 {TIMEOUT_SEC}초를 초과했습니다. 무한 루프가 없는지 확인하세요.",
        }
    finally:
        try:
            os.unlink(script_path)
        except OSError:
            pass

    if proc.returncode != 0 and RESULT_START not in (proc.stdout or ""):
        err = (proc.stderr or "알 수 없는 오류").strip().splitlines()
        return {
            "ok": False,
            "results": [],
            "error": err[-1] if err else "실행 중 오류가 발생했습니다.",
        }

    stdout = proc.stdout or ""
    if RESULT_START not in stdout or RESULT_END not in stdout:
        return {
            "ok": False,
            "results": [],
            "error": "채점 결과를 읽을 수 없습니다. 코드에 print/입력 처리가 없는지 확인하세요.",
        }

    payload = stdout.split(RESULT_START, 1)[1].split(RESULT_END, 1)[0].strip()
    try:
        results = json.loads(payload)
    except json.JSONDecodeError:
        return {"ok": False, "results": [], "error": "채점 결과 파싱에 실패했습니다."}

    return {"ok": True, "results": results, "error": None}
