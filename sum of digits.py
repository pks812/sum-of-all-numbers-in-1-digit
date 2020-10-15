a=input()
l=len(a)
b=str(a)
e=0
while e<l-1:
    d=''
    for i in range(len(a)-1):
        c=int(a[i])+int(a[i+1])
        c=str(c)
        if len(c)!=1:
            for i in range(len(str(c))-1):
                c=int(c[i])+int(c[i+1])
        d=d+str(c)
    e=e+1
    a=d
print(d)
