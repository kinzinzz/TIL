number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(float(total) / float(count))

#total 과 count 모두 int형이므로 연산결과도 int 형이다. 따라서 실수형으로 바꾼다
#// 연산자는 몫을 구하는 연사자이므로 연사자를 / 로 바꾼다