#SET in Python ...........
#set is a collection which is unordered,
#  unchangeable*, and unindexed. In Python sets are 
# written with curly brackets.{}


# collection={"apple","banana","cherry",20,65,88,54,"apple"}
# print(collection)
# print(type(collection))
# print(len(collection))
# print(collection(5))

#Empty Set........

# mela={}
# print(type(mela))   # its a Dictionary...


# mela=set()
# print(type(mela))  #its a Set...


# Method in Set.....

# add...
# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add("Ram")
# collection.add(12.8)
# print(collection)
# print(len(collection))
# collection.remove(12.8)
# print(collection)
# collection.add((1,2,3,4,5,6,7,8,))
# print(collection)
# print(len(collection))
# # collection.clear()
# print(collection)
# print(len(collection))
# group=set()

# group.add(1)
# group.add(5)
# group.add("Pk")
# group.add("3idots")
# group.add(152.2)
# group.add((5,4,5,8,7))
# print(group)
# print(group.pop())
# print(group.pop())
# print(group.pop())



# Union Methods in Sets........
#set.union(set2) # combination both set values & return new
#intersection Method in Sets......
#set.intersection(set2)  #combinations common values & returns new

# set1={1,2,3,4,5,6}
# set2={3,4,5,6,7,8}
# set3=set1.union(set2)
# set4=set1.intersection(set2)
# print(set3)
# print(set4)
# print(set3.union(set4))
# print(set3.intersection(set4))
