"""2.	Write a program to add an element to a tuple based on the user-given value in a specific index, print the result as shown in the
example. If the index is not in the range print the error message"""
values=input("Enter values separated by space : ")
tup1=tuple(values.split())
print("Given tuple : ",tup1)
print("Type of tuple : ",type(tup1))
x=list(tup1)
value=input("Enter value to insert : ")
ind=int(input("Enter an index to where the elment to be inserted : "))
if(ind>=(len(x))):
    print("Indexerror : index out of range")
else:
    x.insert(ind,value)
    tup2=tuple(x)
    print("After inserting the tuple : ", tup2)
