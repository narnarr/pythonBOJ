l = int(input())
word = input()

total = 0

for i in range(l):
    total += (ord(word[i])-96) * (31**i) % 1234567891

print(total%1234567891)