"""4.	Create a tuple with the user given inputs. Take an index n from the user. Write a program to print the tuple element at index n,
print the result as shown in the examples. If the given index range is not in the tuple print the error message """
values=input("Enter values separated by space : ")
tup1=tuple(values.split())
print("Given tuple : ",tup1)
print("Type of tuple : ",type(tup1))
value=int(input("Enter value for index : "))
print("Value at index",value,"is :",tup1[value])