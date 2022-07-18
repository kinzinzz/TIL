numbers = input().split()

int_numbers = list(map(int, numbers))

print(sum(int_numbers))
# 입력받은 데이터형은 문자이므로 sum 메소드를 사용하기 위해서 int 형으로 변환한다.