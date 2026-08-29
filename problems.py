# -*- coding: utf-8 -*-
"""PCCE 연습용 코딩 문제 모음.

각 문제는 solution(...) 형태의 함수를 완성하는 방식입니다.
문제마다 정답(reference) 코드를 함께 정의해두고, 그 코드를 실제로 실행해서
테스트케이스의 기댓값을 계산합니다. 기댓값을 손으로 계산하지 않기 때문에
문제 수가 많아져도 정답이 어긋날 위험이 없습니다.

test_cases 중 앞의 2개는 화면에 예시로 보여주고 나머지는 채점에만 사용합니다
(hidden=True).
"""

CATEGORY_ORDER = ["기초 문법", "리스트/튜플", "문자열", "조건/반복", "딕셔너리"]

# 각 항목: (제목, 난이도, 설명, 제약조건, 파라미터 목록, 정답 코드, 테스트 인자 목록)

BASIC = [
    (
        "두 수의 합", "하",
        "정수 a와 b를 입력받아 두 수의 합을 반환하는 solution 함수를 완성하세요.",
        "-1,000,000 ≤ a, b ≤ 1,000,000", ["a", "b"],
        "def solution(a, b):\n    return a + b\n",
        [(1, 2), (-5, 5), (100, 200), (-10, -20)],
    ),
    (
        "두 수의 차", "하",
        "정수 a와 b를 입력받아 a에서 b를 뺀 값을 반환하는 solution 함수를 완성하세요.",
        "-1,000,000 ≤ a, b ≤ 1,000,000", ["a", "b"],
        "def solution(a, b):\n    return a - b\n",
        [(5, 3), (0, 10), (-4, -4), (100, 1)],
    ),
    (
        "두 수의 곱", "하",
        "정수 a와 b를 입력받아 두 수의 곱을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return a * b\n",
        [(3, 4), (-2, 5), (0, 100), (7, 7)],
    ),
    (
        "두 수의 몫", "하",
        "정수 a와 b를 입력받아 a를 b로 나눈 몫(정수)을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ b ≤ 1,000, 0 ≤ a ≤ 100,000", ["a", "b"],
        "def solution(a, b):\n    return a // b\n",
        [(7, 2), (10, 3), (20, 4), (9, 9)],
    ),
    (
        "두 수의 나머지", "하",
        "정수 a와 b를 입력받아 a를 b로 나눈 나머지를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ b ≤ 1,000, 0 ≤ a ≤ 100,000", ["a", "b"],
        "def solution(a, b):\n    return a % b\n",
        [(7, 2), (10, 3), (20, 4), (9, 9)],
    ),
    (
        "몫과 나머지의 합", "하",
        "정수 a와 b를 입력받아 (a를 b로 나눈 몫) + (a를 b로 나눈 나머지)를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ b ≤ 1,000, 0 ≤ a ≤ 100,000", ["a", "b"],
        "def solution(a, b):\n    return a // b + a % b\n",
        [(7, 2), (10, 3), (29, 5), (100, 7)],
    ),
    (
        "세 수의 합", "하",
        "정수 a, b, c를 입력받아 세 수의 합을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    return a + b + c\n",
        [(1, 2, 3), (-1, 0, 1), (10, 20, 30), (-5, -5, -5)],
    ),
    (
        "세 수의 평균", "하",
        "정수 a, b, c를 입력받아 세 수의 평균을 소수 둘째 자리에서 반올림하여 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    return round((a + b + c) / 3, 2)\n",
        [(1, 2, 3), (10, 20, 30), (5, 5, 5), (1, 2, 2)],
    ),
    (
        "절댓값 구하기", "하",
        "정수 n을 입력받아 n의 절댓값을 반환하는 solution 함수를 완성하세요.",
        "-1,000,000 ≤ n ≤ 1,000,000", ["n"],
        "def solution(n):\n    return n if n >= 0 else -n\n",
        [(5,), (-5,), (0,), (-100,)],
    ),
    (
        "제곱 구하기", "하",
        "정수 n을 입력받아 n의 제곱을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ n ≤ 1,000", ["n"],
        "def solution(n):\n    return n * n\n",
        [(3,), (-4,), (0,), (10,)],
    ),
    (
        "세제곱 구하기", "중",
        "정수 n을 입력받아 n의 세제곱을 반환하는 solution 함수를 완성하세요.",
        "-100 ≤ n ≤ 100", ["n"],
        "def solution(n):\n    return n ** 3\n",
        [(2,), (-3,), (0,), (4,)],
    ),
    (
        "n의 거듭제곱", "중",
        "정수 a와 음이 아닌 정수 b를 입력받아 a의 b제곱을 반환하는 solution 함수를 완성하세요.",
        "-100 ≤ a ≤ 100, 0 ≤ b ≤ 10", ["a", "b"],
        "def solution(a, b):\n    return a ** b\n",
        [(2, 3), (5, 0), (3, 4), (10, 2)],
    ),
    (
        "두 수 중 큰 값", "중",
        "정수 a와 b를 입력받아 둘 중 더 큰 값을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return a if a > b else b\n",
        [(3, 7), (10, 10), (-5, -1), (0, -1)],
    ),
    (
        "두 수 중 작은 값", "중",
        "정수 a와 b를 입력받아 둘 중 더 작은 값을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return a if a < b else b\n",
        [(3, 7), (10, 10), (-5, -1), (0, -1)],
    ),
    (
        "세 수 중 최댓값", "중",
        "정수 a, b, c를 입력받아 셋 중 가장 큰 값을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    return max(a, b, c)\n",
        [(3, 7, 5), (10, 10, 10), (-5, -1, -9), (0, -1, 1)],
    ),
    (
        "세 수 중 최솟값", "중",
        "정수 a, b, c를 입력받아 셋 중 가장 작은 값을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    return min(a, b, c)\n",
        [(3, 7, 5), (10, 10, 10), (-5, -1, -9), (0, -1, 1)],
    ),
    (
        "화씨를 섭씨로 변환", "중",
        "화씨 온도 f를 입력받아 섭씨 온도로 변환해 소수 첫째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요. (섭씨 = (화씨-32)*5/9)",
        "-100 ≤ f ≤ 300", ["f"],
        "def solution(f):\n    return round((f - 32) * 5 / 9, 1)\n",
        [(32,), (212,), (98.6,), (0,)],
    ),
    (
        "섭씨를 화씨로 변환", "중",
        "섭씨 온도 c를 입력받아 화씨 온도로 변환해 소수 첫째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요. (화씨 = 섭씨*9/5+32)",
        "-100 ≤ c ≤ 200", ["c"],
        "def solution(c):\n    return round(c * 9 / 5 + 32, 1)\n",
        [(0,), (100,), (37,), (-40,)],
    ),
    (
        "원의 둘레 구하기", "중",
        "원의 반지름 r을 입력받아 원의 둘레를 소수 둘째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요. (원주율은 3.14로 계산, 둘레 = 2*3.14*r)",
        "0 < r ≤ 1,000", ["r"],
        "def solution(r):\n    return round(2 * 3.14 * r, 2)\n",
        [(1,), (5,), (10,), (2.5,)],
    ),
    (
        "원의 넓이 구하기", "중",
        "원의 반지름 r을 입력받아 원의 넓이를 소수 둘째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요. (원주율은 3.14로 계산, 넓이 = 3.14*r*r)",
        "0 < r ≤ 1,000", ["r"],
        "def solution(r):\n    return round(3.14 * r * r, 2)\n",
        [(1,), (5,), (10,), (2.5,)],
    ),
    (
        "직사각형 넓이 구하기", "중",
        "가로 길이 w와 세로 길이 h를 입력받아 직사각형의 넓이를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ w, h ≤ 1,000", ["w", "h"],
        "def solution(w, h):\n    return w * h\n",
        [(3, 4), (10, 2), (7, 7), (1, 100)],
    ),
    (
        "직사각형 둘레 구하기", "상",
        "가로 길이 w와 세로 길이 h를 입력받아 직사각형의 둘레를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ w, h ≤ 1,000", ["w", "h"],
        "def solution(w, h):\n    return 2 * (w + h)\n",
        [(3, 4), (10, 2), (7, 7), (1, 100)],
    ),
    (
        "두 수의 평균 반올림", "상",
        "정수 a와 b를 입력받아 평균을 가장 가까운 정수로 반올림하여 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a, b ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return round((a + b) / 2)\n",
        [(3, 4), (10, 21), (5, 5), (-3, 3)],
    ),
    (
        "초를 분과 초로 변환", "상",
        "전체 초 seconds를 입력받아 [분, 초]를 리스트로 반환하는 solution 함수를 완성하세요.",
        "0 ≤ seconds ≤ 100,000", ["seconds"],
        "def solution(seconds):\n    return [seconds // 60, seconds % 60]\n",
        [(90,), (45,), (125,), (60,)],
    ),
    (
        "분을 시간과 분으로 변환", "상",
        "전체 분 minutes를 입력받아 [시간, 분]을 리스트로 반환하는 solution 함수를 완성하세요.",
        "0 ≤ minutes ≤ 100,000", ["minutes"],
        "def solution(minutes):\n    return [minutes // 60, minutes % 60]\n",
        [(90,), (45,), (125,), (60,)],
    ),
    (
        "BMI 계산", "상",
        "몸무게 weight(kg)와 키 height(m)를 입력받아 BMI 지수(몸무게 / 키의 제곱)를 소수 첫째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요.",
        "1 ≤ weight ≤ 300, 0.5 ≤ height ≤ 2.5", ["weight", "height"],
        "def solution(weight, height):\n    return round(weight / (height ** 2), 1)\n",
        [(70, 1.75), (50, 1.6), (90, 1.8), (65, 1.7)],
    ),
    (
        "할인된 가격 계산", "상",
        "원가 price와 할인율 rate(%)를 입력받아 할인된 가격을 정수로 반환하는 solution 함수를 완성하세요.",
        "0 ≤ price ≤ 1,000,000, 0 ≤ rate ≤ 100", ["price", "rate"],
        "def solution(price, rate):\n    return int(price * (1 - rate / 100))\n",
        [(10000, 10), (5000, 50), (20000, 0), (12345, 20)],
    ),
    (
        "이익률 계산", "상",
        "원가 cost와 판매가 sell을 입력받아 이익률(%)을 소수 첫째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요. (이익률 = (판매가-원가)/원가*100)",
        "1 ≤ cost ≤ 1,000,000, 0 ≤ sell ≤ 1,000,000", ["cost", "sell"],
        "def solution(cost, sell):\n    return round((sell - cost) / cost * 100, 1)\n",
        [(1000, 1200), (5000, 4500), (2000, 2000), (100, 150)],
    ),
    (
        "삼각형 둘레 구하기", "상",
        "삼각형의 세 변 a, b, c를 입력받아 둘레를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    return a + b + c\n",
        [(3, 4, 5), (6, 6, 6), (1, 1, 1), (10, 20, 30)],
    ),
    (
        "온도 변화량 절댓값", "상",
        "이전 온도 t1과 이후 온도 t2를 입력받아 변화량의 절댓값을 반환하는 solution 함수를 완성하세요.",
        "-100 ≤ t1, t2 ≤ 100", ["t1", "t2"],
        "def solution(t1, t2):\n    return abs(t2 - t1)\n",
        [(20, 25), (30, 10), (-5, 5), (0, 0)],
    ),
]

