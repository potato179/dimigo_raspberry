from pydoc import classname
import cv2
import numpy as np

model = "./dnn/bvlc_googlement.caffemodel"
config = "./dnn/deploy.prototxt"
classFile = "./dnn/classification_classes_ILSVRC2012.txt"

classNames = None
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

net = cv2.dnn.readNet(model, config)
img = cv2.imread("gay.jpg")

blob = cv2.dnn.blobFromImage(img, scalefactor = 1, size = (224, 224), mean = (104, 117, 123))

net.setInput(blob)
detections = net.foward()

out = detections.flatten()
classId = np.argmax(out)
confidence = out[classId]

text = "%s (%4.2f%%)" % (classNames[classId], confidence * 100)
cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()