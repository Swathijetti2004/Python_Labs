"""3.	Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank"""
print("Enter elements of the list : ",end=" ")
a=[int(i) for i in input().split()]
print("The first adjacent elements which have the same sign :",end=" ")
for i in range(1,len(a)):
    if((a[i]<0 and a[i-1]<0) or (a[i]>0 and a[i-1]>0)):
        print(a[i-1],a[i])
        break