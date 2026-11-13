#Como hacer una calculadora

def sum(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation: ") #+, -, *, /

total = ""
if operation == "+":
    total = sum(num1, num2)
elif operation == "-":
    total = minus(num1, num2)
elif operation == "*":
    total = multiply(num1, num2)
elif operation == "/":
    total = divide(num1, num2)
else:
    print("Invalid operation")

print(total)