"""4.	Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h,
as well as all the characters between them. Given a string in which the letter h occurs at least two times, reverse the sequence of characters
enclosed between the first and last appearances."""
s=input("Enter a string : ")
a=s.find('h')
b=s.rfind('h')
print("After removing the string fragrent :",s[:a]+s[b+1:])