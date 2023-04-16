from keras.models import load_model
import tensorflow as tf
import requests

loaded_model = load_model("vgg16_epochs_10.h5")

classes = [
    'CELOSIA_ARGENTEA_L',
    'CROWFOOT_GRASS',
    'PURPLE_CHLORIS'
]

def load_and_prep_image(filename, img_shape = 224):
    img = tf.io.read_file(filename) #read image
    img = tf.image.decode_image(img) # decode the image to a tensor
    img = tf.image.resize(img, size = [img_shape, img_shape]) # resize the image
    img = img/255. # rescale the image
    return img

# predict function
def predict(filename):

    # Import the target image and preprocess it
    img = load_and_prep_image(filename)
    
    # Make a prediction
    pred = loaded_model.predict(tf.expand_dims(img, axis=0))

    # Get the predicted class
    pred_class = classes[pred.argmax()]

    return pred_class


if __name__ == '__main__' : 
    filepath = 'raw_dataset/CROWFOOT_GRASS/crowfoot_grass_150.jpeg'
    result = predict(filepath)
    
    print('result : ', result)