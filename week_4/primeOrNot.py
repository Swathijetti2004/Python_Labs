"""4.	A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
 Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise"""
n=int(input("Enter a number : "))
ans=0
for i in range(1,n):
    if(n%i==0):
        ans+=1
if(ans==1):
    print("PRIME")
else:
    print("COMPOSITE")