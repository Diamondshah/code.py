#del Keyword:-
# Used to delete object properties or object itself.
# """
# del s1.name
# del s1
# """
# class Student():
#     def __init__(self,name):
#         self.name=name
# s1=Student("Prince")
# del s1.name
# print (s1.name)

#Private(like) attributes & methods(just use __ in front)
"""
Conceptual lmpementation in python
Private attributes & methods to be used only within the class and are not 
accessible from outside the class.
"""
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
    
# acc1=Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())

#Inheritance:-
#when one class(child/drived) derives the properties & methods of another class(parent/base).

class Car:
    color="Black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car Stoped..")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortuner")
car2=ToyotaCar("prius")
print(car1.name)
print(car1.start())
print(car1.color)