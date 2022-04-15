# afbeelding van stad bij dag converteren
# naar afbeelding van stad bij nacht

import numpy as np
from imageio import imread, imwrite
import cv2

img = imread('stad.jpg')
arr = img * np.array([0.1, 0.2, 0.5])
arr2 = (255 * arr/arr.max()).astype(np.uint8)
imwrite('stad_bij_nacht.png', arr2)
img2 = cv2.imread('stad_bij_nacht.png')
gamma = 2
gamma_img = np.array(255 * (img2/255) ** gamma, dtype='uint8')
cv2.imwrite('stad_bij_nacht_final.png', gamma_img)
print("Conversie is Klaar!")