## author: Tashnim Chowdhury
## Code to download an image from internet, save it, and open the image.


import urllib2
from urllib2 import Request

url  = "http://p.imgci.com/db/PICTURES/CMS/202600/202607.1.jpg"


## Saving the image file
img = urllib2.urlopen(url)
localFile = open('desktop2.jpg', 'wb')
localFile.write(img.read())
localFile.close()

## Showing the image
from PIL import Image
img2 = Image.open('desktop.jpg')
img2.show()
