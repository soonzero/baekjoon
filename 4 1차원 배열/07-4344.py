for i in range(int(input())):
    arr = list(map(int, input().split()))
    count = 0
    for j in arr[1:]:
        if j > (sum(arr[1:]) / arr[0]):
            count += 1
    print(f"{(count / arr[0] * 100):.3f}%")

# f-string: {}안에 변수, 연산 넣을 수 있음
# 소수점 표현: {} 안에 :.(자리수)f