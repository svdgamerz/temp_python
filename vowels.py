num = input("Enter a word")
vowels = 'aeiouAEIOU'
count = 0

for char in num:
    if char in vowels:
        count += 1

print("Number of vowels:" , count )