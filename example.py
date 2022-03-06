from EZFinger import finger

from PIL import Image

myfinger = finger.Finger(Image.open("finger1.jpg"))
result = myfinger.compare(finger.Finger(Image.open("finger2.jpg")))
print(result.match)
print(result.ratio)