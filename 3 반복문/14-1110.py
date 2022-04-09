original_num = input()
if int(original_num) < 10:
    original_num = "0" + original_num

new_num = original_num

count = 0

while True:
    temp = str(int(new_num[0]) + int(new_num[1]))
    new_num = new_num[-1] + temp[-1]
    count += 1

    if new_num == original_num:
        print(count)
        break
