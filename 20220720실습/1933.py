n = int(input())
list = []
for i in range(1,1001):
    if n % i == 0:
        list.append(i)

for j in list:
    print(j, end=' ') 