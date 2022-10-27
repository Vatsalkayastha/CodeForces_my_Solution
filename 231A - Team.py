ans = 0
for i in range(int(input())):
    a,b,c = map(int,input().split())
    if((a==0 and b==1 and c==1) or (a==1 and b==0 and c==1) or (a==1 and b==1 and c==0) or (a==1 and b==1 and c==1) ):
        ans += 1 
print(ans)
