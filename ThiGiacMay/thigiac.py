import cv2
import numpy as np
import ThiGiacMay.Chapter03 as c3
import ThiGiacMay.Chapter04 as c4
import ThiGiacMay.Chapter05 as c5
import ThiGiacMay.Chapter09 as c9
import streamlit as st

global imgin, imgout

def run():
    st.title("Machine Vision")

    # File operations
    st.write("GRAYSCALE image:")
    image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        # Read the image and display it
        imgin = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        st.image(imgin, caption="Uploaded Image")

    # Chapter 3 operations
    chapter3_menu = st.sidebar.selectbox("Chapter 3", ["Choose your option","Negative", "Logarit", "PiecewiseLinear", "Histogram", "HistEqual", "HistEqualColor", "LocalHist", "HistStat", "BoxFilter", "LowpassGauss", "Threshold", "MedianFilter", "Sharpen", "Gradient"])

    if chapter3_menu == "Negative":
        # Perform negative operation
        # Your code here
      imgout = c3.Negative(imgin)
      st.image(imgout, caption="Negative Image")

    elif chapter3_menu == "Logarit":
        # Perform logarit operation
        st.write("Performing Logarit operation...")
        # Your code here

    # Add the rest of the chapter 3 operations

    # Chapter 4 operations
    chapter4_menu = st.sidebar.selectbox("Chapter 4", ["Choose your option","Spectrum", "FrequencyFilter", "DrawNotchRejectFilter", "RemoveMoire"])

    if chapter4_menu == "Spectrum":
        # Perform spectrum operation
        st.write("Performing Spectrum operation...")
        # Your code here

    elif chapter4_menu == "FrequencyFilter":
        # Perform frequency filter operation
        st.write("Performing FrequencyFilter operation...")
        # Your code here

    # Add the rest of the chapter 4 operations

    # Chapter 5 operations
    chapter5_menu = st.sidebar.selectbox("Chapter 5", ["Choose your option","CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"])

    if chapter5_menu == "CreateMotionNoise":
        # Perform create motion noise operation
        st.write("Performing CreateMotionNoise operation...")
        # Your code here

    elif chapter5_menu == "DenoiseMotion":
        # Perform denoise motion operation
        st.write("Performing DenoiseMotion operation...")
        # Your code here

    # Add the rest of the chapter 5 operations

    # Chapter 9 operations
    chapter9_menu = st.sidebar.selectbox("Chapter 9", ["Choose your option","Erosion"])

    if chapter9_menu == "Erosion":
        # Perform erosion operation
        st.write("Performing Erosion operation...")
        # Your code here

    # Add the rest of the chapter 9 operations