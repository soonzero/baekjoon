a = int(input())
b = int(input())
c = int(input())
mul = str(a * b * c)
arr = []

for i in range(10):
    arr.append(mul.count(str(i)))
    print(arr[i])