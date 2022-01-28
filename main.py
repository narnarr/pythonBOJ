# 가변 변수 인자 사용하면?
import sys
n, *x = map(int, sys.stdin.read().split())  # 시간 줄이기 위해 x를 가변인자로 받아보자.
print(min(x), max(x))

