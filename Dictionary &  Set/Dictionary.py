#Dictionary......in Python 
#A dictionary is a collection which is unordered, 
# changeable and indexed. In Python dictionaries are written with curly brackets,
#  and they have keys and values.
#Creating a Dictionary
#Dictionary={key:Value,Kay:Value,Key:Value,Key:Value,Key:Value}
# no_frnd={}
# frnd={
#     "info":["name","age"],
#     "type":("str","inteager"),
#     "Prince":21.5,
#     "avisash":19,
#     "Diamond":20,
#     "Rohit":19,
#     "Nitesh":20
# }
# print(type(no_frnd))
# frnd["yaksh"]=22
# frnd["Rohit"]=20
# print(frnd)
# print(frnd["Diamond"])
# print(frnd["Rohit"])
# print(frnd["Nitesh"])


#Nested Dictionary...........
Result={
    "name":"Prakash",
    "sub":{
        "phy":48,
        "math":98,
        "Hindi":68,
        "English":78,
    }
}
# print(Result)
# print(Result[sub["math"]])    # ✖ method

print(Result["sub"]["math"])