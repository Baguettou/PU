import shutil
import os

# Directorio donde están ubicadas las carpetas con imágenes extraídas
input_directory = 'DATASET\FOLDERS'

# Directorio donde deseas tener todas las imágenes combinadas
output_directory = 'DATASET\IMGS'

# Iterar a través de las carpetas
for folder_name in os.listdir(input_directory):
    folder_path = os.path.join(input_directory, folder_name)
    if os.path.isdir(folder_path):
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            if os.path.isfile(image_path):
                shutil.move(image_path, output_directory)
        os.rmdir(folder_path)