import cv2
import random
# Load an image using 'imread' specifying the path to image

img  = cv2.imread('./sam.jpg' , -1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# Display image using 'imshow' and 'waitKey' method of cv2
#print the first 100 rows of the image
print("original shape")
print(img.shape)
print("original")
# checl what is max height and width of the image
print("max height and width")
print(img.shape[0])
print(img.shape[1])
# check the color of the pixel at 100,100
# forloop to chage the first 100 rows of the image to random colors
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

copyPortion = img[0:100, 0:100]
img[ 500:600, 300:400] = copyPortion

print("new shape")
print(img)
cv2.imwrite('sam_copy.jpg', img)
cv2.imshow('sam_copy', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

