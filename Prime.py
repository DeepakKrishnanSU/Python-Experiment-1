n=int(input())
count=0
i=1
while i<=n/2:
    if n%i==0:
        count=count+1
    i=i+1
if count==1:
    print("Prime")
else:
    print("Not Prime")