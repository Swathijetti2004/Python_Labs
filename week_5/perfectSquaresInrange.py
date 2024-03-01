"""1.	For a given integer N, print all the squares of integer numbers where the square is less than or equal to
N, in ascending order."""
n=int(input("Enter the range : "))
i=1
while(i<n):
    ans=i**2
    if(ans<n):
        print(ans,end=" ")
    i+=1