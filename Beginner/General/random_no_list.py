import random

numbers = [random.randint(1,50) for i in range(10)]

print("Random numbers", numbers)

unique = random.sample(range(1, 51), 10)

print("Unique random numbers", unique)