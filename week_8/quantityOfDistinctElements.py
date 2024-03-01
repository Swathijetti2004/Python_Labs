"""5.	Given a list of numbers with all of its elements sorted in ascending order, determine and print the quantity of distinct elements in it."""
print("Enter elements of the list : ",end=" ")
a=[int(i) for i in input().split()]
ans=1
for i in range(1,len(a)):
    if(a[i]>a[i-1]):
        ans+=1
print("The quantity of distinct elements : ",ans)