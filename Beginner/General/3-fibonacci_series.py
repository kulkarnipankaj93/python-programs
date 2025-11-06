# Program to generate Fibonacci series

n = int(input("Enter how many terms you want: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
