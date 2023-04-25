a,b = list(map(int,input().split()))
mini = min(a,b)
maxi = max(a,b)
if(maxi==10 and mini==1):
    print("Yes")
elif(mini+1 == maxi):
    print("Yes")
else:
    print("No")