import math
def zxc():
    j=int(input('Что хотите увидеть?(код хэмминга-1, перевод из любой сист счисления в десятичную-2, азбука морзе-3, перевод и десятичной системы счисления в любую-4'))
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
    elif j==4:
        p=int(input())
        Np=int(input())
        k=int(1)
        N10=int(0)
        while p!=0:
            N10=N10+(Np%10)*k
            k=k*p
            Np=Np//10
            p=p-1
        print('N10=',N10)
    elif j==2:
        N10 = int(input('введите число '))
        p = int(input("введите сс "))
        Np = 0
        k = 1
        while N10 != 0:
            Np = Np + (N10 % p) * k
            k = k * 10
            N10 = N10 // p
        print(Np)
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
