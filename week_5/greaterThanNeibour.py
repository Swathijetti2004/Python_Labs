"""2.	A sequence consists of integer numbers and ends with the number 0. Determine how many elements
of this sequence are greater than their neighbours above"""
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
count=0
while(b!=0):
    if(a>b):
        count+=1
    a=b
    b = int(input("Enter a number :"))
print("No of elements that are greater than previous : ",count)