case = int(input())

for i in range(case):
    t, s = input().split()
    for i in range(len(s)):
        print(s[i] * int(t), end = "")
    print()