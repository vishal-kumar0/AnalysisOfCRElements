f = open("promoter_chromosome1.txt", "r")

text = f.read()
#text = "AAAAGCCGACAAAAAGCCGACSSSSSSACCGACSSSSSSSSSSSSSSSSSSSS"

pat1 = "ACCGAC"

p1 = len(pat1)


locs = []

for i in range(len(text)):
    if text[i:i+p1] == pat1 :
        locs.append(i)

print(len(locs))

freq = [0] * 31

for i in range(len(locs)):
    for j in range(i+1, len(locs)):
        diff = locs[j] - locs[i] - p1
        if 0 < diff <= 30:
            freq[diff] = freq[diff] + 1

print(freq[1:])
