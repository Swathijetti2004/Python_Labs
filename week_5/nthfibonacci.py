"""3.	The Fibonacci sequence is defined as follows: ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
Given a non-negative integer nn, print the nnth Fibonacci number ϕnϕn.
This problem can also be solved with a for loop."""
n=int(input("Enter the number : "))
"""a=0
b=1
c=a+b
count=1
if(n==0):
    print(0)
elif(n==1):
    print(1)
else:
    while(count!=n):
        c=a+b
        a=b
        b=c
        count+=1
    print("Nth fibinocci number : ",c)
"""
if n == 0:
    print(0)
else:
    a=0
    b=1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)