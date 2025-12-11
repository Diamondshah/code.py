import os
# os.remove("baby2.txt")


#create a practice file useing python and add sum data in given format:
#f=open("practice.txt","w")
#f.write("Hi everyone \nwe are learing File l/O \nusing Java\n I like programming in Java ")

#WAF that replace occurrences of "Java" with "python" in above file.
# f=open("practice.txt","r")
# data=f.read()
# new_data=data.replace("Java" ,"python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)
#Search if the word "learning" exists in the file or not 
def check_word():
    f=open("practice.txt","r")
    data=f.read()
    word="learing"
    if(data.find(word)) != -1:
     print("found")
    else:
        print("not found")
