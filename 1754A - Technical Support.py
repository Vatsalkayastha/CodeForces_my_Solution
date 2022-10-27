for i in range(int(input())):
    n = int(input())
    s = str(input())
    c = 0
    for i in range(n):
        if(s[i]=="Q"):
            c += 1 
        elif(s[i]=="A"):
            c -= 1 
        if(c<0):
            c = 0
    if(c==0):
        print("Yes")
    else:
        print("No")