LIST_TUPLE = [
    (
        "리스트 최댓값 찾기", "하",
        "정수 리스트 numbers를 입력받아 가장 큰 값을 반환하는 solution 함수를 완성하세요. (내장 함수 max 사용 금지)",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return max(numbers)\n",
        [([3, 7, 2],), ([-1, -5, -2],), ([10],), ([5, 5, 5, 9, 1],)],
    ),
    (
        "리스트 최솟값 찾기", "하",
        "정수 리스트 numbers를 입력받아 가장 작은 값을 반환하는 solution 함수를 완성하세요. (내장 함수 min 사용 금지)",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return min(numbers)\n",
        [([3, 7, 2],), ([-1, -5, -2],), ([10],), ([5, 5, 5, 9, 1],)],
    ),
    (
        "리스트 합계 구하기", "하",
        "정수 리스트 numbers를 입력받아 모든 원소의 합을 반환하는 solution 함수를 완성하세요. (내장 함수 sum 사용 금지)",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sum(numbers)\n",
        [([1, 2, 3],), ([10, 20, 30],), ([-5, 5],), ([0, 0, 0],)],
    ),
    (
        "리스트 평균 구하기", "하",
        "정수 리스트 numbers를 입력받아 평균을 소수 둘째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return round(sum(numbers) / len(numbers), 2)\n",
        [([1, 2, 3],), ([10, 20],), ([5, 5, 5, 5],), ([1, 2, 3, 4, 5],)],
    ),
    (
        "짝수 개수 세기", "하",
        "정수 리스트 numbers에서 짝수의 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sum(1 for x in numbers if x % 2 == 0)\n",
        [([1, 2, 3, 4, 5, 6],), ([1, 3, 5],), ([2, 4, 6, 8],), ([-2, -3, 0, 7],)],
    ),
    (
        "홀수 개수 세기", "하",
        "정수 리스트 numbers에서 홀수의 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sum(1 for x in numbers if x % 2 != 0)\n",
        [([1, 2, 3, 4, 5, 6],), ([1, 3, 5],), ([2, 4, 6, 8],), ([-2, -3, 0, 7],)],
    ),
    (
        "리스트 뒤집기", "하",
        "정수 리스트 numbers를 입력받아 순서를 뒤집은 리스트를 반환하는 solution 함수를 완성하세요. (reverse, [::-1] 사용 금지)",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return numbers[::-1]\n",
        [([1, 2, 3],), ([5],), ([1, 2, 3, 4, 5],), ([9, 8, 7, 6],)],
    ),
    (
        "특정 값의 개수 세기", "하",
        "정수 리스트 numbers와 정수 target을 입력받아 target이 등장하는 횟수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers", "target"],
        "def solution(numbers, target):\n    return numbers.count(target)\n",
        [([1, 2, 2, 3], 2), ([1, 1, 1], 2), ([5, 5, 5, 5], 5), ([1, 2, 3], 9)],
    ),
    (
        "특정 값 존재 여부", "하",
        "정수 리스트 numbers와 정수 target을 입력받아 target이 리스트에 존재하면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers", "target"],
        "def solution(numbers, target):\n    return target in numbers\n",
        [([1, 2, 3], 2), ([1, 2, 3], 9), ([5], 5), ([4, 4, 4], 9)],
    ),
    (
        "원소 합이 짝수인지 판별", "하",
        "정수 리스트 numbers를 입력받아 모든 원소의 합이 짝수이면 True, 홀수이면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sum(numbers) % 2 == 0\n",
        [([1, 2, 3],), ([2, 4, 6],), ([1, 1, 1],), ([0],)],
    ),
    (
        "두 리스트의 원소별 합", "중",
        "같은 길이의 정수 리스트 a와 b를 입력받아 같은 위치의 원소끼리 더한 새 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(a) = len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return [x + y for x, y in zip(a, b)]\n",
        [([1, 2, 3], [4, 5, 6]), ([0, 0], [1, 1]), ([5], [5]), ([1, 2], [10, 20])],
    ),
    (
        "최댓값과 최솟값의 차이", "중",
        "정수 리스트 numbers를 입력받아 최댓값과 최솟값의 차이를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return max(numbers) - min(numbers)\n",
        [([1, 5, 3],), ([10, 10, 10],), ([-5, 5],), ([2, 9, 1, 7],)],
    ),
    (
        "두 번째로 큰 값 찾기", "중",
        "정수 리스트 numbers를 입력받아 오름차순으로 정렬했을 때 뒤에서 두 번째 값을 반환하는 solution 함수를 완성하세요.",
        "2 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    s = sorted(numbers)\n    return s[-2]\n",
        [([3, 1, 4, 1, 5],), ([10, 20],), ([7, 7, 7],), ([1, 2, 3, 4],)],
    ),
    (
        "리스트 중복 제거하기", "중",
        "정수 리스트 numbers를 입력받아 중복을 제거하되 처음 등장한 순서를 유지한 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    seen = []\n    for x in numbers:\n        if x not in seen:\n            seen.append(x)\n    return seen\n",
        [([1, 2, 2, 3, 1],), ([5, 5, 5],), ([1, 2, 3],), ([4, 1, 4, 2, 1],)],
    ),
    (
        "리스트 오름차순 정렬", "중",
        "정수 리스트 numbers를 입력받아 오름차순으로 정렬한 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sorted(numbers)\n",
        [([3, 1, 2],), ([5, 4, 3, 2, 1],), ([1],), ([10, -2, 7],)],
    ),
    (
        "리스트 내림차순 정렬", "중",
        "정수 리스트 numbers를 입력받아 내림차순으로 정렬한 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sorted(numbers, reverse=True)\n",
        [([3, 1, 2],), ([5, 4, 3, 2, 1],), ([1],), ([10, -2, 7],)],
    ),
    (
        "상위 N개 합 구하기", "중",
        "정수 리스트 numbers와 정수 n을 입력받아 가장 큰 값부터 n개를 뽑아 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ len(numbers) ≤ 1,000", ["numbers", "n"],
        "def solution(numbers, n):\n    return sum(sorted(numbers, reverse=True)[:n])\n",
        [([1, 5, 3, 9, 2], 2), ([4, 4, 4], 1), ([10, 20, 30, 40], 3), ([7], 1)],
    ),
    (
        "리스트 왼쪽으로 회전시키기", "중",
        "정수 리스트 numbers와 정수 k를 입력받아 리스트를 왼쪽으로 k칸 회전시킨 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000, 0 ≤ k", ["numbers", "k"],
        "def solution(numbers, k):\n    k %= len(numbers)\n    return numbers[k:] + numbers[:k]\n",
        [([1, 2, 3, 4, 5], 2), ([1, 2, 3], 1), ([1, 2, 3, 4], 4), ([5, 6, 7], 5)],
    ),
    (
        "양수만 필터링", "중",
        "정수 리스트 numbers를 입력받아 0보다 큰 값만 순서대로 모은 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return [x for x in numbers if x > 0]\n",
        [([1, -2, 3, -4],), ([-1, -2],), ([5, 5, 5],), ([0, 1, -1],)],
    ),
    (
        "음수만 필터링", "중",
        "정수 리스트 numbers를 입력받아 0보다 작은 값만 순서대로 모은 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return [x for x in numbers if x < 0]\n",
        [([1, -2, 3, -4],), ([-1, -2],), ([5, 5, 5],), ([0, 1, -1],)],
    ),
    (
        "각 원소 제곱한 새 리스트", "중",
        "정수 리스트 numbers를 입력받아 각 원소를 제곱한 새 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return [x * x for x in numbers]\n",
        [([1, 2, 3],), ([-1, -2],), ([0, 5],), ([4],)],
    ),
    (
        "두 리스트의 공통 원소 찾기", "중",
        "정수 리스트 a와 b를 입력받아 두 리스트에 모두 존재하는 원소를, a에 등장하는 순서대로 중복 없이 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(a), len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    result = []\n    for x in a:\n        if x in b and x not in result:\n            result.append(x)\n    return result\n",
        [([1, 2, 3], [2, 3, 4]), ([1, 1, 2], [1, 3]), ([5, 6], [7, 8]), ([1, 2, 3, 2], [2, 2, 3])],
    ),
    (
        "짝수만 골라 합 구하기", "상",
        "정수 리스트 numbers를 입력받아 짝수만 골라서 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return sum(x for x in numbers if x % 2 == 0)\n",
        [([1, 2, 3, 4],), ([1, 3, 5],), ([2, 4, 6],), ([0, -2, 3],)],
    ),
    (
        "리스트를 절반으로 나눠 앞부분 반환", "상",
        "정수 리스트 numbers를 입력받아 앞쪽 절반(길이를 2로 나눈 몫만큼)을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return numbers[:len(numbers) // 2]\n",
        [([1, 2, 3, 4],), ([1, 2, 3, 4, 5],), ([1, 2],), ([1],)],
    ),
    (
        "좌표 사이 거리 계산", "상",
        "평면 좌표 p1=[x1, y1]과 p2=[x2, y2]를 입력받아 두 점 사이의 거리를 소수 둘째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ 좌표값 ≤ 1,000", ["p1", "p2"],
        "def solution(p1, p2):\n    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5, 2)\n",
        [([0, 0], [3, 4]), ([1, 1], [1, 1]), ([0, 0], [1, 1]), ([2, 3], [7, 9])],
    ),
    (
        "평균 이상 개수 세기", "상",
        "정수 리스트 numbers를 입력받아 평균 이상인 원소의 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    avg = sum(numbers) / len(numbers)\n    return sum(1 for x in numbers if x >= avg)\n",
        [([1, 2, 3, 4, 5],), ([10, 10, 10],), ([1, 100],), ([5, 5, 5, 10],)],
    ),
    (
        "홀수 인덱스 원소만 골라내기", "상",
        "리스트 numbers를 입력받아 인덱스가 홀수인 원소만 순서대로 모은 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    return numbers[1::2]\n",
        [([1, 2, 3, 4, 5],), ([10, 20, 30],), ([1],), ([1, 2],)],
    ),
    (
        "두 리스트 번갈아 합치기", "상",
        "같은 길이의 리스트 a와 b를 입력받아 a[0], b[0], a[1], b[1] 순서로 번갈아 이어붙인 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(a) = len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    result = []\n    for x, y in zip(a, b):\n        result.append(x)\n        result.append(y)\n    return result\n",
        [([1, 3, 5], [2, 4, 6]), ([1], [2]), ([1, 2], [3, 4]), ([9, 9], [1, 1])],
    ),
    (
        "최빈값 찾기", "상",
        "정수 리스트 numbers를 입력받아 가장 많이 등장하는 값을 반환하는 solution 함수를 완성하세요. 등장 횟수가 같다면 먼저 등장한 값을 반환합니다.",
        "1 ≤ len(numbers) ≤ 1,000", ["numbers"],
        "def solution(numbers):\n    counts = {}\n    for x in numbers:\n        counts[x] = counts.get(x, 0) + 1\n    best = numbers[0]\n    for x in numbers:\n        if counts[x] > counts[best]:\n            best = x\n    return best\n",
        [([1, 2, 2, 3],), ([5, 5, 6, 6, 6],), ([1, 1, 2, 2],), ([7],)],
    ),
    (
        "n번 반복되는 리스트 만들기", "상",
        "값 x와 정수 n을 입력받아 x를 n번 반복해서 담은 리스트를 반환하는 solution 함수를 완성하세요. (* 연산자 사용 금지)",
        "0 ≤ n ≤ 1,000", ["x", "n"],
        "def solution(x, n):\n    result = []\n    for _ in range(n):\n        result.append(x)\n    return result\n",
        [(1, 3), ("a", 2), (0, 5), (7, 1)],
    ),
]

