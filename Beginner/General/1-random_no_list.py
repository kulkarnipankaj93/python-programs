import random

# Program to generate random numbers from 1 to 50.
numbers = [random.randint(1,50) for i in range(10)]
print("Random numbers", numbers)


# Program to generate Unique random numbers from 1 to 50.
unique = random.sample(range(1, 51), 10)
print("Unique random numbers", unique)
