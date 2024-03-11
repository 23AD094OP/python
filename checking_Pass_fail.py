print("Checking you Pass or fail in exam:- \n")
print('''Your Mark 
32 is equal or greater then you are pass
32 is less then you are fail \n''')
x = int(input("Enter your mark:- "))
if x>90 and x<=100:
    print("your mark is",x,"\nyou are Pass!!!!!!")
    print("Great work")
elif x>60 and x<=90:
    print("your mark is ",x,"\nYou are Pass!!!!!!")
    print("good")
elif x>=32 and x<=60:
    print("your mark is ", x, "\nYou are Pass!!!!!")
    print("Fine ! better try next time.")
else:
    print(x,"\n You are fail!!!!!")
    print("Your effort is weak!")
