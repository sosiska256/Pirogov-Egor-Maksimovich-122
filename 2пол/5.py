for i in range(1,100):
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        a='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        a='11'+num[2:]+'1'
    if int(a,2)>40:
        print (i, int(a,2))
        break
