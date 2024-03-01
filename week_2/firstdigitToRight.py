#4.	Given a positive real number, print its first digit to the right of the decimal point.
a=float(input("Enter a number : "))
print("First digit to the right of the decimal part : ",int((a*10)%10))