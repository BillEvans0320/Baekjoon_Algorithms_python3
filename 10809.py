# Alphabet

word = input()

alphabet = [-1]*26

for i in range(len(word)-1,-1,-1):
    alphabet[int(ord(word[i]))-97] = i

for j in range(len(alphabet)):
    print(alphabet[j],end=' ')
