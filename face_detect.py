import cv2

# xml 분류기 파일 로그
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# gray스케일 이미지로 변환
img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 얼굴 위치에 대한 좌표 정보 가져오기
for (x, y, w, h) in faces:
    # 원본이미지에 얼굴 위치 표시
    # (x,y) 에서 시작, 끝점(x+가로), (y+세로), BGR색, 굵기 2
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()