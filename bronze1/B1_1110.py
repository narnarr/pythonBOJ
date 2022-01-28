# 더하기 사이클
n = int(input())
init, i = n, 0

while True:
    n = n%10*10 + (n//10+n%10)%10
    i+=1

    if n == init:
        print(i)
        break