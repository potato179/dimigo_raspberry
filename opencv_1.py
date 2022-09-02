import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라 연결 안 됨!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()