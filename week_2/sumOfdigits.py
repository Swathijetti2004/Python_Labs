a=int(input("Enter number : "))
s=(a%10)+((a//10)%10)+(a//100)
"""while(a):
    r=a%10
    s+=r
    a=a//10,"""
print("Sum of digits of",a,"is : ",s)