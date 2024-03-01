n=int(input("Enter number of words :"))
d={}
for i in range(n):
    y,z=input("Enter two synonyms : ").split()
    d[y]=z
    d[z]=y
x=input("Enter word for synonym : ")
print("The synonym of",x,"is :",d[x])