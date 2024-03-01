#5.	Given two integers, print "YES" if exactly one of them is odd and print "NO" otherwise.
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
    print("YES")
else:
    print("NO")
