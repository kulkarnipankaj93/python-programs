"""" create one function which will return all even and odd number
from range of 1 to 20
after that sum of all even numbers in second function
note: do not create global variable"""


def add(a):
    addition = 0
    for i in a:
        addition = addition + i
    return addition


def to_sort():
    even = []
    odd = []
    for i in range(1,21):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result = add(even)
    return even, odd, result


a, b, c = to_sort()
print("list of even numbers", a)
print("list of odd numbers", b)
print("addition of even numbers", c)

"""Create one function which will return prime numbers from range 1 to 100
and store in the list which is inside the tuple"""

# def prime_num():
#     for i in range(1,101):

"""To find even and odd numbers and store them in dictionary"""
dict1 = {}

for i in range(1,10):
    if i%2 == 0:
        dict1[i] = "even"
    else:
        dict1[i] = "odd"

print(dict1)

""" Find largest number from given list """
list1 = [77, 48, 95, 2, 21]
list1.sort()
print(list1)
print(list1[-1])


