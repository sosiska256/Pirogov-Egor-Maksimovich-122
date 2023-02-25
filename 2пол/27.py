with open('27-A.txt') as b:
    a=[int(x) for x in b]
    a.pop(0)
    l=len(a)
    cost=0
    for x in range(l):
        d=a[x:(x+l)]
        for N in range(len(d)):
            ind=0
            if len(d)//2<=N:
                ind=len(d)-N
                cost+=ind*d[N]
            else:
                cost+=N*d[N]
    print(cost)
