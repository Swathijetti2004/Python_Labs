"""3.	Create a tuple with the user given elements. Write a program to remove an element from the input tuple, print the result as shown in
the example. If the element is not present in the tuple print the error message """
values=input("Enter values separated by space : ")
tup1=tuple(values.split())
print("Given tuple : ",tup1)
print("Type of tuple : ",type(tup1))
x=list(tup1)
value=input("Enter value to remove : ")
x.remove(value)
tup1 = tuple(x)
print("After inserting the tuple : ", tup1)
print("Type of tuple : ",type(tup1))
a=tup1.count(3)
print(tup1[:a]+tup1[a+1::])