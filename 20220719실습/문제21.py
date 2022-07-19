n = 1234
list = []
length = 0
result = 0

while n > 0:
    m = n % 10
    n //= 10
    list.append(m)
    length += 1

while length > 0:
    for i in list:
        m = i * (10**(length-1))
        result += m
        length -= 1

print(result)

    
 




