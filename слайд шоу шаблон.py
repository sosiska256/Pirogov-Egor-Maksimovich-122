form moviepy.editor import *
import os
directory =

clips_1 = ImageClip('').set_duration(2)
clips_2 = ImageClip('').set_duration(2)
final_clip = concatenate_videoclips([clips_1, clips_2], method='compose')
final_clip.write_videofile('test.mp4', fps=24)
