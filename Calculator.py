print("----------------------------------")
print("use + for addition")
print("use - for subractration")
print("use * for multiplication")
print("use / for division")
print("use ** for adding power")
print("use // for rooting")
print("----------------------------------")
num1 = int(input("input no 1 : "))

user_input = input("+,-,*,/,**,// : ")

num2 = int(input("input no 2 : "))

if user_input== "+":
    result = num1+num2
elif user_input== "-":
    result = num1-num2
elif user_input== "*":
    result = num1*num2
elif user_input== "/":
    result = num1/num2
elif user_input== "**":
    result = num1**num2
elif user_input== "//":
    result = num1//num2
print (result)

print("----------------------------------")

