with open("file1.txt","r") as f1:
    a=[]
    for i in f1:
        a.append(i[::-1])
    b=a[::-1]
    for i in b:
        print(i)