import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from model import model_predict
import tensorflow_hub as hub
from tensorflow.keras.models import load_model

model = load_model(('catvsdog.h5'),custom_objects={'KerasLayer':hub.KerasLayer})



#=================================== Title ===============================
st.title("""Cat Vs Recognizer""")

#========================== File Uploader ===================================
img_file_buffer = st.file_uploader("Upload an image here 👇🏻")

try:
	image = Image.open(img_file_buffer)
	st.write("""Preview Of Given Image!""")
	if image is not None:
	    st.image(image,width=224,height=224)
	

except:
	st.write("""
		### ❗ Any Picture hasn't selected yet!!!
		""")

#================================= Predict Button ============================


if st.button("Predict"):

	save_img("temp_dir/test_image.png", image)
	image_path = "temp_dir/test_image.png"

	pred = model_predict(image_path,model)
	st.success(pred)
