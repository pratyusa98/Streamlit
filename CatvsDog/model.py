import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img


def model_predict(image_path,model):
    image = load_img(image_path,target_size=(224,224))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    
    result = model.predict(image)

    if result[0]<=0.5:
        result = "The image classified is cat"
        return result
    else:
        result = "The image classified is dog"
        return result
