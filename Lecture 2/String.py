#String..........................................
# String is a sequence of characters
# How to Write a String in Python
# There are three ways to write a string in Python:
# a="Hello"
# b='Hello'
# c='''Hello'''
# d="""Hello"""
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#Escape Sequence Characters
# \n=New Line
# \t=Tab
# \\=Backslash
# \'=Single Quote
# \"=Double Quote
# Examples of Escape Sequence Characters


# a="Hello \nWorld"
# b="Hello \tWorld"
# c="Hello \\ World"
# d='Hello \'World\''
# e="Hello \"World\""
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

#String Concatenation
# Concatenation means joining two strings

# a="Hello"
# b="World"
# c=a+" "+b
# print(c)
# print(type(c))
# print(a+b)
# Name="Diamond"
# Greeting="Good Morning"
# print(Greeting+" "+Name)
# print(Greeting+", "+Name)
# print(Greeting+" "+Name+"!")

#Length of String
# len() function is used to find the length of a string
# a="Hello World"
# print(len(a))

#indexing in String
# Indexing means accessing individual characters of a string
# Indexing starts from 0
# a="Diamond"
# print(a[0])
# print(a[1])
# print(a[2])
# bro=a[5]
# print(bro)
# a[8]='P'   not supported

#Negative Indexing
# Negative indexing means accessing individual characters of a string from the end
# a="Diamond"
# print(a[-1])
# print(a[-2])
# print(a[-3])
# bro=a[-4]
# print(bro)
# # a[-5]='P'   #not supported

#Accessing a range of characters in a string
a="Diamond"
print(a[0:3])  #0 to 2
print(a[1:5])  #1 to 4
print(a[2:])   #2 to end
print(a[:4])   #0 to 3
print(a[:])    #0 to end
print(a[1:6:2]) #1 to 5 with step 2
print(a[::2])   #0 to end with step 2
print(a[::-1])  #reverse the string
print(a[-1:-6:-1]) #reverse the string from index -1 to -5
print(a[-3:-8:-1]) #reverse the string from index -3 to
print(a[-5:-1])   #from index -5 to -2
print(a[-6:])    #from index -6 to end
print(a[:-2])    #from index 0 to -3
print(a[-6:-1])  #from index -6 to -2
print(a[-7:-1])  #from index -7 to -2
print(a[-7:5])   #from index -7 to 4
print(a[-7:6])   #from index -7 to 5

