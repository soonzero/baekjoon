import sys

# input() 대신 sys.stdin.readline()을 사용하는 이유

# 반복문으로 여러 줄을 입력 받아야 할 때에 input()으로 입력 받으면, 시간 초과가 발생할 수 있음.
# 따라서 sys.stdin.readline()을 사용해야 시간 초과가 발생하지 않음.
# 한 개의 정수를 입력 받을 때 
    # a = int(sys.stdin.readline())
# 정해진 개수의 정수를 한 줄에 입력 받을 때
    # a, b, c = map(int, sys.stdin.readline().split())
# 임의의 개수의 정수를 n줄 입력 받아 2차원 리스트에 저장할 때
    # data = []
    # n = int(sys.stdin.readline())
    # for i in range(n)
    #   data.append(list(map(int, sys.stdin.readline().split())))
# "문자열" n줄을 입력 받아 리스트에 저장할 때
    # n = int(sys.stdin.readline())
    # data = [sys.stdin.realine().strip() for i in range(n)]
    # ... strip()은 문자열 맨 앞과 맨 끝의 공백 문자를 제거

# 참고: https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# sys.stdin.readline()을 for문 안에 넣기 복잡해 보이면 처음부터 input을 다음과 같이 정의해주면 편함
# input = sys.stdin.readline
# 그러면 a, b = map(int, input().split()) 이렇게 간단해짐