word = "HappyHacking"

count = 0
list = ["a","e","i","o","u"]

for char in word:
    if char in list:
        count += 1

print(count)

# == 타입을 따지는 조건문이기 때문에 비교하기 위해서는 in과 list 를 이용한다.