"""3.	Given a string consisting of exactly two words separated by a space. Print a new string with the first and
second word positions swapped (the second word is printed first). This task should not use loops and if."""
s = input("Enter a string : ")
space = s.find(' ')
print("After swapping the string is : ",end=" ")
print(s[space:] + " " + s[:space])