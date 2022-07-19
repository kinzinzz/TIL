T = int(input())

for i in range(1,T+1):
    j = input().split(' ')
    temp = len(j)
    j = map(int,j)
    print("#"f'{i}',"{:.0f}".format(sum(j)/temp),end='')
    print()



