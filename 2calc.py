def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


print("please select: \n" "1.Add\n" "2.Substraction\n" "3.Multiplication\n" "4.Division\n")

select = int(input("select from 1, 2, 3, 4 : "))

num1=int(input("Enter first number:"))
num2=int(input("Enter second number: "))
 

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))


elif select == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
 
elif select == 3:
    print(num1, "*", num2, "=", mul(num1, num2))
 
elif select == 4:
    print(num1, "/", num2, "=", div(num1, num2))


else:
    print("Invalid input")