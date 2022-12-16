import math
def zxc():
    j=int(input('Что хотите увидеть?(код хэмминга-1, задачи по информатике-2, азбука морзе-3'))
    if j==1:
        {
          "nbformat": 4,
          "nbformat_minor": 0,
          "metadata": {
            "colab": {
              "provenance": [],
              "collapsed_sections": [],
              "include_colab_link": true
            },
            "kernelspec": {
              "name": "python3",
              "display_name": "Python 3"
            },
            "language_info": {
              "name": "python"
            }
          },
          "cells": [
            {
              "cell_type": "markdown",
              "metadata": {
                "id": "view-in-github",
                "colab_type": "text"
              },
              "source": [
                "<a href=\"https://colab.research.google.com/github/sosiska256/Pirogov-Egor-Maksimovich-122/blob/main/cod%20hemminga.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
              ]
            },
            {
              "cell_type": "markdown",
              "source": [
                "Программа перевода по коду Хэмминга"
              ],
              "metadata": {
                "id": "Dokk9uAXQ2aw"
              }
            },
            {
              "cell_type": "code",
              "source": [
                "a='0123456789'\n",
                "nums=list(a)\n",
                "print(nums)"
              ],
              "metadata": {
                "colab": {
                  "base_uri": "https://localhost:8080/"
                },
                "id": "QzGEJK5NQs9-",
                "outputId": "ffb68f95-fb40-4a80-9e8d-e5f94ec13086"
              },
              "execution_count": null,
              "outputs": [
                {
                  "output_type": "stream",
                  "name": "stdout",
                  "text": [
                    "['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']\n"
                  ]
                }
              ]
            },
            {
              "cell_type": "code",
              "source": [
                "b='0000000 000111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'\n",
                "hem=b.split()\n",
                "print(hem)\n",
                "for i in range(len(hem)):\n",
                "  hem[i]=int(hem[i])\n",
                "print(hem)"
              ],
              "metadata": {
                "id": "APnZUlTrSFBE",
                "colab": {
                  "base_uri": "https://localhost:8080/"
                },
                "outputId": "ddda06e7-f1bc-431b-ba9f-9e6937777615"
              },
              "execution_count": null,
              "outputs": [
                {
                  "output_type": "stream",
                  "name": "stdout",
                  "text": [
                    "['0000000', '000111', '0010110', '0011001', '0100101', '0101010', '0110011', '0111100', '1000011', '1001100']\n",
                    "[0, 111, 10110, 11001, 100101, 101010, 110011, 111100, 1000011, 1001100]\n"
                  ]
                }
              ]
            },
            {
              "cell_type": "code",
              "source": [
                "def distance(x,y):\n",
                "  k=7\n",
                "  for i in range(7):\n",
                "    if x%10==y%10:\n",
                "      k=k-1\n",
                "    x=x//10\n",
                "    y=y//10\n",
                "  return k"
              ],
              "metadata": {
                "id": "KPFZTMTJVQvQ"
              },
              "execution_count": null,
              "outputs": []
            },
            {
              "cell_type": "code",
              "source": [
                "cod=int(input(\"код=\"))"
              ],
              "metadata": {
                "colab": {
                  "base_uri": "https://localhost:8080/"
                },
                "id": "c77fF3oxWxp_",
                "outputId": "390900ec-3ab1-4d2f-dcd1-0f5595073257"
              },
              "execution_count": null,
              "outputs": [
                {
                  "name": "stdout",
                  "output_type": "stream",
                  "text": [
                    "код=1111111\n"
                  ]
                }
              ]
            },
            {
              "cell_type": "code",
              "source": [
                "min=distance(cod,hem[0])\n",
                "imin=0\n",
                "for i in range(10):\n",
                "  D=distance(cod,hem[i])\n",
                "  if D<min:\n",
                "    min=D\n",
                "    imin=i\n",
                "if min==0:\n",
                "  print(f\"Код верный: символ {nums[imin]}\")\n",
                "elif min==1:\n",
                "  print(f\"Код исправлен: символ {nums[imin]}\")\n",
                "else:print(f\"Код неверный\")\n"
              ],
              "metadata": {
                "colab": {
                  "base_uri": "https://localhost:8080/"
                },
                "id": "ULLrpyquXMnx",
                "outputId": "b3286d4f-3e03-4b9a-c1e3-113454b00704"
              },
              "execution_count": null,
              "outputs": [
                {
                  "output_type": "stream",
                  "name": "stdout",
                  "text": [
                    "Код неверный\n"
                  ]
                }
              ]
            }
          ]
        }
    elif j==2:
        x=input('кодирование чего? информации/звука/изображения')
        if x==('информации'):
            x=input('чё неизвестно? Если неизвестно что-то ещё то когда будут спрашивать значения пиши 0')
            if x==('i'):
                I=int(input('I=?'))
                x=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x==('биты'):
                    I=I
                if x==('байты'):
                    I=I*8
                if x==('гигабайты'):
                    I=I*8589934592
                if x==('килобайты'):
                    I=I*8192
                K=int(input('K=?'))
                N=int(input('N=?'))
                z=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if z==('биты'):
                    N=N
                if z==('байты'):
                    N=N*8
                if z==('гигабайты'):
                    N=N*8589934592
                if z==('килобайты'):
                    N=N*8192
                if I==0 or K==0:
                    i=math.log2(N)
                i=I//K
                print(i)
            if x==('I'):
                i=int(input('i=?'))
                r=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if r==('биты'):
                    i=i
                if r==('байты'):
                    i=i*8
                if r==('гигабайты'):
                    i=i*8589934592
                if r==('килобайты'):
                    i=i*8192
                K=int(input('K=?'))
                N=int(input('N=?'))
                y=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if y==('биты'):
                    N=N
                if y==('байты'):
                    N=N*8
                if y==('гигабайты'):
                    N=N*8589934592
                if y==('килобайты'):
                    N=N*8192
                if  i==0:
                    i=math.log2(N)
                I=K*i
                print(I)
            if x==('K'):
                i=int(input('i=?'))
                t=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if t==('биты'):
                    i=i
                if t==('байты'):
                    i=i*8
                if t==('гигабайты'):
                    i=i*8589934592
                if t==('килобайты'):
                    i=i*8192
                I=int(input('I=?'))
                b=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if b==('биты'):
                    I=I
                if b==('байты'):
                    I=I*8
                if b==('гигабайты'):
                    I=I*8589934592
                if b==('килобайты'):
                    I=I*8192
                N=int(input('N=?'))
                n=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if n==('биты'):
                    N=N
                if n==('байты'):
                    N=N*8
                if n==('гигабайты'):
                    N=N*8589934592
                if n==('килобайты'):
                    N=N*8192
                if i==0:
                    i=math.log2(N)
                K=I//i
                print(K)
            if x==('N'):
                i=int(input('i=?'))
                p=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if p==('биты'):
                    i=i
                if p==('байты'):
                    i=i*8
                if p==('гигабайты'):
                    i=i*8589934592
                if p==('килобайты'):
                    i=i*8192
                I=int(input('I=?'))
                o=input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if o==('биты'):
                    I=I
                if o==('байты'):
                    I=I*8
                if o==('гигабайты'):
                    I=I*8589934592
                if o==('килобайты'):
                    I=I*8192
                K=int(input('K=?'))
                if i==0:
                    i=I//K
                N=2**i
                print(N)
        elif x==('звука'):
            x=input('чё неизвестно? Если неизвестно 2 и более величины то когда их будут спрашивать пиши 0')
            if x==('H'):
                t = int(input('t=?'))
                y=input('секунды или минуты? Пиши слово с мелкой буквы')
                if y==('минуты'):
                    t=t*60
                N = int(input('N=?'))
                K = int(input('K=?'))
                b = int(input('b=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    b = b * 8
                if x == ('гигабайты'):
                    b = b * 8589934592
                if x == ('килобайты'):
                    b = b * 8192
                I = int(input('I=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    I = I * 8
                if x == ('гигабайты'):
                    I = I * 8589934592
                if x == ('килобайты'):
                    I = I * 8192
                if N==0:
                    H=I/(t*b)
                H=N/t
                print(H)
            elif x==('t'):
                N = int(input('N=?'))
                H = int(input('H=?'))
                x=input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
                if x==('гГц'):
                    H=H*100
                if x==('кГц'):
                    H=H*1000
                if x==('МГц'):
                    H=H*1000000
                K = int(input('K=?'))
                b = int(input('b=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    b = b * 8
                if x == ('гигабайты'):
                    b = b * 8589934592
                if x == ('килобайты'):
                    b = b * 8192
                I = int(input('I=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    I = I * 8
                if x == ('гигабайты'):
                    I = I * 8589934592
                if x == ('килобайты'):
                    I = I * 8192
                if N==0:
                    t=I/(H*b)
                t=N/H
                print(t)
            elif x==('N'):
                t = int(input('t=?'))
                z = input('секунды или минуты? Пиши слово с мелкой буквы')
                if z == ('минуты'):
                    t = t * 60
                H = int(input('H=?'))
                x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
                if x == ('гГц'):
                    H = H * 100
                if x == ('кГц'):
                    H = H * 1000
                if x == ('МГц'):
                    H = H * 1000000
                N=H*t
                print(N)
            elif x==('K'):
                t = int(input('t=?'))
                p = input('секунды или минуты? Пиши слово с мелкой буквы')
                if p == ('минуты'):
                    t = t * 60
                N = int(input('N=?'))
                H = int(input('H=?'))
                x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
                if x == ('гГц'):
                    H = H * 100
                if x == ('кГц'):
                    H = H * 1000
                if x == ('МГц'):
                    H = H * 1000000
                b = int(input('b=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    b = b * 8
                if x == ('гигабайты'):
                    b = b * 8589934592
                if x == ('килобайты'):
                    b = b * 8192
                I = int(input('I=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    I = I * 8
                if x == ('гигабайты'):
                    I = I * 8589934592
                if x == ('килобайты'):
                    I = I * 8192
                if b==0:
                    if t==0:
                        t=N/H
                    elif H==0:
                        H=N/t
                    b=I/(H*t)
                K=2**b
                print(K)
            elif x==('b'):
                t = int(input('t=?'))
                l = input('секунды или минуты? Пиши слово с мелкой буквы')
                if l == ('минуты'):
                    t = t * 60
                N = int(input('N=?'))
                H = int(input('H=?'))
                x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
                if x == ('гГц'):
                    H = H * 100
                if x == ('кГц'):
                    H = H * 1000
                if x == ('МГц'):
                    H = H * 1000000
                K = int(input('K=?'))
                I = int(input('I=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    I = I * 8
                if x == ('гигабайты'):
                    I = I * 8589934592
                if x == ('килобайты'):
                    I = I * 8192
                if K==0:
                    b=I/(H*t)
                    print(b)
                b=math.log2(K)
                print(b)
            elif x==('I'):
                t = int(input('t=?'))
                v = input('секунды или минуты? Пиши слово с мелкой буквы')
                if v == ('минуты'):
                    t = t * 60
                N = int(input('N=?'))
                H = int(input('H=?'))
                x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
                if x == ('гГц'):
                    H = H * 100
                if x == ('кГц'):
                    H = H * 1000
                if x == ('МГц'):
                    H = H * 1000000
                K = int(input('K=?'))
                b = int(input('b=?'))
                x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
                if x == ('байты'):
                    b = b * 8
                if x == ('гигабайты'):
                    b = b * 8589934592
                if x == ('килобайты'):
                    b = b * 8192
                if H==0:
                    H=N/t
                if t==0:
                    t=N/H
                if b==0:
                    b=math.log2(K)
                I=H*t*b
                print(I)
        elif x==('изображения'):
            x=input('что неизвестно?'):
                if x==('b'):
                    K=int(input('K=?')
                    b=log2(K)
                    print(b)
                if x==('K'):
                    b=int(input('b=?')
                    K=2**b
                    print(K)
    elif j==3:
        abc=['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','а','б','в','г','д','е','ж','з','и','й','к']
    ab=['._','-…','.--','--.','-..','.','…-','--..','..','.---','-.-','._','-…','.--','--.','-..','.','…-','--..','..','.---','-.-']
    word1=list(input())
    word2=[]
    for i in range(len(word1)):
        word2.append(ab[abc.index(word1[i])])
    B=''.join(word2)
    print(B)
    m=int(input('Хотите ещё раз запустить?(1-да 2-нет)'))
    if m==1:
        os.system('cls')
        return zxc()
zxc()
