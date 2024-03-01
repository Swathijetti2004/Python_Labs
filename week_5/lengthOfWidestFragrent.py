"""4.	Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment
 where all the elements are equal to each other."""
x = int(input("Enter a number : "))
prev = x
count = 1
mcount = count
while x != 0:
  x = int(input("Enter a number : "))
  if x == prev:
    count += 1
    prev = x
  else:
    if count > mcount:
      mcount = count
    count = 1
    prev = x
print("The maximum number of consecutive equal numbers : ",mcount)
