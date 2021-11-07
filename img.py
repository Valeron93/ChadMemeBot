import textwrap
from PIL import Image, ImageDraw, ImageFont
import time

def maker(average_fan_txt, average_enj_txt):

    font = ImageFont.truetype("arial.ttf", 20)

    img = Image.open('meme.jpg', mode = 'r') 

    draw = ImageDraw.Draw(im = img)

    text1 = textwrap.fill(text = average_fan_txt, width = 50)
    text2 = textwrap.fill(text = average_enj_txt, width = 50)

    draw.text(xy = (20, 20), text = text1, font = font, fill = '#000000')
    draw.text(xy = (350, 20), text = text2, font = font, fill = '#000000')
    
    #img.show()

    img_name = f'{time.time()}.jpg'
    img.save(img_name)
    
    return img_name

