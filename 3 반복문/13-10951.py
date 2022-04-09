# 입력이 없는 경우에는 break를 해줘야 하기 때문에 try, except 문을 사용해줘야 함
# 사용하지 않으면 while: True 이기 때문에 무조건 계속 실행되기 때문

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break