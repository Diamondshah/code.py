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
# a="Diamond"
# print(a[0:3])  #0 to 2
# print(a[1:5])  #1 to 4
# print(a[2:])   #2 to end
# print(a[:4])   #0 to 3
# print(a[:])    #0 to end
# print(a[1:6:2]) #1 to 5 with step 2
# print(a[::2])   #0 to end with step 2
# print(a[::-1])  #reverse the string
# print(a[-1:-6:-1]) #reverse the string from index -1 to -5
# print(a[-3:-8:-1]) #reverse the string from index -3 to
# print(a[-5:-1])   #from index -5 to -2
# print(a[-6:])    #from index -6 to end
# print(a[:-2])    #from index 0 to -3
# print(a[-6:-1])  #from index -6 to -2
# print(a[-7:-1])  #from index -7 to -2
# print(a[-7:5])   #from index -7 to 4
# print(a[-7:6])   #from index -7 to 5

#Functions in String
a="Hello World"
print(a.upper())  #convert to uppercase
print(a.lower())  #convert to lowercase
print(a.capitalize()) #capitalize the first character
print(a.title())  #capitalize the first character of each word
print(a.count("o")) #count the number of occurrences of a character
print(a.find("o"))  #find the index of the first occurrence of a character
print(a.replace("o","a")) #replace a character with another character
print(a.split(" "))  #split the string into a list of words
b="Hello,World,Python"
print(b.split(","))  #split the string into a list of words
print(a.strip())  #remove leading and trailing spaces
c="   Hello World   "
print(c.strip())  #remove leading and trailing spaces
print(c.lstrip()) #remove leading spaces
print(c.rstrip()) #remove trailing spaces
print(a.startswith("H")) #check if the string starts with a character
print(a.endswith("d"))   #check if the string ends with a character
print(a.isalpha())  #check if the string contains only alphabets
print(a.isdigit())  #check if the string contains only digits
d="12345"
print(d.isdigit())  #check if the string contains only digits
print(a.isalnum())  #check if the string contains only alphanumeric characters
e="Hello123"
print(e.isalnum())  #check if the string contains only alphanumeric characters
print(a.index("o"))  #find the index of the first occurrence of a character
print(a.rindex("o")) #find the index of the last occurrence of a character
print(a.center(20))  #center the string with spaces
print(a.ljust(20))  #left justify the string with spaces
print(a.rjust(20))  #right justify the string with spaces
print(a.zfill(20))  #pad the string with zeros on the left
f="hello world"
print(f.swapcase())  #swap the case of each character
g="HELLO WORLD"
print(g.swapcase())  #swap the case of each character
h="hello world"