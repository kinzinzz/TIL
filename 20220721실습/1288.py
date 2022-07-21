T = int(input())

for i in range(1,T+1):
    N = int(input())
    numbers = set()
    j = 1
    
    while 1:
        k = N * j
        j += 1
        while k > 0:
            numbers.add(k % 10)
            k = k // 10
        if len(numbers) == 10:
            j -= 1
            break     
    print(f'#{i}', j * N, end=' ')     
    print('') 