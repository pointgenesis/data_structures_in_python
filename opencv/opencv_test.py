import cv2

print(f'OpenCV Version: {cv2.__version__}')

img = cv2.imread("travis_dream_office.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Office", img)
cv2.imshow("Office - gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()