n = int(input())

for i in range(1,n+1):
    m = int(input())
    result = 0
    for j in range(1,m+1):
        if j % 2 == 0:
            result -= j
        else :
            result += j
    print(f'#{i}',result,end=' ')
    print('')