num1 = float(input("Enter first value- "))
num2 = float(input("Enter second value- "))

print("/n select operations from below choices:")
print("1- Addition (+)")
print("2- Subtraction (-)")
print("3- Multiplication (*)")
print("4- Division (/)")

choice = input("Enter choice 1/2/3/4 : ")

if choice == "1":
    print("Addition of values is-", num1+num2)

elif choice == "2":
    print("Subtraction of values is-", num1-num2)

elif choice == "3":
    print("Multiplication of values is-", num1*num2)

elif choice == "4":
    if num2 != 0:
        print("Division of values is-", num1/num2)
    else:
        print("Division of zero is not allowed")

else:
    print("Invalid choice")