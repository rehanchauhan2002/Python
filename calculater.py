print("1 Addition")
print("2 subtraction")
print("3 multiplication")
print("4 Division")

choice = int(input(" please select what do you want to choose between 1 to 4"))

num1 = int(input("Enter num 1:"))
num2 = int(input("Enter num 2:"))

a = (num1 + num2)
b = (num1 - num2)
c = (num1 * num2)
d = (num1 / num2)


if (choice == 1):
    print(" your ans is", num1, "+", num2, "=",a)
elif (choice == 2):
    print(" your ans is", num1, "-", num2, "=",b)
elif (choice == 3):   
    print(" your ans is", num1, "*", num2, "=",c)          
elif (choice == 4):
    print(" your ans is", num1, "/", num2, "=",d)
else:
    print("invalid")     
