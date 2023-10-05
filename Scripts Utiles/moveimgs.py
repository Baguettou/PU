import os
import shutil

# Ruta del directorio de origen
directorio_origen = 'DATASET\IMGS'

# Ruta del directorio de destino
directorio_destino = 'TEST\HR'

# Crear el directorio de destino si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Contador para llevar un seguimiento de las imágenes copiadas
contador = 0

# Recorrer las imágenes en el directorio de origen
for filename in os.listdir(directorio_origen):
    if filename.endswith('.png'):
        # Construir el camino completo de la imagen de origen
        origen = os.path.join(directorio_origen, filename)
        
        # Construir el camino completo de la imagen de destino
        destino = os.path.join(directorio_destino, filename)
        
        # Copiar la imagen de origen a la carpeta de destino
        shutil.copy(origen, destino)
        
        # Incrementar el contador
        contador += 1
        
        # Si se han copiado 1000 imágenes, salir del bucle
        if contador == 1000:
            break

print(f'Se han copiado {contador} imágenes al directorio de destino.')
