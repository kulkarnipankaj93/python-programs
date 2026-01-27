#Program to find and count vowels in string
str1 = input("Enter the string- ")
no_vowels = []
count = 0
vowels = "aeiouAEIOU"

for i in str1:
    if i in vowels:
        no_vowels.append(i)
        count += 1

print(f"List of vowels in {str1}", no_vowels)
print(f"Total number of vowels in {str1}-", count)
