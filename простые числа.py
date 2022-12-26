sets=[]
for i in range(2,1000):
    flag=True
    for a in range(2,i):
        if i%a != 0:
            c=2
        else:
            flag=False
    if flag==True:
        sets.append(i)
print(sets)
