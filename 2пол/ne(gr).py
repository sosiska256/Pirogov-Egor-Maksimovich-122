a='nepu'
alp=['н', 'е', 'п', 'а']
n=['*  *','*  *','****','*  *','*  *']
e=['****','*   ','****','*   ','****']
p=['****','*   ','*   ','*   ','*   ']
u=['*** ','*  *','*** ','*   ','*   ']
mat=[n, e, p, u]
alp=list('nepu')
ch=[alp.index(z) for z in list(a)]
for i in range(len(mat[0])):
    for g in range(len(ch)):
        print(mat[ch[g]][i],end=' ')
    print()
