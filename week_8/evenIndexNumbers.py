"""1.	Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...)."""
print("Enter elements of the list : ",end=" ")
l=[int(i) for i in input().split()]
print("Elements with an even index number :",end=" ")
for i in l[::2]:
    print(i,end=" ")