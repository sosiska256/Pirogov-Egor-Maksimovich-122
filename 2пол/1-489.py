from itertools import product
f=product('12',repeat=5)
for i in f:
    i=list(i)
    a=12
    for j in range(5):
        if i[j]=='1':
            a-=1
        elif i[j]=='2':
            a*=7
    if a==489:
        print(i)
        break