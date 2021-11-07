import moviepy.editor as mp
import time

def movie(text1: str, text2: str) -> str:
    video = mp.VideoFileClip('data/meme.mp4', audio=True)

    w,h = moviesize = video.size
    name = f'{time.time()}.mp4'

    boxsize = (340, 100)

    label1 = mp.TextClip(text1, size=boxsize, method='caption', font='Amiri-regular').set_position((10,10))
    label2 = mp.TextClip(text2, size=boxsize, method='caption', font='Amiri-regular').set_position((370,10))

    final = mp.CompositeVideoClip([video,label1, label2])

    final.subclip(0,video.duration).write_videofile(name)
    return name
