import tensorflow as tf
import numpy as np
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from tensorflow.python import pywrap_tensorflow
model_dir=r'train1_3_1/model'
checkpoint_path = os.path.join(model_dir, "-1")

reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)

var_to_shape_map = reader.get_variable_to_shape_map()

for key in var_to_shape_map:
    print("tensor_name: ", key,reader.get_tensor(key).shape)