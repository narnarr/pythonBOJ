# OX퀴즈

for _ in range(int(input())):
    os = input().split('X')

    total = 0
    for o in os: total += len(o)*(len(o)+1)/2
    print(int(total))
