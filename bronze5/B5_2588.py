# 곱셈

# a = int(input())
# b = int(input())
# print(a*(b%10), a*(b//10%10), a*(b//100), a*b, sep='\n')

# 문자열로 받아지니 필요한 자리수만 정수로 변환해서 계산하자
a = int(input())
b = input()
print(a*int(b[-1]), a*int(b[-2]), a*int(b[-3]), a*int(b), sep='\n')