"""5.	A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
 Given two integers A and B, print all prime numbers between them, inclusively."""
a=int(input("Enter starting number : "))
b=int(input("Enter ending number : "))
for i in range(a,b+1):
    count = 0
    for j in  range(1,i):
        if(i%j==0):
            count+=1
    if(count==1):
        print(i,end="  ")