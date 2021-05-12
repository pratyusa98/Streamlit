import streamlit as st


# Text/Title
st.title('Streamlit Tutorials')

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")


## Working with Colorful Text and Error Messages

st.success("Successful")
st.info("Info")
st.warning("This is a warning")
st.error("This is an error Danger")
st.exception("NameError('name three not defined')")


## Getting Help Info About Python
st.help(range)


## Using the Write Function For More

# Writing Text/Super Fxn
st.write("Text with write")

st.write(range(10))

## Working with media files eg images,audio,video

st.title('Image_Process')
from PIL import Image
img = Image.open("example.png")
st.image(img,width=400,caption="Simple Image")

# Videos
# vid_file = open("example.mp4","rb").read()
# # vid_bytes = vid_file.read()
# st.video(vid_file)

# Audio
# audio_file = open("examplemusic.mp3","rb").read()
# st.audio(audio_file,format='audio/mp3')