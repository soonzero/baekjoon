# h, m = map(int, input().split())
# p = int(input())
# h_p = p // 60
# m_p = p % 60

# if m + m_p >= 60:
#     m += m_p - 60
#     if h + h_p + 1 >= 24:
#         h += h_p - 23
#     else:
#         h += h_p + 1
# else:
#     m += m_p
#     if h + h_p >= 24:
#         h += h_p - 24
#     else:
#         h += h_p

# print(h, m)

h, m = map(int, input().split())
p = int(input())
h += p // 60
m += p % 60

if m >= 60:
    h += 1
    m -= 60

if h >= 24:
    h -= 24

print(h, m)