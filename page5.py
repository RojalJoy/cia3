import streamlit as st
import numpy as np
import cv2
from PIL import Image

def main():
    st.title("Image Manipulation with OpenCV")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert PIL image to numpy array for OpenCV operations
        img_np = np.array(image)

        st.header("Image Operations")

        if st.button("Grayscale"):
            grayscale_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            st.image(grayscale_img, caption="Grayscale Image", use_column_width=True)

        if st.button("Blur"):
            blur_img = cv2.GaussianBlur(img_np, (15, 15), 0)
            st.image(blur_img, caption="Blurred Image", use_column_width=True)

        if st.button("Edge Detection"):
            gray_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            edge_img = cv2.Canny(gray_img, 100, 200)
            st.image(edge_img, caption="Edge Detection", use_column_width=True)

if __name__ == "__main__":
    main()
