import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras

train_vec=pd.read_csv('train_vec.txt')
print(train_vec[0][:10])