from PIL import Image

sample=Image.open("3fd84abbd1bc42b3b1534d52e1338bf3.jpeg")
sample.save('3fd84abbd1bc42b3b1534d52e1338bf3.jpeg')
sample.show()
cord = (10, 10, 640, 340) # лево, верх, право, низ
new_picture = picture.crop(cord)
new_picture.show()

