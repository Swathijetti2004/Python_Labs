n=int(input("Enter number of countries : "))
d={}
for i in range(n):
    a=input("Enter country name along with its cities : ").split()
    for city in a[1:]:
        d[city]=a[0]
a=int(input("Enter number of cities do you want to check :"))
for s in range(a):
    city=input("Enter city name : ")
    print(d[city])