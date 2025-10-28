import seaborn as sns 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print(tf.__version__)

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
sns.countplot(x = y_train)
plt.show

## Check to make sure that there are NO values that are not a number 
print("Any NaN Training: ", np.isnan(x_train).any())
print("Any NaN Testing: ", np.isnan(x_test).any())

input_shape = (28, 28, 1) ## 28x28 p0x, 1 color channel (gray scale)
## Reshape the training and testing data
x_train = x_train.reshape(x_train.shape[0]), x_train.shape[1], x_train.shape[2], 1
x_train = x_train/255 ## Normalize the data to between 0 and 1

x_test= x_test.reshape(x_test.shape[0]), x_test.shape[1], x_test.shape[2], 1
x_test = x_test/255 ## Normalize the data to between 0 and 1