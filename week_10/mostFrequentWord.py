d = {}
n=int(input("Number of input lines : "))
for i in range(n):
    line = input("Enter input data line :").split()
    for i in line:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
max_count = max(d.values())
most_frequent = [k for k, v in d.items() if v == max_count]
print("Most frequent word is :",min(most_frequent))