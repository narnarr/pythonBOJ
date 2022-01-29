# 평균은 넘겠지
for _ in range(int(input())):
    scores = list(map(int, input().split()))
    n = scores.pop(0)

    avg = sum(scores)/n
    cnt = 0
    for s in scores:
        if s > avg:
            cnt+=1

    print('{:.3f}%'.format(round(cnt/n*100, 3)))