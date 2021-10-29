#Python Program to Make a Simple Calculator

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
        return x / y

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    print(var1,"+",var2,"=", add(var1,var2))
elif choice == '2':
    print(var1,"-",var2,"=", subtract(var1,var2))
elif choice == '3':
    print(var1,"*",var2,"=", multiply(var1,var2))
elif choice == '4':
    print(var1,"/",var2,"=", divide(var1,var2))
else:
    print("Invalid input")
    
