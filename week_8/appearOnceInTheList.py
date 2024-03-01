"""6.	Given a list of numbers, find and print the elements that appear in the list only once. The elements must be printed in the order in
which they occur in the original list."""
print("Enter elements of the list : ",end=" ")
a=[int(i) for i in input().split()]
print("The elements that appear in the list only once : ",end=" ")
for i in a:
    if(a.count(i)==1):
        print(i,end=' ')