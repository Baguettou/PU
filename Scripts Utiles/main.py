import tensorflow as tf
from tensorflow import keras

data_dir = r"DATASET\BADIMGS"
image_count = len(list(data_dir.glob('*/*.png')))
print(image_count)
