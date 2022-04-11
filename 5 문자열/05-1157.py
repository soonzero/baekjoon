str = input().upper()
char = list(set(str))
# char.sort() => 굳이 필요가 없음
arr = []

for i in range(len(char)):
    arr.append(str.count(char[i]))

if arr.count(max(arr)) >= 2:
    print("?")
else:
    print(char[arr.index(max(arr))])