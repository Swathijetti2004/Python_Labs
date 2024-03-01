"""1.	Write a function capitalize(lower_case_word) that takes the lower case word and returns the word with the first letter capitalized.
Eg., print(capitalize('word')) should print the word Word. Then, given a line of lowercase ASCII words (text separated by a single space),
print it with the first letter of each word capitalized using the your own function capitalize(). In Python there is a function ord(character),
which returns character code in the ASCII chart, and the function chr(code), which returns the character itself from the ASCII code. For example,
ord('a') == 97, chr(97) == 'a'."""
def cap(a):
    s=a.split(" ")
    n=[]
    for i in range(len(s)):
        b=s[i]
        c=b[0].upper()+b[1::]
        n.append(c)
    return (" ".join(n))
"""def cap(s):
    return s.title()"""
text=input("Enter the string : ")
print("After capitalizing the output is : ",cap(text))