STRING = [
    (
        "문자열 뒤집기", "하",
        "문자열 s를 입력받아 뒤집은 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s[::-1]\n",
        [("hello",), ("python",), ("a",), ("코딩테스트",)],
    ),
    (
        "문자열 길이 구하기", "하",
        "문자열 s를 입력받아 길이를 반환하는 solution 함수를 완성하세요. (내장 함수 len 사용 금지)",
        "0 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return len(s)\n",
        [("hello",), ("a",), ("파이썬",), ("",)],
    ),
    (
        "특정 문자 개수 세기", "하",
        "문자열 s와 문자 ch를 입력받아 s 안에 ch가 등장하는 횟수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s", "ch"],
        "def solution(s, ch):\n    return s.count(ch)\n",
        [("banana", "a"), ("hello", "l"), ("aaaa", "a"), ("abc", "z")],
    ),
    (
        "팰린드롬 판별", "하",
        "문자열 s를 입력받아 앞뒤가 같은 문자열(팰린드롬)이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s == s[::-1]\n",
        [("level",), ("hello",), ("a",), ("noon",)],
    ),
    (
        "문자열 대문자로 변환", "하",
        "문자열 s를 입력받아 모두 대문자로 변환하여 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s.upper()\n",
        [("hello",), ("Python",), ("ABC",), ("a1b2",)],
    ),
    (
        "공백 개수 세기", "하",
        "문자열 s를 입력받아 공백 문자의 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s.count(' ')\n",
        [("hello world",), ("a b c",), ("noSpace",), ("   ",)],
    ),
    (
        "모음 개수 세기", "하",
        "영문자로 이루어진 문자열 s를 입력받아 모음(a, e, i, o, u, 대소문자 무관)의 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return sum(1 for c in s.lower() if c in 'aeiou')\n",
        [("hello",), ("PYTHON",), ("bcdfg",), ("aeiou",)],
    ),
    (
        "대소문자 무시하고 비교하기", "하",
        "문자열 a와 b를 입력받아 대소문자를 무시했을 때 같은 문자열이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(a), len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return a.lower() == b.lower()\n",
        [("Hello", "hello"), ("abc", "ABD"), ("Python", "PYTHON"), ("a", "A")],
    ),
    (
        "앞뒤 공백 제거하기", "하",
        "문자열 s를 입력받아 앞뒤 공백을 제거한 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s.strip()\n",
        [("  hello  ",), ("python",), ("   a",), ("b   ",)],
    ),
    (
        "첫 글자만 대문자로 바꾸기", "하",
        "문자열 s를 입력받아 첫 글자만 대문자로 바꾼 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s[:1].upper() + s[1:]\n",
        [("hello",), ("python code",), ("a",), ("Already",)],
    ),
    (
        "구분자로 나눠 리스트로 반환", "중",
        "문자열 s와 구분자 sep을 입력받아 sep 기준으로 나눈 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s", "sep"],
        "def solution(s, sep):\n    return s.split(sep)\n",
        [("a,b,c", ","), ("2024-01-01", "-"), ("hello world", " "), ("a::b::c", "::")],
    ),
    (
        "리스트를 구분자로 합치기", "중",
        "문자열 리스트 words와 구분자 sep을 입력받아 sep으로 이어붙인 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(words) ≤ 1,000", ["words", "sep"],
        "def solution(words, sep):\n    return sep.join(words)\n",
        [(["a", "b", "c"], ","), (["2024", "01", "01"], "-"), (["hello", "world"], " "), (["x"], ",")],
    ),
    (
        "문자열에서 숫자만 추출하기", "중",
        "문자열 s를 입력받아 숫자 문자만 순서대로 모은 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return ''.join(c for c in s if c.isdigit())\n",
        [("a1b2c3",), ("hello",), ("2024-01-01",), ("999",)],
    ),
    (
        "문자열에서 알파벳만 추출하기", "중",
        "문자열 s를 입력받아 알파벳 문자만 순서대로 모은 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return ''.join(c for c in s if c.isalpha())\n",
        [("a1b2c3",), ("123",), ("Hello, World!",), ("abc",)],
    ),
    (
        "문자 번갈아 이어붙이기", "중",
        "문자열 a와 b를 입력받아 a와 b의 문자를 한 글자씩 번갈아 이어붙인 문자열을 반환하는 solution 함수를 완성하세요. (짧은 쪽 길이만큼만 사용)",
        "1 ≤ len(a), len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    result = ''\n    for x, y in zip(a, b):\n        result += x + y\n    return result\n",
        [("abc", "123"), ("xy", "12"), ("a", "1"), ("ab", "xyz")],
    ),
    (
        "연속 문자 압축하기", "중",
        "알파벳 소문자로 이루어진 문자열 s에서 연속으로 반복되는 문자를 '문자+개수' 형태로 압축한 문자열을 반환하는 solution 함수를 완성하세요. 개수가 1이면 숫자는 생략합니다. 예: 'aaabbc' -> 'a3b2c'",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    result = ''\n    count = 1\n    for i in range(1, len(s)):\n        if s[i] == s[i - 1]:\n            count += 1\n        else:\n            result += s[i - 1] + (str(count) if count > 1 else '')\n            count = 1\n    result += s[-1] + (str(count) if count > 1 else '')\n    return result\n",
        [("aaabbc",), ("abc",), ("aaaa",), ("aabbaa",)],
    ),
    (
        "특정 단어 등장 횟수 세기", "중",
        "공백으로 구분된 문자열 s와 단어 word를 입력받아 word가 몇 번 등장하는지 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s", "word"],
        "def solution(s, word):\n    return s.split().count(word)\n",
        [("나는 학교에 간다 학교는 좋다", "학교에"), ("a a a b", "a"), ("hello world", "world"), ("x y z", "w")],
    ),
    (
        "단어 개수 세기", "중",
        "공백으로 구분된 문자열 s를 입력받아 단어의 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return len(s.split())\n",
        [("hello world",), ("a b c d",), ("onlyone",), ("  spaced   out  ",)],
    ),
    (
        "각 단어 길이를 리스트로 반환", "중",
        "공백으로 구분된 문자열 s를 입력받아 각 단어의 길이를 순서대로 담은 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return [len(w) for w in s.split()]\n",
        [("hello world",), ("a bb ccc",), ("python",), ("x y",)],
    ),
    (
        "가장 긴 단어 찾기", "중",
        "공백으로 구분된 문자열 s를 입력받아 가장 긴 단어를 반환하는 solution 함수를 완성하세요. (가장 긴 단어가 여럿이면 먼저 등장한 단어)",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return max(s.split(), key=len)\n",
        [("the quick brown fox",), ("a bb ccc",), ("python",), ("cat dog bird",)],
    ),
    (
        "카이사르 암호 만들기", "상",
        "알파벳 소문자로 이루어진 문자열 s와 이동할 칸 수 k를 입력받아, 각 알파벳을 k칸씩 뒤로 밀어서 암호화한 문자열을 반환하는 solution 함수를 완성하세요. (z 다음은 다시 a로 순환)",
        "1 ≤ len(s) ≤ 1,000, 0 ≤ k ≤ 25", ["s", "k"],
        "def solution(s, k):\n    result = ''\n    for c in s:\n        if c.isalpha():\n            base = ord('a')\n            result += chr((ord(c) - base + k) % 26 + base)\n        else:\n            result += c\n    return result\n",
        [("abc", 1), ("xyz", 3), ("hello", 2), ("a", 25)],
    ),
    (
        "중복 문자 제거하기", "상",
        "문자열 s를 입력받아 중복 문자를 제거하되 처음 등장한 순서를 유지한 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    seen = ''\n    for c in s:\n        if c not in seen:\n            seen += c\n    return seen\n",
        [("programming",), ("aabbcc",), ("hello",), ("a",)],
    ),
    (
        "애너그램 판별하기", "상",
        "문자열 a와 b를 입력받아 두 문자열이 애너그램(같은 문자로 재배열 가능)이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(a), len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return sorted(a) == sorted(b)\n",
        [("listen", "silent"), ("hello", "world"), ("abc", "cab"), ("aabb", "abab")],
    ),
    (
        "문자열 n번 반복하기", "상",
        "문자열 s와 정수 n을 입력받아 s를 n번 반복한 문자열을 반환하는 solution 함수를 완성하세요. (* 연산자 사용 금지)",
        "1 ≤ len(s) ≤ 100, 0 ≤ n ≤ 100", ["s", "n"],
        "def solution(s, n):\n    result = ''\n    for _ in range(n):\n        result += s\n    return result\n",
        [("ab", 3), ("x", 5), ("hi", 1), ("no", 0)],
    ),
    (
        "특정 문자 치환하기", "상",
        "문자열 s와 문자 old, new를 입력받아 s에서 old를 모두 new로 바꾼 문자열을 반환하는 solution 함수를 완성하세요. (replace 사용 금지)",
        "1 ≤ len(s) ≤ 1,000", ["s", "old", "new"],
        "def solution(s, old, new):\n    result = ''\n    for c in s:\n        result += new if c == old else c\n    return result\n",
        [("banana", "a", "o"), ("hello", "l", "L"), ("abc", "x", "y"), ("aaa", "a", "b")],
    ),
    (
        "이진수 문자열을 십진수로 변환", "상",
        "0과 1로 이루어진 이진수 문자열 s를 입력받아 십진수 정수로 변환하여 반환하는 solution 함수를 완성하세요. (int(s, 2) 사용 금지)",
        "1 ≤ len(s) ≤ 32", ["s"],
        "def solution(s):\n    result = 0\n    for c in s:\n        result = result * 2 + int(c)\n    return result\n",
        [("101",), ("1111",), ("0",), ("100000",)],
    ),
    (
        "십진수를 이진수 문자열로 변환", "상",
        "0 이상의 정수 n을 입력받아 이진수 문자열로 변환하여 반환하는 solution 함수를 완성하세요. (bin() 사용 금지)",
        "0 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    if n == 0:\n        return '0'\n    result = ''\n    while n > 0:\n        result = str(n % 2) + result\n        n //= 2\n    return result\n",
        [(5,), (0,), (255,), (32,)],
    ),
    (
        "숫자로만 이루어진 문자열 판별", "상",
        "문자열 s를 입력받아 모든 문자가 숫자이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "0 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return s.isdigit()\n",
        [("12345",), ("12a45",), ("",), ("007",)],
    ),
    (
        "대문자, 소문자 개수 세기", "상",
        "문자열 s를 입력받아 [대문자 개수, 소문자 개수]를 리스트로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    return [sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())]\n",
        [("Hello World",), ("ABC",), ("abc",), ("Python3.9",)],
    ),
    (
        "두 문자열 합쳐 정렬하기", "상",
        "문자열 a와 b를 입력받아 두 문자열을 합친 뒤 문자 단위로 오름차순 정렬한 문자열을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(a), len(b) ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return ''.join(sorted(a + b))\n",
        [("bca", "fed"), ("z", "a"), ("hello", "world"), ("ab", "ba")],
    ),
]

