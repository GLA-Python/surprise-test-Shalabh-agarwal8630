def exp(a):
    x=[ ]
    c=0
    for i in range(len(a)-1):
          x.append(abs(a[i+1]-a[i]))
    for i in range(len(x)-1):
        if x[i+1] > x[i]:
            c=1
        else:
            c=0
            break
    if c== 1:
        return True
    else:
        return False
g=list(map(int,input("enter").split()))
o=exp(g)
print(o)
