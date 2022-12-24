a=2
i=0
nums=[4,5,5,6,7,3567]
flag=False
flag=True
while True:
    for c in range(2):
        for b in range(2):
            if ((c<=b) or not(a))==False:
                print(f'{c}бара бара бара ',end='бере бере бере ')
            elif a%14==0:
                a=1
                print(a)
            elif a//14==0:
                a=2
                print(a)
            else: a=3
    break
num=[1,1,2,4,5,5,6,7,34,56]                               
num.append(40)           
print(num.count('1'),num,num.sort(reverse=True),max(num),min(num),sum(num))
f=int(input('Введите число: '))
print('Ваше число но в 2ичной системе счисления: ',(bin(2)[2:]))
with open('1.txt') as l:
    s=l.readline()
with open('2.txt') as l:
    s=l.readline()
    print(s)
with open('1.txt') as f:
   n=f.readlines()
   print(n)
with open('2.txt') as f:
   n=f.readlines()
   print(n)
with open('1.txt') as f:
    d=[int(x) for x in f]
    print(d)
with open('2.txt') as f:
    d=[int(x) for x in f]
    print(d)
if ((abs(num[i])%10==3) and (abs(num[i+1])%10!=3)) or\
         ((abs(num[i])%10!=3) and (abs(nums[i+1])%10==3))==False:
    print('Obunga')


