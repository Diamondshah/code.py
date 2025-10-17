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
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

sum=calc_sum(10)
print(sum)