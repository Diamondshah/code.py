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

class car():
    comp="BMW"
    def __init__(self,color,price):
        self.colour=color
        self.price=price

car1=car("blur",25000)
car2=car("Red",36000)
print(car1.colour,car1.comp,car1.price)
print(car2.comp,car2.colour,car2.price)