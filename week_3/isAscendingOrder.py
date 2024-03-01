#6.	Given three different integers, print YES if they're given in ascending order, print NO otherwise.
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if(a<b and b<c):
    print("YES")
else:
    print("NO")