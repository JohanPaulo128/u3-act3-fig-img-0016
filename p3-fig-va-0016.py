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

print("Cuadro azul en la imagen")
img_cantinflas=cv2.imread('cantinflas.jpg')
plt.imshow(img_cantinflas)
x=[120,250,250,140,140]
y=[60,60,220,220,60]
plt.plot(x,y,c='blue')
plt.show()

print("+-+-+Circul verde en la imagen+-+-+-+")
I = cv2.imread('cantinflas.jpg')
plt.imshow(I)
N = 80
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc)=(200,120)
r = 80
for i in range(N+1):
  t   = 2*np.pi / N*i
  x[i]= xc + r*np.cos(t)
  y[i]= yc + r*np.sin(t)
plt.plot(x,y,c='green')
plt.show()

