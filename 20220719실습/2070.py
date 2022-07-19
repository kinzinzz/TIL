T = int(input())

for i in range(1,T+1):
    a, b = map(int,input().split())
    if(a < b):
        print("#"f'{i}','<',end='')
    elif(a == b):
        print("#"f'{i}','=',end='')
    else:
        print("#"f'{i}','>',end='')
    print()