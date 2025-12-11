"""#Opp in Python 
# To map with real world scenarios,we started using objects in code.
#This is called object oriented programming."""

""" Procedural Programing me hub line by line sab kuch likhte hai jise hamara code 
kafi lamba ho jata hai orsame code ko kai bar use parne per likhna parta hai """

"""in the function redendancy decrease hota hai or 
code reuseblity increas hota hai """

#OOP:- Object Orianted Programing 
#Procudural -----> Function----->OOp
#opps is a Game of class and object  

#Class & Object in Python:-
#Class is a blueprint for creating objects.
#creating class
# class Student:
#     name = "Diamond Kumar"
#     age = 20
# #creating object (instance)
# s1 = Student()
# print(s1.name)
# print(s1.name,"\n" ,"age =",s1.age)

# class Student:
#     name = "Diamond"

# s1=Student()
# print(s1)
# print(s1.name)
# s2=Student()
# print(s2.name)

# class car:
#     color="blur"
#     brand="BMW"
# car1=car()
# print(car1)
# print(car1.color)
# print(car1.brand)
"""
# __init__ Function:
#Constructor
#All classes have a function called __init _()
which is always excuted when the class is being initiated""" 

#Creating Class
# class Student:
#     def __init__(self,fullname,num_age):
#         self.name = fullname
#         self.age = num_age

# #creating object
# s1=Student("karan",28)
# print(s1.name)
# print(s1.age)
# s2=Student("Diamond",20)
# print(s2.name,"and age=",s2.age)

""" The self parameter is a reference to the current 
instance of the class, and is used to access variables
that belong to the class"""
# #Defult Constructors
# class Student:
#     def __init__(self):

#parameterized constractor(name,age)
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1=Student("Mohan",12)
# s2=Student("ramu",15)
# s3=Student("Kalu",16)

# print(s1.name)

# ......Class & Instance Attributes...
# Instance attributes ----> self.name,self.age(becouse sabka alag alag hoga)
#Class Attributes---> only one time stored in memory (becouse sabka same hoga)

# class car():
#     comp="BMW"
#     def __init__(self,color,price):
#         self.colour=color
#         self.price=price

# car1=car("blur",25000)
# car2=car("Red",36000)
# print(car1.colour,car1.comp,car1.price)
# print(car2.comp,car2.colour,car2.price)

#.........Methods........
#Methods are functions that belongs to objects.

# class Student():
#     c_name="RIMT University"
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):
#         print("welcome student,",self.name)
    
#     def get_marks(self):
#        print(self.marks)

# s1=Student("Dimaond",99)
# # s1.welcome()
# s1.get_marks()
# """
# #Q...Create student class that takes name & marks of 3 subjects as
# argument in canstructor. Then create a method to print the average"""
# class Student():
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name=name
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def avg(self):
#         sum=self.sub1+self.sub2+self.sub3
#         average=sum/3
#         print(average)
# s1=Student("Diamond",65,95,33)
# s1.avg()

#Static Methods
#methodsthat don't use the self parameter(work at class level)"""
              #opp Important 
              # Abstraction 
              # Encapsulation
              #Inheratience
              #Polymorphism

#Abstraction:-(bina kam ki chijhe user se chhupa lena bas kam wali chijhe hi dikhan )
#Hiding the implementation detail od a class and only showing
#the essentaila feature to the user.

#Encapsulation:-
#Wrapping data and Function into a single unit (object)

#Abstraction:-


# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started..")

# car1=Car()
# car1.start()

#Create Account class with 2 attributes-Balance & 
# account no,create method for debit ,credit &  printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    #debite method
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited..")
        print("total balance =",self.get_balance())

     def credit(self,amount):
  s     self.balance += amount
        print("Rs",amount,"was credited..")
    def get_balance(self):
        return self.balance
    
acc1=Account(25000,123456)
acc1.debit(1500)
acc1.credit(500)