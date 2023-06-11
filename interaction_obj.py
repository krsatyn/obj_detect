#from neural_network import HESH_COMPARATOR
#from setting import *
#from apps_construct import *
import matplotlib.pyplot as plt
import cv2

# def a():
#     suspect_image = SUSPECT_SOURCE + get_suspect_name()
#     warning_image = 'Image_Source/Suspect/pole.jpg'

#     print('____________________________-' + suspect_image)

#     ACCURACY_NETWORK = HESH_COMPARATOR
#     probability_class = ACCURACY_NETWORK(suspect_image, warning_image)

#     probability = probability_class.main_nan()

#     print(probability)
#     return 0

image = 'Image_Source/input_image/input_backage.jpg'
# image = 'Image_Source/Suspect/pistol.jpg'
image = cv2.imread(image)


#серое 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#размытое
image = cv2.GaussianBlur(image, (11,11), 0)

image = cv2.Canny(image, 30, 150, 3)

image = cv2.dilate(image, (1,1), iterations=0)

(cnt, hierarchy) = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2RGB)
image = cv2.drawContours(image, cnt, -1, (0,255, 0), 2)
print(f"count countor {len(cnt)}")

cv2.imshow("image", image)
cv2.waitKey(0)