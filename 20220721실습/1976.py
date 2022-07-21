import sys

sys.stdin = open("input.txt", "r")

T = int(input())
clock = []
for i in range(1,T+1):
    
    h1, m1, h2, m2 = map(int,input().split())
   
    h = h1 + h2
    m = m1 + m2

    if h > 12 and m < 60:
        h = h - 12
        print(f'#{i}',h,m,end='')
        print('')
        
    elif h > 12 and m > 60:
        h = h - 11
        m = m - 60
        print(f'#{i}',h,m,end='')
        print('')
        
    elif h < 12 and m > 60:
        h = h + 1
        m = m - 60
        print(f'#{i}',h,m,end='')
        print('')
        
    else :
        print(f'#{i}',h,m,end='')
        print('')       