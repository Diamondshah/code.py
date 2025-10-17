#......Recursion.....
#When a function calls itself repeatedly


#Q... fectorial calculate...   #...❌ aabhi samajhna hai
# def fact(n):
#     if (n==1 or n==0):
#         return 1
#     return fact(n-1)*n              

# n=int(input("Enter the Value of n:"))
# print(fact(n))

#Q...Write a recursive function to calculate the sum of first n natural numbers.
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n

# sum=calc_sum(10)
# print(sum)

#Q....Write a recursive function to print all element in a list.(hint:use list & index as parameters.)
def print_list(list,idx=0 ):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

frnd=["kaluaa","prince","Rohit","nitesh","akash","Niraj","avinash","Priyanshu","krishna","sunny"]
print_list(frnd,)