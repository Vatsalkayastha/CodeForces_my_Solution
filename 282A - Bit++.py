x = 0
for i in range(int(input())):
    s=input()
    if(s=="X++" or s=="++X"):
        x = x + 1 
    elif(s=="X--" or s=="--X"):
        x = x - 1
    else:
        continue
print(x)
