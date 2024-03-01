#2.	10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
sum=0
for i in range(10):
    a = int(input("Enter a number : "))
    sum+=a
print("Sum is : ",sum)