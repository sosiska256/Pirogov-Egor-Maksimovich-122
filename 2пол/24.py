with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('F','S').replace('D','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    kmax=0
    k=0
    for i in s:
        if i == '*':
            k+=1
            kmax=max(k,kmax)
        else:
            k=0
    print(kmax)
