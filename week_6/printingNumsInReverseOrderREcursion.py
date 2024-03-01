"""3.	Given a sequence of integers that end with a 00. Print the sequence in reverse order. Don't use lists or other data structures.
Use the force of recursion instead"""
def rev():
    a=int(input("Enter a number : "))
    if(a!=0):
        rev()
    print(a,end=" ")
rev()