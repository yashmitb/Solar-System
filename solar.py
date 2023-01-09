import cv2

image1 = cv2.imread("Image_Manipulation/solar-system.jpg")


cv2.putText(image1, "Sun", (100, 160),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.7, color=(0, 0, 255))
cv2.putText(image1, "Mercury", (130, 260),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.3, color=(255, 255, 255))
cv2.putText(image1, "Venus", (200, 260),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.3, color=(255, 255, 255))
cv2.putText(image1, "Earth", (300, 260),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.3, color=(255, 255, 255))
cv2.putText(image1, "Mars", (390, 260),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.3, color=(255, 255, 255))
cv2.putText(image1, "Jupiter", (490, 90),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color=(255, 255, 255))
cv2.putText(image1, "Saturn", (690, 120),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color=(255, 255, 255))
cv2.putText(image1, "Uranus", (960, 120),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color=(255, 255, 255))
cv2.putText(image1, "Neptune", (1120, 120),
            fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color=(255, 255, 255))
cv2.imshow("solar", image1)
cv2.imwrite("labeled_solar_system.jpg", image1)

cv2.waitKey(0)
