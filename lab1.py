#task 3
num1 = int(input("Enter number 1: ")) 
num2 = int(input("Enter number 2: ")) 
num3 = int(input("Enter number 3: ")) 
num4 = int(input("Enter number 4: ")) 
num5 = int(input("Enter number 4: ")) 
ALL_values=[num1,num2,num3,num4,num5]
print(ALL_values)
ALL_values.sort()
print(ALL_values)
#task4
num1 = int(input("Enter marks 1: ")) 
num2 = int(input("Enter marks 2: ")) 
num3 = int(input("Enter nmarks 3: "))
average=num1+num2+num3/3 
if(num1 < 33 or num2 < 33 or num3 < 33) :
    print("you are fail")
elif(average < 40) :
    print("you are fail again")
else:
    ("congratulations you are paas")