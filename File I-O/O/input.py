#File I/O in Python...
#python can be used to perform operation on a file.(read&write data)
#Type of all files:-
# 1. Text Files:. .txt,.doc,.log...etc.
# 2. Binary Files:. .mp4, .mov, .png, .jpeg etc.
"""
'r'----Open for reading(default)
'w'-----open for writing,truncating the file first
'x'------create a new file and open it for writing
'a'------open for writing,appending to the end of the file if it exists
'b'-------binary mode
't'------text mode(default)
'+'-------open a disk file for updating(reading and writing)


"""
#open,Read and Close a file.....
#We have toi open a file before raeding or writing....
#f=open("file_name","mode")
#fiel_name>>.>>             #mode
#sample.txt              r:read mode
#demo.docx                w: write mode
#data=f.read()
#f.close(q)
# f=open("demo.txt","r")
# data=f.read()
# # print(data)
# print(len(data))
# print(type(data))
# print(data)
# f.close()
# print("hlo")
# f = open("demo.txt", "r+t")  # Open in read+write text mode
# data = f.read()  # Read the file contents
# f.write("Some text")  # Write some text to the file
# f.close()  # Close the file when done
# print(data)  # Print the contents that were read
#Reading a ile and writing a file....
# f1 =open("demo.txt","r") #source file
# f2 =open("demo_copy.txt","w") #destination file
# data =f1.read()
# f2.write(data)
# f1.close()
# f2.close()


#............file input and output:-........
# f=open("File I-O/O/demo.txt","r")
# data=f.read()
# data2=f.readline()
# print(data2)
# # print(data)
# f.close()
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()
# f=open("File I-O/O/demo.txt","a")
# f.write(" Python code looks clean and simple. \n " \
# "It works on all operating systems.\n " \
# "Python is great for beginners.")

# f=open("File I-O/O/demo.txt","r")
# data=f.read()
# print(data)
# f.close()  
# f=open("Baby.txt","a")
# f.write("/this is testing for file creation \n python")
# f=open("Baby2.txt","w")
# f.write("/this is testing for file creation \n python")

# r+.....use for read and write , if we write
# something in r+ mode then text overwrite in the staring 
#  
# w+(truncate + write) mode me file delete ho janega or nya data add karene per so karega

# a+ mode me file read,+ writeing in append mode me open hoga 
#  ishe overwrite nhi hoga staring me data add ho jayega

# ..............with syntax...........

with open("baby.txt","a") as f:
    f.write("aabhi me check kar raha hu \n "
    "ki with open syntax kam kese karta hai ")
    f.close()