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
# marks=int(input("Enter your Marks :  "))
# if(marks>=90 and marks<=100):
#     print("Your Grade is A+")
# elif(marks>=80 and marks<90):
#     print("Your Grade is A")
# elif(marks>=70 and marks<80):
#     print("Your Grade is B+")
# elif(marks>=60 and marks<70):
#     print("Your Grade is B")
# else:
#      print("You are Fail , Try Again")   


#Nested if else
age=int(input("Enter your Age :"))
if age>=18:
    print("You are Eligible to Voting")
    if age>=21:
        print("You are Eligible for Driving")
        if age>=24:
            print("You are Eligible for Marriage")
        else:
            print("You are not Eligible for Marriage")
    else:
        print("You are not Eligible for Driving")
else:
    print("You are not Eligible to Voting")
