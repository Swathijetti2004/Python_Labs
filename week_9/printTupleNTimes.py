'''1.	Take two inputs from the user one is to create a tuple and another one is an integer n. Write a program to print the tuple n times.
Create another tuple with the user given elements and concatenate both the tuples and print the result as shown in the example
'''
tup=input("Enter tuple1 elements seperated with spaces : ")
tup1=tuple(tup.split())
n=int(input("How many times to print tuple : "))
print((tup1*n))
val=input("Enter tuple2 elements seperated with spaces : ")
tup2=tuple(val.split())
print("Concatinating tuple 1 & 2 : ",tup1+tup2)