LOOP = [
    (
        "구구단 리스트 만들기", "하",
        "정수 n을 입력받아 n단 구구단 결과(n*1부터 n*9까지)를 리스트로 반환하는 solution 함수를 완성하세요.",
        "2 ≤ n ≤ 9", ["n"],
        "def solution(n):\n    return [n * i for i in range(1, 10)]\n",
        [(2,), (5,), (9,), (3,)],
    ),
    (
        "소수 판별하기", "하",
        "정수 n을 입력받아 소수이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 10,000", ["n"],
        "def solution(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n",
        [(2,), (4,), (1,), (17,), (97,), (100,)],
    ),
    (
        "FizzBuzz 리스트 만들기", "하",
        "1부터 n까지의 정수에 대해, 3의 배수이면 'Fizz', 5의 배수이면 'Buzz', 둘 다의 배수이면 'FizzBuzz', 그 외에는 숫자를 문자열로 변환한 값을 순서대로 담은 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100", ["n"],
        "def solution(n):\n    result = []\n    for i in range(1, n + 1):\n        if i % 15 == 0:\n            result.append('FizzBuzz')\n        elif i % 3 == 0:\n            result.append('Fizz')\n        elif i % 5 == 0:\n            result.append('Buzz')\n        else:\n            result.append(str(i))\n    return result\n",
        [(5,), (15,), (1,), (20,)],
    ),
    (
        "1부터 n까지 합 구하기", "하",
        "정수 n을 입력받아 1부터 n까지의 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    return n * (n + 1) // 2\n",
        [(1,), (5,), (10,), (100,)],
    ),
    (
        "1부터 n까지 짝수의 합", "하",
        "정수 n을 입력받아 1부터 n까지 짝수의 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    return sum(i for i in range(1, n + 1) if i % 2 == 0)\n",
        [(10,), (1,), (7,), (20,)],
    ),
    (
        "1부터 n까지 홀수의 합", "하",
        "정수 n을 입력받아 1부터 n까지 홀수의 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    return sum(i for i in range(1, n + 1) if i % 2 != 0)\n",
        [(10,), (1,), (7,), (20,)],
    ),
    (
        "n의 팩토리얼", "하",
        "0 이상의 정수 n을 입력받아 n의 팩토리얼(n!)을 반환하는 solution 함수를 완성하세요.",
        "0 ≤ n ≤ 15", ["n"],
        "def solution(n):\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result\n",
        [(0,), (1,), (5,), (10,)],
    ),
    (
        "피보나치 수열 n번째 항", "하",
        "정수 n을 입력받아 피보나치 수열의 n번째 항을 반환하는 solution 함수를 완성하세요. (1번째 항과 2번째 항은 모두 1입니다)",
        "1 ≤ n ≤ 30", ["n"],
        "def solution(n):\n    a, b = 1, 1\n    for _ in range(n - 1):\n        a, b = b, a + b\n    return a\n",
        [(1,), (2,), (5,), (10,)],
    ),
    (
        "피보나치 수열 리스트 만들기", "하",
        "정수 n을 입력받아 피보나치 수열의 앞 n개 항을 리스트로 반환하는 solution 함수를 완성하세요. (1번째 항과 2번째 항은 모두 1입니다)",
        "1 ≤ n ≤ 30", ["n"],
        "def solution(n):\n    fibs = []\n    a, b = 1, 1\n    for _ in range(n):\n        fibs.append(a)\n        a, b = b, a + b\n    return fibs\n",
        [(1,), (2,), (5,), (8,)],
    ),
    (
        "최대공약수 구하기", "하",
        "정수 a와 b를 입력받아 두 수의 최대공약수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ a, b ≤ 100,000", ["a", "b"],
        "def solution(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n",
        [(12, 18), (7, 13), (100, 75), (24, 36)],
    ),
    (
        "최소공배수 구하기", "중",
        "정수 a와 b를 입력받아 두 수의 최소공배수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ a, b ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    def gcd(x, y):\n        while y:\n            x, y = y, x % y\n        return x\n    return a * b // gcd(a, b)\n",
        [(4, 6), (3, 5), (21, 6), (8, 12)],
    ),
    (
        "자릿수 합 구하기", "중",
        "0 이상의 정수 n을 입력받아 각 자릿수의 합을 반환하는 solution 함수를 완성하세요.",
        "0 ≤ n ≤ 1,000,000", ["n"],
        "def solution(n):\n    return sum(int(d) for d in str(n))\n",
        [(123,), (9,), (1000,), (4567,)],
    ),
    (
        "자릿수 개수 세기", "중",
        "0 이상의 정수 n을 입력받아 자릿수의 개수를 반환하는 solution 함수를 완성하세요.",
        "0 ≤ n ≤ 1,000,000", ["n"],
        "def solution(n):\n    return len(str(n))\n",
        [(5,), (123,), (1000000,), (0,)],
    ),
    (
        "숫자 뒤집기", "중",
        "0 이상의 정수 n을 입력받아 자릿수를 뒤집은 정수를 반환하는 solution 함수를 완성하세요.",
        "0 ≤ n ≤ 1,000,000", ["n"],
        "def solution(n):\n    return int(str(n)[::-1])\n",
        [(123,), (100,), (7,), (4560,)],
    ),
    (
        "회문 숫자 판별하기", "중",
        "0 이상의 정수 n을 입력받아 자릿수를 뒤집어도 같은 수(회문 숫자)이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "0 ≤ n ≤ 1,000,000", ["n"],
        "def solution(n):\n    return str(n) == str(n)[::-1]\n",
        [(121,), (123,), (7,), (12321,)],
    ),
    (
        "n까지의 소수 개수 세기", "중",
        "정수 n을 입력받아 2 이상 n 이하의 소수 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 10,000", ["n"],
        "def solution(n):\n    count = 0\n    for i in range(2, n + 1):\n        is_prime = True\n        for j in range(2, int(i ** 0.5) + 1):\n            if i % j == 0:\n                is_prime = False\n                break\n        if is_prime:\n            count += 1\n    return count\n",
        [(10,), (1,), (20,), (2,)],
    ),
    (
        "n 이하의 소수 리스트 만들기", "중",
        "정수 n을 입력받아 2 이상 n 이하의 소수를 오름차순 리스트로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 10,000", ["n"],
        "def solution(n):\n    result = []\n    for i in range(2, n + 1):\n        is_prime = True\n        for j in range(2, int(i ** 0.5) + 1):\n            if i % j == 0:\n                is_prime = False\n                break\n        if is_prime:\n            result.append(i)\n    return result\n",
        [(10,), (1,), (20,), (2,)],
    ),
    (
        "별 삼각형 문자열 만들기", "중",
        "정수 n을 입력받아, i번째 줄에 별(*)이 i개 있는 n줄짜리 삼각형을 줄바꿈으로 이어붙인 문자열로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 20", ["n"],
        "def solution(n):\n    lines = []\n    for i in range(1, n + 1):\n        lines.append('*' * i)\n    return '\\n'.join(lines)\n",
        [(3,), (1,), (5,), (2,)],
    ),
    (
        "완전수 판별하기", "중",
        "정수 n을 입력받아, 자기 자신을 제외한 약수의 합이 자기 자신과 같으면 True(완전수), 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 10,000", ["n"],
        "def solution(n):\n    total = 0\n    for i in range(1, n):\n        if n % i == 0:\n            total += i\n    return total == n\n",
        [(6,), (28,), (10,), (1,)],
    ),
    (
        "약수 리스트 구하기", "중",
        "정수 n을 입력받아 n의 약수를 오름차순 리스트로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 10,000", ["n"],
        "def solution(n):\n    return [i for i in range(1, n + 1) if n % i == 0]\n",
        [(12,), (7,), (1,), (28,)],
    ),
    (
        "약수 개수 구하기", "상",
        "정수 n을 입력받아 n의 약수 개수를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 10,000", ["n"],
        "def solution(n):\n    return sum(1 for i in range(1, n + 1) if n % i == 0)\n",
        [(12,), (7,), (1,), (28,)],
    ),
    (
        "n단 구구단 문자열 리스트", "상",
        "정수 n을 입력받아 'n x i = 결과' 형식의 문자열을 i=1부터 9까지 담은 리스트로 반환하는 solution 함수를 완성하세요.",
        "2 ≤ n ≤ 9", ["n"],
        "def solution(n):\n    return [f'{n} x {i} = {n * i}' for i in range(1, 10)]\n",
        [(2,), (9,), (5,), (3,)],
    ),
    (
        "3 또는 5의 배수 합 구하기", "상",
        "정수 n을 입력받아 1 이상 n 이하의 정수 중 3 또는 5의 배수의 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)\n",
        [(10,), (20,), (3,), (1,)],
    ),
    (
        "학점 계산하기", "상",
        "점수 score를 입력받아 90점 이상 'A', 80점 이상 'B', 70점 이상 'C', 60점 이상 'D', 그 외 'F'를 반환하는 solution 함수를 완성하세요.",
        "0 ≤ score ≤ 100", ["score"],
        "def solution(score):\n    if score >= 90:\n        return 'A'\n    elif score >= 80:\n        return 'B'\n    elif score >= 70:\n        return 'C'\n    elif score >= 60:\n        return 'D'\n    else:\n        return 'F'\n",
        [(95,), (85,), (72,), (50,)],
    ),
    (
        "윤년 판별하기", "상",
        "연도 year를 입력받아 윤년이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요. (4의 배수이면서 100의 배수가 아니거나, 400의 배수이면 윤년)",
        "1 ≤ year ≤ 9999", ["year"],
        "def solution(year):\n    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0\n",
        [(2024,), (2023,), (1900,), (2000,)],
    ),
    (
        "삼각형 성립 여부 판별하기", "상",
        "세 변의 길이 a, b, c를 입력받아 삼각형을 만들 수 있으면 True, 없으면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    return (a + b > c) and (b + c > a) and (a + c > b)\n",
        [(3, 4, 5), (1, 1, 3), (6, 6, 6), (2, 2, 5)],
    ),
    (
        "직각삼각형 판별하기", "상",
        "세 변의 길이 a, b, c를 입력받아 직각삼각형이면 True, 아니면 False를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ a, b, c ≤ 1,000", ["a", "b", "c"],
        "def solution(a, b, c):\n    sides = sorted([a, b, c])\n    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2\n",
        [(3, 4, 5), (5, 4, 3), (2, 3, 4), (6, 8, 10)],
    ),
    (
        "n번째 짝수 구하기", "상",
        "정수 n을 입력받아 n번째 짝수(2, 4, 6, ...)를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    return n * 2\n",
        [(1,), (5,), (10,), (100,)],
    ),
    (
        "n번째 홀수 구하기", "상",
        "정수 n을 입력받아 n번째 홀수(1, 3, 5, ...)를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ n ≤ 100,000", ["n"],
        "def solution(n):\n    return n * 2 - 1\n",
        [(1,), (5,), (10,), (100,)],
    ),
    (
        "두 수 사이의 정수 합", "상",
        "정수 a와 b(a ≤ b)를 입력받아 a부터 b까지 모든 정수의 합을 반환하는 solution 함수를 완성하세요.",
        "-1,000 ≤ a ≤ b ≤ 1,000", ["a", "b"],
        "def solution(a, b):\n    return sum(range(a, b + 1))\n",
        [(1, 5), (3, 3), (10, 20), (-2, 2)],
    ),
]

