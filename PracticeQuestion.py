#Q1.... write a program to input 2 numbers and print their sum

# a=int(input("Enter karo pahla Number : "))
# b=int(input("Enter karo dusra Number : "))
# sum=a+b
# print("sum of both number =",sum)

#Q2...WAP to input side of a square and print area of squear

# side=float(input("Enter Side of a Square(cm) :"))
# # area=side*side
# area=side**2
# print("Area of your Square :",area)

#Q3... WAP to input 2 Floating Number and print their average

# a=float(input("Enter First Floating Number :"))
# b=float(input("Enter Second Floating Number :"))
# sum=a+b
# average=sum/2
# print("Average of those Number : ",average)

# """Q4... WAP to input 2 Number and print ture if a<=b efse false"""

# a=int(input("Enter your first Num a : "))
# b=int(input("Enter your secand Num b :"))
# print(a<=b)

# Q5.....WAP to input user's First Name & Print its lengh

# name=input("Enter your Name")
# print("lenth of Name :",len(name))

#Q6....WAP to find the occurrence/count of '$' in a string 

# name="Praksh"
# print(name,"in a :",name.count("a"))

# #Q7.... Audlt Checker 
# Name=input("Enter Your Name :")
# age=int(input("Enter Your Age : "))
# if age>=18 :
#     print(Name,"you name Eligible to voting ")
# else :
#     print(Name,"you are not eligible to voting" )

#Q8.... WAP to check if a number entered by the user is odd or even.

# num=int(input("Enter Your Number :"))
# if(num%2==0):
#     print(num,"is Even Number" )
# else :
#     print(num,"is odd Number")

#Q9....WAP to find the greatest of 3 number entered by the user.
# a=int(input("Enter you Number a : "))
# b=int(input("Enter your Number b :"))
# c=int(input("Enter your Number c : "))
# if(a>b and b>c):
#     print("a is Greatest NUmber" )
# elif(b>a and b>c):
#     print("b is greatest Number ")
# elif(c>a and c>b):
#     print("c is Greatest Number ")
# else :
#     print("I think some number are Equale Check Again")

#Q10...WAP to check if a number is a multiple of 7 or Not?

# num=int(input("Enter  Your Number : "))
# if (num%7==0) :
#     print(num,"Is multiple of 7 ")
# else :
#     print(num,"Is not Multiple of 7")

#Q11....WAP to ask the user to enter names
#  of their 3 favorite movies & store them in a list 
movies=[]
mov1=input("enter your first movie")
mov2=input("Enter your second movie")
mov3=input("Enter your third movie")
# movies=[mov1,mov2,mov3]
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

