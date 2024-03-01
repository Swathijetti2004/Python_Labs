#3.	For the given integer n calculate the value n!. Don't use math module in this exercise.
n=int(input("Enter a number : "))
ans=1
for i in range(1,n+1):
    ans*=i
print("Factorial of ",n,"is : ",ans)