DICT = [
    (
        "평균 이상 학생 찾기", "하",
        "학생 이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아 전체 평균 이상의 점수를 받은 학생 이름을 리스트로 반환하는 solution 함수를 완성하세요. 이름은 딕셔너리에 등장하는 순서를 유지합니다.",
        "1 ≤ len(scores) ≤ 100", ["scores"],
        "def solution(scores):\n    avg = sum(scores.values()) / len(scores)\n    return [name for name, score in scores.items() if score >= avg]\n",
        [({"철수": 80, "영희": 90, "민수": 60},), ({"A": 70, "B": 70, "C": 70},), ({"A": 100, "B": 0},), ({"x": 50, "y": 60, "z": 40},)],
    ),
    (
        "최고 점수 학생 이름 찾기", "하",
        "학생 이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아 가장 높은 점수를 받은 학생의 이름을 반환하는 solution 함수를 완성하세요. 동점이 여럿이면 먼저 등장한 학생을 반환합니다.",
        "1 ≤ len(scores) ≤ 100", ["scores"],
        "def solution(scores):\n    best = None\n    for name, score in scores.items():\n        if best is None or score > scores[best]:\n            best = name\n    return best\n",
        [({"철수": 80, "영희": 90, "민수": 60},), ({"A": 100, "B": 50},), ({"x": 10},), ({"a": 5, "b": 5, "c": 9},)],
    ),
    (
        "최저 점수 학생 이름 찾기", "하",
        "학생 이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아 가장 낮은 점수를 받은 학생의 이름을 반환하는 solution 함수를 완성하세요. 동점이 여럿이면 먼저 등장한 학생을 반환합니다.",
        "1 ≤ len(scores) ≤ 100", ["scores"],
        "def solution(scores):\n    worst = None\n    for name, score in scores.items():\n        if worst is None or score < scores[worst]:\n            worst = name\n    return worst\n",
        [({"철수": 80, "영희": 90, "민수": 60},), ({"A": 100, "B": 50},), ({"x": 10},), ({"a": 9, "b": 5, "c": 5},)],
    ),
    (
        "점수 딕셔너리의 평균 구하기", "하",
        "이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아 점수의 평균을 소수 둘째 자리까지 반올림하여 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(scores) ≤ 100", ["scores"],
        "def solution(scores):\n    return round(sum(scores.values()) / len(scores), 2)\n",
        [({"a": 80, "b": 90},), ({"a": 100},), ({"a": 0, "b": 0, "c": 100},), ({"a": 70, "b": 80, "c": 90},)],
    ),
    (
        "딕셔너리 값들의 합 구하기", "하",
        "딕셔너리 d를 입력받아 모든 값의 합을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return sum(d.values())\n",
        [({"a": 1, "b": 2, "c": 3},), ({"x": 10},), ({"a": -5, "b": 5},), ({"a": 0},)],
    ),
    (
        "문자별 등장 횟수 세기", "하",
        "문자열 s를 입력받아 각 문자가 몇 번 등장하는지를 담은 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(s) ≤ 1,000", ["s"],
        "def solution(s):\n    counts = {}\n    for c in s:\n        counts[c] = counts.get(c, 0) + 1\n    return counts\n",
        [("banana",), ("hello",), ("a",), ("aabbcc",)],
    ),
    (
        "리스트 원소별 등장 횟수 세기", "하",
        "문자열 리스트 items를 입력받아 각 원소가 몇 번 등장하는지를 담은 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(items) ≤ 1,000", ["items"],
        "def solution(items):\n    counts = {}\n    for x in items:\n        counts[x] = counts.get(x, 0) + 1\n    return counts\n",
        [(["a", "b", "a", "c", "b", "a"],), (["x", "x"],), (["p"],), (["a", "b", "c"],)],
    ),
    (
        "특정 값 이상인 키 목록 반환", "하",
        "딕셔너리 d와 기준값 threshold를 입력받아 값이 threshold 이상인 키를 리스트로 반환하는 solution 함수를 완성하세요. 키는 등장 순서를 유지합니다.",
        "1 ≤ len(d) ≤ 100", ["d", "threshold"],
        "def solution(d, threshold):\n    return [k for k, v in d.items() if v >= threshold]\n",
        [({"a": 10, "b": 20, "c": 5}, 10), ({"x": 1, "y": 2}, 5), ({"a": 100}, 50), ({"a": 1, "b": 2, "c": 3}, 2)],
    ),
    (
        "두 딕셔너리 합치기", "하",
        "딕셔너리 a와 b를 입력받아 합친 딕셔너리를 반환하는 solution 함수를 완성하세요. 같은 키가 있으면 두 값을 더합니다.",
        "0 ≤ len(a), len(b) ≤ 100", ["a", "b"],
        "def solution(a, b):\n    result = dict(a)\n    for k, v in b.items():\n        result[k] = result.get(k, 0) + v\n    return result\n",
        [({"a": 1, "b": 2}, {"b": 3, "c": 4}), ({"x": 5}, {"x": 5}), ({"a": 1}, {"b": 2}), ({}, {"a": 1})],
    ),
    (
        "값 기준 내림차순 정렬 키 리스트", "하",
        "딕셔너리 d를 입력받아 값이 큰 순서대로 정렬한 키 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return [k for k, v in sorted(d.items(), key=lambda kv: -kv[1])]\n",
        [({"a": 3, "b": 1, "c": 2},), ({"x": 5, "y": 5},), ({"a": 1},), ({"a": 10, "b": 20, "c": 5},)],
    ),
    (
        "값 기준 오름차순 정렬 키 리스트", "중",
        "딕셔너리 d를 입력받아 값이 작은 순서대로 정렬한 키 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return [k for k, v in sorted(d.items(), key=lambda kv: kv[1])]\n",
        [({"a": 3, "b": 1, "c": 2},), ({"x": 5, "y": 5},), ({"a": 1},), ({"a": 10, "b": 20, "c": 5},)],
    ),
    (
        "최댓값을 가진 키 찾기", "중",
        "딕셔너리 d를 입력받아 값이 가장 큰 키를 반환하는 solution 함수를 완성하세요. 동점이 여럿이면 먼저 등장한 키를 반환합니다.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    best = None\n    for k, v in d.items():\n        if best is None or v > d[best]:\n            best = k\n    return best\n",
        [({"a": 1, "b": 5, "c": 3},), ({"x": 10},), ({"a": 5, "b": 5},), ({"a": -1, "b": -5},)],
    ),
    (
        "최솟값을 가진 키 찾기", "중",
        "딕셔너리 d를 입력받아 값이 가장 작은 키를 반환하는 solution 함수를 완성하세요. 동점이 여럿이면 먼저 등장한 키를 반환합니다.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    worst = None\n    for k, v in d.items():\n        if worst is None or v < d[worst]:\n            worst = k\n    return worst\n",
        [({"a": 1, "b": 5, "c": 3},), ({"x": 10},), ({"a": 5, "b": 5},), ({"a": -1, "b": -5},)],
    ),
    (
        "총점 딕셔너리를 평균 딕셔너리로 변환", "중",
        "학생 이름을 키, 총점을 값으로 갖는 딕셔너리 totals와 과목 수 n을 입력받아, 각 학생의 평균 점수를 소수 둘째 자리까지 반올림한 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(totals) ≤ 100, 1 ≤ n ≤ 20", ["totals", "n"],
        "def solution(totals, n):\n    return {k: round(v / n, 2) for k, v in totals.items()}\n",
        [({"a": 270, "b": 240}, 3), ({"x": 100}, 2), ({"a": 90, "b": 180}, 3), ({"a": 50}, 1)],
    ),
    (
        "두 리스트로 딕셔너리 만들기", "중",
        "이름 리스트 names와 점수 리스트 scores를 입력받아 이름을 키, 점수를 값으로 갖는 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(names) = len(scores) ≤ 100", ["names", "scores"],
        "def solution(names, scores):\n    return dict(zip(names, scores))\n",
        [(["a", "b", "c"], [1, 2, 3]), (["x"], [10]), (["p", "q"], [5, 6]), (["a", "b"], [0, 0])],
    ),
    (
        "딕셔너리 키 목록 정렬해서 반환", "중",
        "딕셔너리 d를 입력받아 키를 오름차순으로 정렬한 리스트를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return sorted(d.keys())\n",
        [({"b": 1, "a": 2},), ({"z": 1, "x": 2, "y": 3},), ({"a": 1},), ({"c": 1, "b": 2, "a": 3},)],
    ),
    (
        "딕셔너리 값 목록 정렬해서 반환", "중",
        "딕셔너리 d를 입력받아 키를 오름차순으로 정렬했을 때의 값 목록을 리스트로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return [d[k] for k in sorted(d.keys())]\n",
        [({"b": 1, "a": 2},), ({"z": 1, "x": 2, "y": 3},), ({"a": 1},), ({"c": 1, "b": 2, "a": 3},)],
    ),
    (
        "기본값과 함께 조회하기", "중",
        "딕셔너리 d, 키 key, 기본값 default를 입력받아 key가 d에 있으면 그 값을, 없으면 default를 반환하는 solution 함수를 완성하세요.",
        "0 ≤ len(d) ≤ 100", ["d", "key", "default"],
        "def solution(d, key, default):\n    return d.get(key, default)\n",
        [({"a": 1}, "a", 0), ({"a": 1}, "b", 0), ({}, "x", 99), ({"a": 1, "b": 2}, "b", -1)],
    ),
    (
        "재고 0인 상품 찾기", "중",
        "상품명을 키, 재고 수량을 값으로 갖는 딕셔너리 stock을 입력받아 재고가 0인 상품명을 리스트로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(stock) ≤ 100", ["stock"],
        "def solution(stock):\n    return [k for k, v in stock.items() if v == 0]\n",
        [({"apple": 0, "banana": 5},), ({"a": 0, "b": 0},), ({"x": 1},), ({"a": 0, "b": 1, "c": 0},)],
    ),
    (
        "장바구니 총액 계산하기", "중",
        "상품명을 키, 가격을 값으로 갖는 딕셔너리 prices와 상품명을 키, 수량을 값으로 갖는 딕셔너리 quantities를 입력받아 총 결제 금액을 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(prices) ≤ 100", ["prices", "quantities"],
        "def solution(prices, quantities):\n    return sum(prices[k] * quantities[k] for k in prices)\n",
        [({"apple": 1000, "banana": 500}, {"apple": 2, "banana": 3}), ({"a": 100}, {"a": 5}), ({"a": 10, "b": 20}, {"a": 1, "b": 1}), ({"x": 0}, {"x": 10})],
    ),
    (
        "값이 짝수인 것만 남기기", "상",
        "딕셔너리 d를 입력받아 값이 짝수인 항목만 남긴 새 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return {k: v for k, v in d.items() if v % 2 == 0}\n",
        [({"a": 1, "b": 2, "c": 4},), ({"x": 1, "y": 3},), ({"a": 2, "b": 4, "c": 6},), ({"a": 0},)],
    ),
    (
        "단어를 길이별로 그룹핑하기", "상",
        "문자열 리스트 words를 입력받아, 단어 길이를 키로 하고 해당 길이의 단어 리스트를 값으로 갖는 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(words) ≤ 100", ["words"],
        "def solution(words):\n    groups = {}\n    for w in words:\n        groups.setdefault(len(w), []).append(w)\n    return groups\n",
        [(["a", "bb", "cc", "ddd"],), (["cat", "dog", "fish"],), (["x"],), (["ab", "cd", "ef", "ghij"],)],
    ),
    (
        "키와 값을 뒤바꾸기", "상",
        "값이 모두 서로 다른 딕셔너리 d를 입력받아 키와 값을 뒤바꾼 새 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return {v: k for k, v in d.items()}\n",
        [({"a": 1, "b": 2},), ({"x": 10},), ({"a": 1, "b": 2, "c": 3},), ({"p": 5},)],
    ),
    (
        "합격 여부 딕셔너리 만들기", "상",
        "이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아, 60점 이상이면 True, 미만이면 False를 값으로 갖는 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(scores) ≤ 100", ["scores"],
        "def solution(scores):\n    return {name: score >= 60 for name, score in scores.items()}\n",
        [({"a": 70, "b": 50},), ({"x": 60},), ({"a": 100, "b": 0},), ({"p": 59, "q": 61},)],
    ),
    (
        "최댓값과 같은 모든 키 찾기", "상",
        "딕셔너리 d를 입력받아 값이 최댓값과 같은 모든 키를 리스트로 반환하는 solution 함수를 완성하세요. 키는 등장 순서를 유지합니다.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    m = max(d.values())\n    return [k for k, v in d.items() if v == m]\n",
        [({"a": 1, "b": 5, "c": 5},), ({"x": 10},), ({"a": 1, "b": 1, "c": 1},), ({"a": -1, "b": -5},)],
    ),
    (
        "투표 결과 1위 후보 찾기", "상",
        "후보 이름을 키, 득표수를 값으로 갖는 딕셔너리 votes를 입력받아 1위 후보 이름을 반환하는 solution 함수를 완성하세요. 동률이면 먼저 등장한 후보를 반환합니다.",
        "1 ≤ len(votes) ≤ 100", ["votes"],
        "def solution(votes):\n    best = None\n    for name, count in votes.items():\n        if best is None or count > votes[best]:\n            best = name\n    return best\n",
        [({"a": 10, "b": 20, "c": 5},), ({"x": 5, "y": 5},), ({"only": 1},), ({"a": 3, "b": 3, "c": 1},)],
    ),
    (
        "공통 키만 남긴 딕셔너리 만들기", "상",
        "딕셔너리 a와 b를 입력받아 두 딕셔너리에 모두 있는 키만 남긴 새 딕셔너리를 반환하는 solution 함수를 완성하세요. 값은 a의 값을 사용합니다.",
        "1 ≤ len(a) ≤ 100", ["a", "b"],
        "def solution(a, b):\n    return {k: v for k, v in a.items() if k in b}\n",
        [({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 9, "d": 9}), ({"x": 1}, {"x": 2}), ({"a": 1}, {"b": 2}), ({"a": 1, "b": 2}, {"a": 9, "b": 9})],
    ),
    (
        "처음 등장 인덱스 딕셔너리 만들기", "상",
        "문자열 리스트 items를 입력받아, 각 원소를 키로 하고 그 원소가 처음 등장한 인덱스를 값으로 갖는 딕셔너리를 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(items) ≤ 100", ["items"],
        "def solution(items):\n    result = {}\n    for i, x in enumerate(items):\n        if x not in result:\n            result[x] = i\n    return result\n",
        [(["a", "b", "a", "c"],), (["x"],), (["a", "a", "a"],), (["p", "q", "r"],)],
    ),
    (
        "등수 딕셔너리 만들기", "상",
        "이름을 키, 점수를 값으로 갖는 딕셔너리 scores를 입력받아, 점수가 높을수록 등수가 높은(1등이 가장 높은 점수) {이름: 등수} 딕셔너리를 반환하는 solution 함수를 완성하세요. 동점이면 먼저 등장한 사람이 더 높은 등수를 받습니다.",
        "1 ≤ len(scores) ≤ 100", ["scores"],
        "def solution(scores):\n    ranked = sorted(scores.items(), key=lambda kv: -kv[1])\n    result = {}\n    for i, (name, _) in enumerate(ranked, start=1):\n        result[name] = i\n    return result\n",
        [({"a": 90, "b": 80, "c": 70},), ({"x": 50},), ({"a": 100, "b": 100},), ({"p": 10, "q": 30, "r": 20},)],
    ),
    (
        "값의 합과 개수 반환하기", "상",
        "딕셔너리 d를 입력받아 [값들의 합, 항목 개수]를 리스트로 반환하는 solution 함수를 완성하세요.",
        "1 ≤ len(d) ≤ 100", ["d"],
        "def solution(d):\n    return [sum(d.values()), len(d)]\n",
        [({"a": 1, "b": 2, "c": 3},), ({"x": 10},), ({"a": 0, "b": 0},), ({"a": 5, "b": 5, "c": 5, "d": 5},)],
    ),
]


