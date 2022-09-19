import cv2

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret,frame = cap.read()
    if not ret:
        break
    img2 = cv2.resize(frame,(640, 360))

    gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(img2,100,150)

    cv2.imshow('frame',img2)
    cv2.imshow('frame1', gray)
    cv2.imshow('frame2', edge)


    if cv2.waitKey(10)==27:
        break

cap.release()
cv2.destroyAllWindows()