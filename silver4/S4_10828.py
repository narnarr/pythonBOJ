import sys

N = int(sys.stdin.readline())
stk = []

for _ in range(N):
    temp = sys.stdin.readline().split()
    cmd = temp[0]

    if cmd == "push":
        stk.append(temp[1])
    elif cmd == "pop":
        if len(stk) > 0:
            print(stk.pop(-1))
        else:
            print(-1)
    elif cmd == "size":
        print(len(stk))
    elif cmd == "top":
        if len(stk) > 0:
            print(stk[-1])
        else:
            print(-1)
    else:
        if len(stk) == 0:
            print(1)
        else:
            print(0)