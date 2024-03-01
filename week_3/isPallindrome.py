"""7.	A palindrome is a number which reads the same when read forward as it it does when read backward.
Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise"""
a=input("Enter number : ")
b=a[::-1]
if a==b:
    print("YES")
else:
    print("NO")