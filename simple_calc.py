
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("""
Please select one operation out of the following:
1. add
2.subtract
3.multiply
4.divide
""")

select = int(input("Select operations from 1, 2, 3, 4: "))
print(select)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("invalid input")