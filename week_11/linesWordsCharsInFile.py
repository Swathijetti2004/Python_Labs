"""2.	Write a program to print the number of lines , words and characters in a file.
(Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10)"""
f=open("file1.txt","r")
No_lines=0
No_words=0
No_chars=0
for line in f:
    No_lines+=1
    No_words+=len(line.split())
    No_chars+=len(line.strip())
print("Number of lines : ",No_lines)
print("Number of words : ",No_words)
print("Number of chars : ",No_chars)
f.close()