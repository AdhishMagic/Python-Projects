import cv2

imgcapture = cv2.VideoCapture(0)
result = True

while result:
    ret, frame = imgcapture.read()
    cv2.imwrite("src/test.jpg", frame)
    result = False
    print("Image captured and saved as test.jpg")

imgcapture.release()
