from PIL import Image, ImageChops

Img1 = Image.open("1.jpg")
Img2 = Image.open("2.jpg")

diff = ImageChops.difference(Img1, Img2)
if diff.getbbox():
	diff.show()
