for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='0'+num[2:]+'10'

    if num.count('1')%2!=0:
        chislo='1'+num[2:]+'11'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break
