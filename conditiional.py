day_of_week = input("Enter the day of week").lower()
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("i will learn Live Devops")
else:
    print("I will practice Devops")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Enter the operation: [options +, -, *]")

if choice == "+":
   sum = num1 + num2 
   print("Addition",sum)
elif choice == "-":
    sub = num1 - num2 
    print("subrations",sub)

else:
    print("Invalid")