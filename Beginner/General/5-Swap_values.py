a = int(input("Enter value of first variable-"))
b = int(input("Enter value of second variable-"))

print("value of a before swapping-", a)
print("value of b before swapping-", b)

# first way to swap values is
a, b = b, a
print("value of a after swapping-", a)
print("value of b after swapping-", b)


# second way
a = a + b
b = a - b
a = a - b
print("value of a after swapping-", a)
print("value of b after swapping-", b)