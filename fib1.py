import time
n=int(input("Enter number of iterations: "))
b=time.time()
a=0
b=1
print(a,"\t",b,end="\t")
if(n<=1):
    print("\t",n)
else:
    for i in range (n-2):
        c=a+b
        print(c,end="\t")
        a=b
        b=c
e=time.time()
print("\ntime required is",e-b)