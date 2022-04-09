n = int(input())

for i in range(n):
    sum = 0
    score = 1
    answer = input()
    for j in range(len(answer)):
        if answer[j] == "O":
            sum += score
            score += 1
        else:
            score = 1 # O의 연속이 끊기면 score를 초기화 해줘야 함 
    print(sum)