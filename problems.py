# -*- coding: utf-8 -*-
"""PCCE 연습용 코딩 문제 모음.

각 문제는 solution(...) 형태의 함수를 완성하는 방식입니다.
test_cases 중 hidden=True 인 항목은 문제 화면에는 노출하지 않고 채점에만 사용합니다.
"""

PROBLEMS = [
    {
        "id": 1,
        "title": "두 수의 합",
        "category": "기초 문법",
        "difficulty": "하",
        "function_name": "solution",
        "params": ["a", "b"],
        "description": "정수 a와 b를 입력받아 두 수의 합을 반환하는 solution 함수를 완성하세요.",
        "constraints": "-1,000,000 ≤ a, b ≤ 1,000,000",
        "starter_code": "def solution(a, b):\n    answer = 0\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": [1, 2], "expected": 3, "hidden": False},
            {"args": [-5, 5], "expected": 0, "hidden": False},
            {"args": [100, 200], "expected": 300, "hidden": True},
            {"args": [-10, -20], "expected": -30, "hidden": True},
        ],
    },
    {
        "id": 2,
        "title": "리스트 최댓값 찾기",
        "category": "리스트/튜플",
        "difficulty": "하",
        "function_name": "solution",
        "params": ["numbers"],
        "description": "정수 리스트 numbers를 입력받아 가장 큰 값을 반환하는 solution 함수를 완성하세요. (내장 함수 max 사용 금지)",
        "constraints": "1 ≤ len(numbers) ≤ 1,000",
        "starter_code": "def solution(numbers):\n    answer = numbers[0]\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": [[3, 7, 2]], "expected": 7, "hidden": False},
            {"args": [[-1, -5, -2]], "expected": -1, "hidden": False},
            {"args": [[10]], "expected": 10, "hidden": True},
            {"args": [[5, 5, 5, 9, 1]], "expected": 9, "hidden": True},
        ],
    },
    {
        "id": 3,
        "title": "문자열 뒤집기",
        "category": "문자열",
        "difficulty": "하",
        "function_name": "solution",
        "params": ["s"],
        "description": "문자열 s를 입력받아 뒤집은 문자열을 반환하는 solution 함수를 완성하세요.",
        "constraints": "1 ≤ len(s) ≤ 1,000",
        "starter_code": "def solution(s):\n    answer = \"\"\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": ["hello"], "expected": "olleh", "hidden": False},
            {"args": ["python"], "expected": "nohtyp", "hidden": False},
            {"args": ["a"], "expected": "a", "hidden": True},
            {"args": ["코딩테스트"], "expected": "트스테딩코", "hidden": True},
        ],
    },
    {
        "id": 4,
        "title": "짝수 개수 세기",
        "category": "리스트/튜플",
        "difficulty": "하",
        "function_name": "solution",
        "params": ["numbers"],
        "description": "정수 리스트 numbers에서 짝수의 개수를 반환하는 solution 함수를 완성하세요.",
        "constraints": "1 ≤ len(numbers) ≤ 1,000",
        "starter_code": "def solution(numbers):\n    answer = 0\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": [[1, 2, 3, 4, 5, 6]], "expected": 3, "hidden": False},
            {"args": [[1, 3, 5]], "expected": 0, "hidden": False},
            {"args": [[2, 4, 6, 8]], "expected": 4, "hidden": True},
            {"args": [[-2, -3, 0, 7]], "expected": 2, "hidden": True},
        ],
    },
    {
        "id": 5,
        "title": "구구단 리스트 만들기",
        "category": "조건/반복",
        "difficulty": "중",
        "function_name": "solution",
        "params": ["n"],
        "description": "정수 n을 입력받아 n단 구구단 결과(n*1부터 n*9까지)를 리스트로 반환하는 solution 함수를 완성하세요.",
        "constraints": "2 ≤ n ≤ 9",
        "starter_code": "def solution(n):\n    answer = []\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": [2], "expected": [2, 4, 6, 8, 10, 12, 14, 16, 18], "hidden": False},
            {"args": [5], "expected": [5, 10, 15, 20, 25, 30, 35, 40, 45], "hidden": False},
            {"args": [9], "expected": [9, 18, 27, 36, 45, 54, 63, 72, 81], "hidden": True},
        ],
    },
    {
        "id": 6,
        "title": "평균 이상 학생 찾기",
        "category": "딕셔너리",
        "difficulty": "중",
        "function_name": "solution",
        "params": ["scores"],
        "description": (
            "학생 이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아, "
            "전체 평균 이상의 점수를 받은 학생 이름을 리스트로 반환하는 solution 함수를 완성하세요. "
            "이름은 딕셔너리에 등장하는 순서를 유지합니다."
        ),
        "constraints": "1 ≤ len(scores) ≤ 100",
        "starter_code": "def solution(scores):\n    answer = []\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {
                "args": [{"철수": 80, "영희": 90, "민수": 60}],
                "expected": ["철수", "영희"],
                "hidden": False,
            },
            {
                "args": [{"A": 70, "B": 70, "C": 70}],
                "expected": ["A", "B", "C"],
                "hidden": False,
            },
            {
                "args": [{"A": 100, "B": 0}],
                "expected": ["A"],
                "hidden": True,
            },
        ],
    },
    {
        "id": 7,
        "title": "소수 판별하기",
        "category": "조건/반복",
        "difficulty": "중",
        "function_name": "solution",
        "params": ["n"],
        "description": "정수 n을 입력받아 소수이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "constraints": "1 ≤ n ≤ 10,000",
        "starter_code": "def solution(n):\n    answer = True\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": [2], "expected": True, "hidden": False},
            {"args": [4], "expected": False, "hidden": False},
            {"args": [1], "expected": False, "hidden": True},
            {"args": [17], "expected": True, "hidden": True},
            {"args": [97], "expected": True, "hidden": True},
            {"args": [100], "expected": False, "hidden": True},
        ],
    },
    {
        "id": 8,
        "title": "연속 문자 압축하기",
        "category": "문자열",
        "difficulty": "상",
        "function_name": "solution",
        "params": ["s"],
        "description": (
            "알파벳 소문자로 이루어진 문자열 s에서 연속으로 반복되는 문자를 "
            "'문자+개수' 형태로 압축한 문자열을 반환하는 solution 함수를 완성하세요. "
            "개수가 1인 경우 숫자는 생략합니다. 예: 'aaabbc' -> 'a3b2c'"
        ),
        "constraints": "1 ≤ len(s) ≤ 1,000",
        "starter_code": "def solution(s):\n    answer = \"\"\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": ["aaabbc"], "expected": "a3b2c", "hidden": False},
            {"args": ["abc"], "expected": "abc", "hidden": False},
            {"args": ["aaaa"], "expected": "a4", "hidden": True},
            {"args": ["aabbaa"], "expected": "a2b2a2", "hidden": True},
        ],
    },
    {
        "id": 9,
        "title": "상위 N개 합 구하기",
        "category": "리스트/튜플",
        "difficulty": "중",
        "function_name": "solution",
        "params": ["numbers", "n"],
        "description": "정수 리스트 numbers에서 가장 큰 값부터 n개를 뽑아 합을 반환하는 solution 함수를 완성하세요.",
        "constraints": "1 ≤ n ≤ len(numbers) ≤ 1,000",
        "starter_code": "def solution(numbers, n):\n    answer = 0\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {"args": [[1, 5, 3, 9, 2], 2], "expected": 14, "hidden": False},
            {"args": [[4, 4, 4], 1], "expected": 4, "hidden": False},
            {"args": [[10, 20, 30, 40], 3], "expected": 90, "hidden": True},
        ],
    },
    {
        "id": 10,
        "title": "FizzBuzz 리스트 만들기",
        "category": "조건/반복",
        "difficulty": "하",
        "function_name": "solution",
        "params": ["n"],
        "description": (
            "1부터 n까지의 정수에 대해, 3의 배수이면 'Fizz', 5의 배수이면 'Buzz', "
            "둘 다의 배수이면 'FizzBuzz', 그 외에는 숫자를 문자열로 변환한 값을 "
            "순서대로 담은 리스트를 반환하는 solution 함수를 완성하세요."
        ),
        "constraints": "1 ≤ n ≤ 100",
        "starter_code": "def solution(n):\n    answer = []\n    # 여기에 코드를 작성하세요\n    return answer\n",
        "test_cases": [
            {
                "args": [5],
                "expected": ["1", "2", "Fizz", "4", "Buzz"],
                "hidden": False,
            },
            {
                "args": [15],
                "expected": [
                    "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz",
                    "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
                ],
                "hidden": True,
            },
        ],
    },
]

PROBLEMS_BY_ID = {p["id"]: p for p in PROBLEMS}
CATEGORIES = sorted({p["category"] for p in PROBLEMS})
DIFFICULTIES = ["하", "중", "상"]
