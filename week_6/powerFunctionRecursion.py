"""2.	Given a positive real number aa and a non-negative integer nn. Calculate anan without using loops, ** operator or the built in function
math.pow(). Instead, use recursion and the relation an=a⋅an−1an=a⋅an−1. Print the result. Form the function power(a, n)."""
def power(a,n):
    if(n==0):
        return 1
    return a*power(a,n-1)
a=int(input("Enter a base number : "))
n=int(input("Enter a power number : "))
print("Answer (",a,"^",n,") : ",power(a,n))