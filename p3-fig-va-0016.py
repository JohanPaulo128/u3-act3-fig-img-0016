import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
# Johan Aros NC 0016
print("Johan Aros NC 0016")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA") 
Mi_imagen = cv2.imread('cantinflas.jpg')
plt.imshow(Mi_imagen)
plt.title('cantinflas y Johan Paulo NC 0016')
plt.show()
print("+-+-+ Puntos en la imagen +-+-+")
plt.imshow(Mi_imagen)
x = [100, 100, 300,300]
y = [100, 400, 500,300]
plt.scatter(x,y,s=20, c='red')
plt.show()