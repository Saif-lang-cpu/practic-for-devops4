num1 = int(input("give first number"))
num2 = int(input("give  second number"))
choise = input("enter fvrt symbol: (options +,-,*,%)")
if choise == "+":
    add = num1+num2
    print("additions is",add)

elif choise == "-":
    add = num1-num2
    print("minus  is",add)

elif choise == "*":
    add = num1*num2
    print("multiply is",add)

elif choise == "%":
    add = num1%num2
    print("divide is is",add)

else:
    print("yrrrrr kya choose kr liyay bro") 