import PySimpleGUI as sg

sg.theme('LightBlue2')  # Set the theme
s=['2','5','9','12','14','15','16','17','23','24','25','26','27b']
a=[
'''
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(y<=x) or (z<=w) or not(z))==False:
                    print(x,y,z,w)''',
'''
a=bin(79)[2:]
for i in range(2):
    a=a+str((a.count('1')%2))
print(a)''',
'''
tt=\'''66;39;77;31;132;117\'''
tt=t.split(';')
n=list(map(int,tt))
c=0
for i in range (6400):
    b=i*6
    f=n[b]
    s=n[b+1]
    trd=n[b+2]
    fo=n[b+3]
    fiv=n[b+4]
    six=n[b+5]
    Y=[f,s,trd,fo,fiv,six]
    d=0
    T=False
    diff=0
    sums=0
    for a in range(6): 
       d+=Y.count(Y[a]) 
       if d==8 and a==5:
         T=True
    for p in range(6):
      if Y.count(Y[p])==2:
         sums=2*Y[p]
      if Y.count(Y[p])==1:
         diff+=Y[p]
    diff==diff/4
    if sums>=(diff/4) and diff!=0 and sums!=0 and T:
      c+=1
print(c)''',
'''tt='8'*86
while ('1111'in(tt) or '8888'in(tt)):
    if '1111'in(tt):
        tt = tt.replace('1111','8',1)
    else:
         tt = tt.replace('8888','11',1)
    print(tt)
''',
'''
al='0123456789abcde'
for i in al:
    s=int(f'123{i}5',15) + int(f'1{i}233',15)
    if s%14==0:
        print(int(str(s//14),10))
''','''
for a in range(0,100):
    if all(((x%3==0) <= (x%5!=0)) or ((x+a)>=70) for x in range(1,10000)):
        print(a)
''',
'''it1=1
it2=1
for x1 in range(1,2024):
    it1=it1*x1
for x2 in range(1,2021):
    it2=it2*x2
print(it1/it2)
''',
'''
with open('17.txt')as f:
    a=[int(x)for x in f]
    g=[x for x in a if x%10==3]
    g=max(g)
    cs=[]
    for x,y in zip(a,a[1:]):
        if (((abs(x)%10==3) and (abs(y)%10!=3)) or ((abs(y)%10==3) and (abs(x)%10!=3))) and (x**2+y**2>=g**2):
            cs.append(x**2+y**2)
    print(len(cs),max(cs))
            
''',
'''
def f(x,y):
    if x>y or x==17:
         return 0
    elif x==y:
         return 1
    return(f(x+1,y))+f(x*2,y)
print(f(1,10)*f(10,35))
    
''','''
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('F','S').replace('D','S').replace('A','G').replace('O','G')
    s=s.replace("SG",'*')
    k=0
    kmax=0
    for i in s:
        if i=='*':
            k+=1
            kmax=max(k,kmax)
        else:
            k=0
    print(kmax)
''','''
for i in range(2023,10**10,2023):
    num=str(i)
    if (num[0]=='1') and (num[2:6]=='2139') and (num[-1]=='4'):
        print(i,i//2023)''',
'''
with open('26.txt') as f:
    s=[int(x) for x in f]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]
    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k,mini)
''',
'''with open('27-B.txt') as f:
    a=[int(x) for x in f]
    l=len(a)
    d=a+a
    allcost=[]
    res=0
    for i in range(l,(l//2)):
        cost=0
        v=d[i:i+l]
        for x in range(v):
            cost+=v[x]*x
        allcost.append(cost)
     mi=min(allcost)
            
'''

]

layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(90,50), key='outputt')],
          [sg.Button('Process Input', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('Someth', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button')]]

window = sg.Window('ЕГЭ архив', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'process':
        choice=a[s.index(values['Combo'])]
        window['outputt'].update(choice)
    if event == 'button':
        break

window.close()
