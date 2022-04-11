a, b = input().split()
a = a[2] + a[1] + a[0]
b = b[2] + b[1] + b[0]

if int(a) > int(b):
    print(a)
else:
    print(b)

# 세 개 이상의 수를 비교하는 거라면 for문이랑 list를 사용하면 편리할 것 같지만, 
# 두 개의 다른 수를 비교하는 거라서 굳이 사용하지 않았음