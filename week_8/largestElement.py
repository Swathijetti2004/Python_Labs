"""4.	Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the
index number. If the highest element is not unique, print the index of the first instance."""
print("Enter elements of the list : ",end=" ")
a=[int(i) for i in input().split()]
print("Largest element of the list : ",end=" ")
m=a[0]
index=0
for i in range(0,len(a)):
    if(a[i]>m):
        m=a[i]
        index=i
print(m,index)