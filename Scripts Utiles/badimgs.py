import cv2
import numpy as np
import os

# Función para simular una foto mal tomada con efectos aleatorios
def simular_foto_mal_tomada(imagen):
    # Lee la imagen de entrada
    img = cv2.imread(imagen)

    # Redimensiona la imagen 
    img = cv2.resize(img, (255, 255))

    # Genera grano aleatorio
    altura, ancho, _ = img.shape
    grano = np.random.normal(0, np.random.randint(5, 50), (altura, ancho, 3))
    img_con_grano = cv2.add(img, grano.astype(np.uint8))

    # Genera parámetros de distorsión aleatorios
    ksize = np.random.randint(1, 21)  # Tamaño del kernel Gaussiano (número impar)
    ksize = ksize + 1 if ksize % 2 == 0 else ksize  # Asegura que sea impar
    distorsion = cv2.GaussianBlur(img_con_grano, (ksize, ksize), 0)
    
    return distorsion

# Directorio de imágenes de entrada
directorio_entrada = 'DATASET/IMGS/'

# Directorio de imágenes de salida con efecto
directorio_salida = 'TEST/LR'

# Asegúrate de que el directorio de salida exista
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

# Procesa las primeras 100 imágenes
for i in range(1000):
    numero_imagen = f"{i:05d}.png"  # Formato de nombres de archivo: 00000.png, 00001.png, ...
    ruta_imagen_entrada = os.path.join(directorio_entrada, numero_imagen)
    ruta_imagen_salida = os.path.join(directorio_salida, numero_imagen)
    
    # Genera la imagen mal tomada con efectos aleatorios
    imagen_salida = simular_foto_mal_tomada(ruta_imagen_entrada)
    
    # Guarda la imagen de salida
    cv2.imwrite(ruta_imagen_salida, imagen_salida)

print("Se han generado y guardado las imágenes mal tomadas con efectos aleatorios en el directorio de salida:", directorio_salida)