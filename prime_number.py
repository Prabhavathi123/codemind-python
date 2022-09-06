A=int(input())
i=1
count=0
while i<=A:
    if A%i==0 and A%1==0:
        count+=1
    i=i+1
if count==2:
    print("prime")
else:
    print("not a prime")
    