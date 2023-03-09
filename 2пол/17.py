with open('17.txt')as f:
    a=[int(x)for x in f]
    b=[x for x in a if x%10==3]
    b=max(b)
    c=[]
    for x,y in zip(a,a[1:]):
        if (((abs(x)%10==3) and (abs(y)%10!=3)) or ((abs(y)%10==3) and (abs(x)%10!=3))) and (x**2+y**2>=b**2):
            c.append(x**2+y**2)
    print(len(c),max(c))
