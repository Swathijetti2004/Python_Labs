"""3.	Write a Python program to copy one file to another file.
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10"""
f=open("file1.txt","r")
new_file=open("newFile.txt","w")
for line in f:
    new_file.write(line)
f.close()
new_file.close()