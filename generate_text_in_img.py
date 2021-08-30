import random   
import string  
import secrets # import package  
from PIL import Image, ImageDraw, ImageFont
import os


def generator_text_img(path, size=(512,512)):
    img = Image.new('RGB', size, color = (255, 255, 255))
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    d = ImageDraw.Draw(img)
    for line in range(32):
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(50))
        d.text((10+line, 15*(line+1)), str(res), font=fnt, fill=(0, 0, 0))
    img.save(path)


num_of_img = 1000
folder_path = 'fake_text_image/raw/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for imgs in range(num_of_img):
    path = os.path.join(folder_path, 'img_' + str(imgs) + '.png')
    generator_text_img(path)

