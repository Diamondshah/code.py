#Conditional Statements ........
# if       elif         else

# a=5
# b=8
# if a>b:
#     print("a is greater than b")
# elif a==b :
#     print(" a or b Dono equal hai ")
# else :
#     print("b is Greater than a")

#Q..... Grading System
marks=int(input("Enter your Marks :  "))
if(marks>=90 and marks<=100):
    print("Your Grade is A+")
elif(marks>=80 and marks<90):
    print("Your Grade is A")
elif(marks>=70 and marks<80):
    print("Your Grade is B+")
elif(marks>=60 and marks<70):
    print("Your Grade is B")
else:
        print("You are Fail , Try Again")   