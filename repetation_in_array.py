arr=[]
a=int(input("enter number of elements "))
for k in range(a):
    c=int(input("element="))
    arr.append(c)

arr1=[]
for i in arr:
    count=0
    for j in arr:
        if(i==j):
         count+=1
    if(count>1 and (i not in arr1)):
        print(i,"repeted",count,"times")
    if(count>1):
        arr1.append(i)
