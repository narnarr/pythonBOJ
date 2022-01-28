# 빠른 A+B
# input()보다 sys.stdin.readline()이 더 빠르다
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))