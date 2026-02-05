s = "hello"

freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)


from collections import Counter

s = "hello"
freq = Counter(s)

print(freq)

s = "hello"

freq = {char: s.count(char) for char in s}
print(freq)

