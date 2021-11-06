import moviepy.editor as mp
import time

def a(text1: str, text2: str) -> str:
    video = mp.VideoFileClip('meme.mp4', audio=True)

    w,h = moviesize = video.size
    name = f'{time.time()}.mp4'

    my_text = mp.TextClip(text1, font="Amiri-regular", color='white', fontsize=34)
    txt_col = my_text.on_color(size=(video.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)
    final = mp.CompositeVideoClip([video,txt_col])

    final.subclip(0,video.duration).write_videofile(name)
    return name
