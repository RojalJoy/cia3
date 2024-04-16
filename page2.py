import streamlit as st
import numpy as np
import cv2
from PIL import Image

def main():
    st.title("Image Processing")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        img_np = np.array(image)

        st.header("Image Operations")

        if st.button("Grayscale"):
            grayscale_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            st.image(grayscale_img, caption="Grayscale Image", use_column_width=True)

        if st.button("Resize"):            
            img_resize=image.resize((200,200),Image.HAMMING)
            st.image(img_resize, caption="Resized Image", use_column_width=True)

        if st.button("Cropping"):
            top_left_x = 0
            top_left_y = 0
            width = 100
            height = 100
            Image_Cropped=img_np[top_left_y:top_left_y+height,top_left_x:top_left_x+width]
            st.image(Image_Cropped, caption="Cropped Image", use_column_width=True)
        
        if st.button("Image Rotation"):
            rotated_image=image.rotate(45)
            st.image(rotated_image, caption="Rotated Image", use_column_width=True)

if __name__ == "__main__":
    main()

