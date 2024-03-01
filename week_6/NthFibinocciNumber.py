"""4.	Given a non-negative integer nn, print the nnth Fibonacci number. Do this by writing a function fib(n) which takes the non-negative
integer nn and returns the nnth Fibonacci number.Don't use loops, use the flair of recursion instead. However, you should think about why the
recursive method is much slower than using loops."""
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
         return fib(n-1)+fib(n-2)
n=int(input("Enter a number : "))
print("The",n,"th fibinocci number : ",fib(n))