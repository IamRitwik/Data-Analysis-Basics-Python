import numpy
import cv2

with open("array.txt", "r") as file:
    img_array = file.read()

a = numpy.array(
[[[255, 0, 0],
  [255, 255, 255],
  [255, 255, 255],
  [187, 41, 160]],

 [[255, 255, 255],
  [255, 255, 255],
  [255,  255,  255],
  [255, 255, 255]],

 [[255, 255, 255],
  [0, 0, 0],
  [47, 255, 173],
  [255, 255, 255]]]
)

cv2.imwrite("image2.png", a)