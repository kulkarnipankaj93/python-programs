# Program to find if the given string is palindrome or not
str1 = input("Enter the string- ")
# rev_str1 = str1[::-1]             # first way to reverse string
rev_str1 = "".join(reversed(str1))  # second way to reverse string
if rev_str1 == str1:
    print("given string is palindrome")
else:
    print("given string is not palindrome")
