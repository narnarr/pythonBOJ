# 문자열 반복
for _ in range(int(input())):
    n, str = input().split()
    p=''
    for s in str:
        p += s*int(n)
    print(p)