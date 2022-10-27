for i in range(int(input())):
    s = str(input())
    n = len(s)
    ans = n-2
    if(n>10):
        print(s[0]+str(ans)+s[-1])
    else:
        print(s)
