from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
coordinates_com = (25, 0, image.width-25, image.height)

ex_middle = red.crop(coordinates_com)
coordinates = (50, 0, image.width, image.height)
ex_left = red.crop(coordinates)
ex_shifted_red = Image.blend(ex_left, ex_middle, 0.3)

ex_middle = blue.crop(coordinates_com)
coordinates = (0, 0, image.width-50, image.height)
ex_right = blue.crop(coordinates)
ex_shifted_blue = Image.blend(ex_right, ex_middle, 0.3)

ex_middle = green.crop(coordinates_com)
new_image = Image.merge("RGB", (ex_shifted_red, ex_middle, ex_shifted_blue))
new_image.save("new_picture.jpg")
new_image.thumbnail((80, 80))
new_image.save("user_pic.jpg")