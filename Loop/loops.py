#loops.........
#loop is used to repeat a block of code multiple
#  times until a certain condition is met.
# loops are use to repeart instructions.
# Types of loops in python 
# 1...while loop      2....For loop

# while loop.......(jab-tak)
# num=15
# while 0<=num:
#     print(num,"ruko jara sabar karo .")
#     num=num-1

# print 1 to 9 number 
# num=1 
# while  num<=9:
#     print(num)
#     num=num+1

#Q....Print number from 1 to 100
# num=1
# while num<=100:
#     print(num)
#     num=num+1

#Q....Print number from 100 to 1
# num=100
# while num>=0:
#     print(num)
#     num=num-1

#Q....Print the multiplication table of a number n.
# num=1
# value=int(input("enter the number "))
# while num<=10:
#     print(num*value)
#     num=num+1
#Q....Print the elements of the following list using a loop


# list=[1,4,9,16,25,36,49,64,81,100]
# n=0
# while n<=len(list):
#     print(list[n])
#     n=n+1

# num=1
# list={}
# while num<=10:
#     list{print(num**2)}
#     num=num+1
# Search for a number X in this tuple using loop:
list=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the value of X "))
n=0
while n < len(list) :
    if(x==list[n]):
        print(n,"found")
    n=n+1