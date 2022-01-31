import cv2

capture = cv2.VideoCapture("VID_20171106_144131284.mp4")

while True:
    success, img = capture.read()
    cv2.imshow("Deer Video", img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
