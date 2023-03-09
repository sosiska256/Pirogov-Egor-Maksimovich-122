for x in range(0,15):
    a=[1,2,3,x,5]
    int(''.join(map(str,a)))
    b=[1,x,2,3,3]
    int(''.join(map(str,a)))
    a=int('', 15)
    b=int('', 15)
    if (a+b)%14==0:
        print(x)