def _default_literal(expected):
    if isinstance(expected, bool):
        return "False"
    if isinstance(expected, (int, float)):
        return "0"
    if isinstance(expected, str):
        return '""'
    if isinstance(expected, dict):
        return "{}"
    if isinstance(expected, (list, tuple)):
        return "[]"
    return "None"


def _build_problems():
    problems = []
    pid = 0
    for category, specs in [
        ("기초 문법", BASIC),
        ("리스트/튜플", LIST_TUPLE),
        ("문자열", STRING),
        ("조건/반복", LOOP),
        ("딕셔너리", DICT),
    ]:
        for title, difficulty, description, constraints, params, ref_code, test_args in specs:
            pid += 1
            namespace = {}
            exec(ref_code, namespace)
            ref_fn = namespace["solution"]

            test_cases = []
            for i, args in enumerate(test_args):
                expected = ref_fn(*args)
                test_cases.append({"args": list(args), "expected": expected, "hidden": i >= 2})

            default_lit = _default_literal(test_cases[0]["expected"])
            params_str = ", ".join(params)
            starter_code = (
                f"def solution({params_str}):\n"
                f"    answer = {default_lit}\n"
                f"    # 여기에 코드를 작성하세요\n"
                f"    return answer\n"
            )

            problems.append(
                {
                    "id": pid,
                    "title": title,
                    "category": category,
                    "difficulty": difficulty,
                    "function_name": "solution",
                    "params": params,
                    "description": description,
                    "constraints": constraints,
                    "starter_code": starter_code,
                    "test_cases": test_cases,
                }
            )
    return problems


PROBLEMS = _build_problems()
PROBLEMS_BY_ID = {p["id"]: p for p in PROBLEMS}
CATEGORIES = CATEGORY_ORDER
DIFFICULTIES = ["하", "중", "상"]
