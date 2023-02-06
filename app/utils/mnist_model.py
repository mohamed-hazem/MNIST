import tensorflow as tf
import numpy as np
import os
# =============== #
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# =============== #
os.chdir(os.path.dirname(__file__))
model_path = r"../../model/mnist_model.h5"
model = tf.keras.models.load_model(model_path)
# =============== #
# img = [[255, 255, 255]*35]*35
# img = r"E:\Mo Hazem\Programing\Deep Learning Projects\01 - MNIST\Deployment\3.png"

def process_img(img, rows, cols):
    img = np.array(img).reshape(rows, cols, 3)
    img = tf.convert_to_tensor(img)
    img = tf.image.rgb_to_grayscale(img)
    img = tf.image.resize(img, size=(28, 28)) / 255.
    img = np.expand_dims(img, 0)

    return img

def predict_num(img, rows, cols):
    img = process_img(img, rows, cols)

    pred = model.predict(img, verbose=0)
    pred_num = np.argmax(pred)
    pred_con = np.max(pred)

    if (pred_con > 0.3):
        return pred_num, round(pred_con*100, 2)
    return None

# ================================================== #