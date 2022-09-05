import streamlit as st
from PIL import Image,ImageFilter

st.header("Image Processing")
st.sidebar.subheader("options")
image=st.sidebar.file_uploader("upload an image", type=['jpg','png','gif'])

if image:
    st.image(image,use_column_width=True)
    filters=['grayscale','outline','embose']
    fil=st.sidebar.selectbox("select a filter",filters)

    if fil==filters[0]:
        im=Image.open(image)
        out=im.convert('L')
        st.image(out)

    


    