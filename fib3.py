a=0
b=1
c=1
num=0
def fib(n):
    global a,b,c,num
    if(n<=0 and n<1):
        print("enter positive integer")
    elif(n>=0 and n<1):
        print(a,"\t",b,end="\t")
    else:
        
        c=a+b
        print(c,end="\t")
        a=b
        b=c
        num+=1
        while(num<n-2):
            fib(n)
n=int(input("enter number of recurssions: "))
if(n>0 and n<=1):
    print(n)
else:
    print(a,"\t",b,end="\t")
    fib(n)

