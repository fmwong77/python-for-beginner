import cv2
image = cv2.imread("files/smallgray.png", 0)
print(image)
# cv2.imwrite("files/new_smallgray.png", image)

# print row
for i in image:
  print(i)

# print column
for i in image.T:
  print(i)

for i in image.flat:
  print(i)

print(image[0:2,2:4])

