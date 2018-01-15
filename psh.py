# image downloder

import random
import urllib.request

def dwnlod_img(url):
    name= random.randrange(1,1000)
    filename= str(name)+".png"
    urllib.request.urlretrieve(url, filename)



dwnlod_img("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Alia_Bhatt_at_the_DVD_launch_of_%27Highway%27_%28cropped%29.jpg/170px-Alia_Bhatt_at_the_DVD_launch_of_%27Highway%27_%28cropped%29

"""
from PIL import Image
img = Image.open("65.jpg")
# print(img.size)
# print(img.format)


area = (100,100,300,375)
cropped_img = img.crop(area)
cropped_img.show()"""




