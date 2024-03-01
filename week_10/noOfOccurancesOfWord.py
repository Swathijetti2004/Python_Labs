"""1.	The text is given in a single line. For each word of the text count the number of its occurrences before it. A word is a sequence of
non-whitespace characters. Two consecutive words are separated by one or more spaces. Punctiation marks are a part of a word, by this definition."""
data=input("Enter data : ").split()
d={}
for i in data:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("The number of occurrences of the given words :")
for i in d:
    print(d[i],end=" ")