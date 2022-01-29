# 단어 공부
string = input().upper()
al_count = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in alphabet:
    al_count.append(string.count(a))

print('?' if al_count.count(max(al_count))>1 else alphabet[al_count.index(max(al_count))])