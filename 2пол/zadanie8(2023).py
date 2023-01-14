g=int(0)
for a in range(1,8):
    for b in range(1,8):
        for c in range(1,8):
            for d in range(1,8):
                for e in range(1,8):
                    f=str(a)+str(b)+str(c)+str(d)+str(e)
                    if f.index('6')!=0 and f.index('6')!=4 and f.count('6')==1 and f[f.index('6')+1]%2==0 and f[f.index('6')-1]%2==0:
                        g+=1
                    elif f.index('6')==0 and f.count('6')==1 and f[f.index('6')+1]%2==0:
                        g+=1
                    elif f.index('6')!=4 and f.count('6')==1 and f[f.index('6')-1]%2==0:
                        g+=1
print(g)
