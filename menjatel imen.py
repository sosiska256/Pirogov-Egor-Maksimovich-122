import random
def zxc():
    a=input('Введи имя: ')
    pol=int(input('Вы мужчина?(1-да,2-нет): '))
    if pol==1:
        b=list(a)
        c=b[2:]
        var=b[3:]
        var2=''.join(var)
        d=''.join(c)
        v=random.choice(['нер','ор'])
        z=random.choice(['нер','ор','кс'])
        print(f'Мар{d}{v}')
        print(f'Мар{var2}{z}. Какой молодец, а может теперь займешься чем-то полезным?')
    elif pol==2:
        b=list(a)
        c=b[2:]
        var=b[3:]
        var2=''.join(var)
        d=''.join(c)
        v=random.choice(['лина','на','ка'])
        z=random.choice(['лина','на','ка'])
        print(f'Мар{d}{v}')
        print(f'Мар{var2}{z}. Какая умница, а может теперь займешься чем-то полезным?')
    x=int(input('Хотите увидеть кто работал над генератором имён?(1-да,2-нет): '))
    if x==1:
        print(f'Лидер команды-Пирогов Егор\n Моральная поддержка-Пирогов Егор\n Подбиратель имён-Пирогов Егор\n И просто самый лучший и скромный человек на земле-Пирогов Егор(если всё ещё не поняли, то это я)')
    return zxc()
zxc()
