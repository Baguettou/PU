import zipfile
import os

# Directorio donde están ubicados los archivos ZIP
zip_directory = 'DATASET'

# Directorio donde deseas extraer todas las imágenes
output_directory = 'IMGS'

# Iterar a través de los archivos ZIP
for zip_file_name in os.listdir(zip_directory):
    if zip_file_name.endswith('.zip'):
        zip_file_path = os.path.join(zip_directory, zip_file_name)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_directory)
