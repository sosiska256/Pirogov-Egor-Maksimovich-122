def zxc():
    a=['Вы поддерживаете КПСС?(1-да,2-нет)','2+2=?','если любое число умножить на 0, то получится?','Небо голубое?(1-да,2-нет)','Владимир Путин молодец?(1-да,2-нет)']
    b=int(0)
    for i in range(len(a)):
        if i==0:
            c=int(input(f'{a[i]}\n'))
            if c==1:
                b=b+1
        elif i==1:
            c = int(input(f'{a[i]}\n'))
            if c==4:
                b=b+1
        elif i==2:
            c = int(input(f'{a[i]}\n'))
            if c==0:
                b=b+1
        elif i==3:
            c = int(input(f'{a[i]}\n'))
            if c==1:
                b=b+1
        elif i==4:
            c = int(input(f'{a[i]}\n'))
            if c==1:
                b=b+1
    print(b)
    n = int(input('Хотите сыграть?(1-да,2-нет)'))
    if n == 1:
        return zxc()
zxc()
