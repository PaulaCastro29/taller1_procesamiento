from class_basicColor import basicColor
"""
TALLER 1- Paula Castro Aguilar
Archivo principal
"""
    # El usuario ingresa la ruta donde esta la imagen que quiere visualizar
path = input("Ingrese la ruta de la imagen: ")

    #Se ejecutan los métodos de la clase basicColor
color = basicColor(path)
color.displayProperties()
color.makeWB()

    #El usuario ingresa el valor de Hue
a=int(input("Ingrese el valor de Hue entre 0 y 179: "))
color.colorize(a)

