"""1.	Write a program to print each line of a file in reverse order.
(Line 1
Line 2
Line 3+
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10)"""
f=open("file1.txt","r")
l=[]
for line in f:
    l.append(line[::-1])
print("Each line of a file in reverse order : \n",end=" ")
a=[]
for i in l:
    a.append(i)
for i in a:
    print(i)
f.close()
