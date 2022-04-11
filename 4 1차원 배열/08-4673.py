# 생성자 있는 수 넣을 selection이라는 set 새로 넣어줌
selection = set()

# 생성자 만드는 함수
# 모든 생성자는 selection 안에 들어가게 만듦
def select(n):
    num = n
    for i in range(len(str(n))):
        num += int(str(n)[i])
    selection.add(num)

# 생성자 만드는 함수 호출 => 실제로 1부터 10000까지의 number 중 생성자가 있는 애들은 다 selection 안에 들어감
for j in range(1, 10001):
    select(j)

# 만들어진 셀프 넘버 아닌 수를 1 ~ 10000까지의 set에서 빼 주고 순서대로 정렬(sorted -> 오름차순으로 정렬해줌)
self_num = sorted(set(range(1, 10001)) - selection)

# 한 줄에 하나씩 출력
for result in self_num:
    print(result)