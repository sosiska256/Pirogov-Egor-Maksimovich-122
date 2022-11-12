import math

x=input('чё неизвестно? Если неизвестно что-то ещё то когда будут спрашивать значения пиши 0')
if x==('i'):
    I=int(input('I=?'))
    K=int(input('K=?'))
    N=int(input('N=?'))
    if I==0 or K==0:
        i=math.log2(N)
    i=I/K
    print(i)
if x==('I'):
    i=int(input('i=?'))
    K=int(input('K=?'))
    N=int(input('N=?'))
    if  i==0:
        i=math.log2(N)
    I=K*i
    print(I)
if x==('K'):
    i=int(input('i=?'))
    I=int(input('I=?'))
    N=int(input('N=?'))
    if i==0:
        i=math.iog2(N)
    K=I/i
    print(K)
if x==('N'):
    i=int(input('i=?'))
    I=int(input('I=?'))
    K=int(input('K=?'))
    if i==0:
        i=I/K
    N=2**i
    print(N)


    


