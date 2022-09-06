a=int(input())
b=int(input())
psf_a=0
for i in range (1,a):
    if a%i==0:
        psf_a+=i
psf_b=0
for i in range (1,b):
    if b%i==0:
        psf_b+=i
if psf_a==b and psf_b==a:
    print("Amicable")
else:
    print("Not Amicable")