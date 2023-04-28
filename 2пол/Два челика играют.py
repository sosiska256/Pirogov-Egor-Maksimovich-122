s=[]
for i in range(501,600):
    r=list(map(int,str(i)))

    maxim=max(r)
    minim=min(r)
    sred=sum(r)-minim-maxim
    
    ma=int(str(maxim)+str(sred))
    if minim==0:
        mi=int(str(sred)+str(minim))    
    else:    
        mi=int(str(minim)+str(sred))
    
    ras=ma-mi
    if ras==10:
        s.append(i)
print(sum(s))
