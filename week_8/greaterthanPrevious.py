"""2.	Given a list of numbers, find and print all the elements that are greater than the previous element."""
print("Enter elements of the list : ",end=" ")
l=[int(i) for i in input().split()]
print("Elements that are greater than the previous element :",end=" ")
for i in range(1,len(l)):
    """if(l[i]<l[i+1]):
        print(l[i+1],end=" ")"""
    if(l[i]>l[i-1]):
        print(l[i],end=" ")