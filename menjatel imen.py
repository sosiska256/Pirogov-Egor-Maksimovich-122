import random, os
def zxc():
    x=int(input('Нужна ли справка об авторе?(1-да,2-нет): '))
    if x==1:
        print(f' Всё сделал-Пирогов Егор')
        a=input('Введи имя: ')
        pol=int(input('Вы мужчина?(1-да,2-нет): '))
        if pol==1:
            b=list(a)
            c=b[2:]
            var=b[3:]
            var2=''.join(var)
            d=''.join(c)
            v=random.choice(['Мар','Муд','Зиг'])
            z=random.choice(['нер','ор','кс'])
            k=random.choice(['Мар','Муд','Зиг'])
            l=random.choice(['дер','ор','кс'])
            print(f'Ваше имя: {v}{d}{z}.Альтернативный вариант: {k}{var2}{l}')
        elif pol==2:
            b=list(a)
            c=b[2:]
            var=b[3:]
            var2=''.join(var)
            d=''.join(c)
            v=random.choice(['Мар','Муд','Зиг'])
            z=random.choice(['лина','на','ла'])
            k=random.choice(['Мар','Муд','Зиг'])
            l=random.choice(['лина','на','ла'])
            print(f'Ваше имя: {v}{d}{z}.Альтернативный вариант: {k}{var2}{l}')
        m=int(input('Хотите ещё раз запустить?(1-да 2-нет)'))
        if m==1:
            os.system('cls')
            return zxc()
zxc()
    elif x==2:
        a=input('Введи имя: ')
        pol=int(input('Вы мужчина?(1-да,2-нет): '))
        if pol==1:
            b=list(a)
            c=b[2:]
            var=b[3:]
            var2=''.join(var)
            d=''.join(c)
            v=random.choice(['Мар','Муд','Зиг'])
            z=random.choice(['нер','ор','кс'])
            k=random.choice(['Мар','Муд','Зиг'])
            l=random.choice(['дер','ор','кс'])
            print(f'Ваше имя: {v}{d}{z}.Альтернативный вариант: {k}{var2}{l}')
        elif pol==2:
            b=list(a)
            c=b[2:]
            var=b[3:]
            var2=''.join(var)
            d=''.join(c)
            v=random.choice(['Мар','Муд','Зиг'])
            z=random.choice(['лина','на','ла'])
            k=random.choice(['Мар','Муд','Зиг'])
            l=random.choice(['лина','на','ла'])
            print(f'Ваше имя: {v}{d}{z}.Альтернативный вариант: {k}{var2}{l}')
        m=int(input('Хотите ещё раз запустить?(1-да 2-нет)'))
        if m==1:
            os.system('cls')
            return zxc()
zxc()
