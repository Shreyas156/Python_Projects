import urllib.request
import cv2
import numpy as np

url = "http://192.168.43.211:8080/shot.jpg"

while True:

    img = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)

    image = cv2.imdecode(img, -1)

    cv2.imshow('IPWebcam', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
