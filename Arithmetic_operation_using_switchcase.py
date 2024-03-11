print("1. Addition \n2. Subtraction n \n3. Multiplication\n4. Division\n5. Floor division\n6. Remainder\n7.Exponential\n")
x = int(input("Enter the first number:- "))
y = int(input("Enter the second number:- "))
choice = int(input("Enter the given option(1,2,3,4,5,6,7):-"))
if choice== 1:
     result = x + y
     print("Addition =",result)
elif choice == 2:
    result = x - y
    print("Subtraction : ",result)
elif choice == 3:
     result = x *y
     print("Multiplication :",result)
elif choice == 4:
     result = x / y
     print("Division : ",result)
elif choice == 5:
    result = x//y
    print("Floor divide =",result)
elif choice == 6:
     result = x % y
     print("Remainder : ",result)
elif choice == 7:
  result = x ** y
  print("Exponential : ",result)
else:
 print("Invalid Value")
