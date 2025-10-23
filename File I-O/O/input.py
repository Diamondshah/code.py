#File I/O in Python...
#python can be used to perform operation on a file.(read&write data)
#Type of all files:-
# 1. Text Files:. .txt,.doc,.log...etc.
# 2. Binary Files:. .mp4, .mov, .png, .jpeg etc.


#open,Read and Close a file.....
#We have toi open a file before raeding or writing....
#f=open("file_name","mode")
#fiel_name>>.>>             #mode
#sample.txt              r:read mode
#demo.docx                w: write mode
#data=f.read()
#f.close(q)
f=open("demo.txt","r")
data=f.read()
# print(data)
print(len(data))
print(type(data))
print(data)
f.close()