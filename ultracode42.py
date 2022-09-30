N10=int(input('N10='))
Np=0
k=1
p=int(input('p='))
Np=Np+(N10%p)*k
k=k*10
N10=N10//p
print(Np)
