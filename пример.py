from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import random
from random import randint
import os
def f(z):
    s=randint(400,60)
    x=randint(50,600)
    y=randint(50,50)
    colors=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    J=random.choice(colors)
    V=random.choice(colors)
    R=random.choice(colors)
    G=random.choice(colors)
    im = Image.new('RGB',(500,500), color=(f'#FAACAC'))
    draw_text= ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", s)
    draw_text.text((x,y), f'{str(int(z))}',font=font, fill=(f'#{G}{V}06{J}6'))
    im.save(f'C:/Users/student/OneDrive/gog/niga/{z}.png')

t=["v","l","a","d","i","m","i","r","p","u","t","i","n","m","o","l","o","d","e","z","!"]
for i in t:
    f(i)
directory = 'C:/Users/student/OneDrive/gog/niga'
files = os.listdir(directory)
imges = list(filter(lambda x: x.endswith('.png'), files))
clips = [ImageClip(m).set_duration(2) for m in imges]
final_clip= concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('videotest.mp4',fps=24)



abc=['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','а','б','в','г','д','е','ж','з','и','й','к']
ab=['._','-…','.--','--.','-..','.','…-','--..','..','.---','-.-','._','-…','.--','--.','-..','.','…-','--..','..','.---','-.-']
word1=list(input())
word2=[]
for i in range(len(word1)):
    word2.append(ab[abc.index(word1[i])])
B=''.join(word2)
print(B)
