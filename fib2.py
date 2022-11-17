"""name=Gauri Ramesh Gunawant
roll n0=4150
practical no=1
"""
import time
num=int(input("enter number of recurssions : "))
b=time.time()
def fib(n):
   if (n<=1):
       return n
   else:
       return(fib(n-1) + fib(n-2))
if num <= 0:
   print("Plese enter a positive integer")
else:
   for i in range(num):
       print(fib(i),end="\t")
e=time.time()
print("\ntime required is :",e-b)