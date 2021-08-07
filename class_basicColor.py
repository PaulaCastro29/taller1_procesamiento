import cv2
import numpy as np

""" 
TALLER 1- Paula Castro Aguilar
Este archivo contiene la definición de la clase basicColor y sus respectivos métodos
"""
# Definición de la clase basicColor y sus respectivos métodos
class basicColor:

    # Constructor que recibe la ruta de una imagen la carga y almacena via OpenCv
    def __init__(self, path):
       self.image = cv2.imread(path)                            # Lee la imagen de la ruta definida
       cv2.imshow("Image", self.image)                          # Muestra la imagen
       cv2.waitKey(0)                                           # Mantiene la imagen abierta

    # Método que imprime las propiedades de la imagen
    def displayProperties(self):
       print('canales de la imagen:', self.image.ndim)          # Muestra el número de canales
       print('Número de pixeles de la imagen:', self.image.size)# Muestra el número de pixeles de la imagen

    # Método que transforma la imagen de entrada en el espacio de color HSV
    def colorize(self, a):
       image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  # Convierte la imagen en espacio HSV
       h, s, v = cv2.split(image_hsv)                           # Divide los componentes h, s, v
       h = a * np.ones_like(h)                                  # Cambia el valor de Hue
       image_hue = cv2.merge((h, s, v))                         # Comprime nuevamente la imagen HSV
       image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)# Convierte la imagen en BGR
       cv2.imshow('imageHSV',image_hue_bgr)
       cv2.waitKey(0)

    # Método que transforma la imagen de entrada en su version binaria con el método Otsu
    def makeBW(self):
       image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) # Convierte la imagen de entrada en binaria
       ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Método Otsu
       cv2.imshow('imageBW', Ibw_otsu)
       cv2.waitKey(0)

    # Método que transforma la imagen de entrada en su version binaria con el método Otsu
    def makeWB(self):
       image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) # Convierte la imagen de entrada en binaria invertida
       ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Método Otsu
       cv2.imshow('imageBW', Ibw_otsu)
       cv2.waitKey(0)

if __name__ == '__main__':
  color = basicColor()
  color.displayProperties()
  color.colorize()
  color.makeBW()
