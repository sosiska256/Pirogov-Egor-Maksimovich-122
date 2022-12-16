def zxc():
    j = int(input('Что хотите увидеть?(код хэмминга-1, перевод из любой сист счисления в десятичную-2, азбука морзе-3, перевод и десятичной системы счисления в любую-4'))
    if j == 1:
        a = '0123456789'
        nums = list(a)
        print(nums)

        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        b = '0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
        hem = b.split()
        print(hem)
        for i in range(len(hem)):
            hem[i] = int(hem[i])
        print(hem)

        cod = int(input("код="))

        min = distance(cod, hem[0])
        imin = 0
        for i in range(10):
            D = distance(cod, hem[i])
            if D:
                min = D
                imin = i
        if min == 0:
            print(f"Код верный: символ {nums[imin]}")
        elif min == 1:
            print(f"Код исправлен: символ {nums[imin]}")
        else:
            print(f"Код неверный")
    elif j == 4:
        p = int(input('Введите число: '))
        Np = int(input('Введите систему счисления: '))
        k = int(1)
        N10 = int(0)
        while p != 0:
            N10 = N10 + (Np % 10) * k
            k = k * p
            Np = Np // 10
            p = p - 1
        print('Ответ: ', N10)
    elif j == 2:
        N10 = int(input('введите число '))
        p = int(input("введите систему счисления "))
        Np = 0
        k = 1
        while N10 != 0:
            Np = Np + (N10 % p) * k
            k = k * 10
            N10 = N10 // p
        print(Np)
    elif j == 3:
            abc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й','к']
        ab = ['._', '-…', '.--', '--.', '-..', '.', '…-', '--..', '..', '.---', '-.-', '._', '-…', '.--', '--.', '-..','.', '…-', '--..', '..', '.---', '-.-']
        word1 = list(input())
        word2 = []
        for i in range(len(word1)):
            word2.append(ab[abc.index(word1[i])])
        B = ''.join(word2)
        print(B)
        m = int(input('Хотите ещё раз запустить?(1-да 2-нет)'))
        if m == 1:
            return zxc()
    zxc()
