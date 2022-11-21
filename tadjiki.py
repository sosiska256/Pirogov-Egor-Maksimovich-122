from moviepy.editor import *

clips_1 = ImageClip('foto-muzhchin-tadzhikov.jpg').set_duration(2)
clips_2 = ImageClip('12780315.jpg').set_duration(2)
final_clip = concatenate_videoclips([clips_1, clips_2], method='compose')
final_clip.write_videofile('tadjiki.mp4', fps=24)
