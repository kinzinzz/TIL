n = int(input())

for i in range(1,n+1):
    m = list(map(int,input().split()))
    if m[2] > m[4]:
        if(m[0] * m[4]) > (m[1]):
            print(f'#{i}',m[1],end=' ')
        else :
            print(f'#{i}',m[0] * m[4],end=' ')
    else :
        if(m[0] * m[4]) > (m[1] + (m[4]-m[2])*m[3]):
            print(f'#{i}',m[1] + (m[4]-m[2])*m[3],end=' ')
        else :
            print(f'#{i}',m[0] * m[4],end=' ')
    print('')