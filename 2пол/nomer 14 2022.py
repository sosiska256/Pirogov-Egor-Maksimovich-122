a=3*16**2018-2*8**1028-3*4**1100-2**1050-2022
b=[]
while a!=0:
    b.append((str(a%4)))
    a=a//4
c=''.join(b)
print(c.count('3'))
