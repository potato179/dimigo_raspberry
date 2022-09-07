import cv2

img = cv2.imread("haengsin.jpg")
img = cv2.resize(img, (600, 400))

cv2.imshow("haengsin", img)

edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow("edge1", edge1)
cv2.imshow("edge2", edge2)
cv2.imshow("edge3", edge3)

cv2.waitKey()

cv2.destroyAllWindows()