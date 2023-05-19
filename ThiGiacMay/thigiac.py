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
        imgout = c5.CreateMotionNoise(imgin)
        st.image(imgout, caption="CreateMotionNoise Image")

    elif chapter5_menu == "DenoiseMotion":
        imgout = c5.DenoiseMotion(imgin)
        st.image(imgout, caption="DenoiseMotion Image")
    
    elif chapter5_menu == "DenoisestMotion":
        temp = cv2.medianBlur(imgin, 7)
        imgout = c5.DenoiseMotion(temp)
        st.image(imgout, caption="DenoisestMotion Image")



    # Add the rest of the chapter 5 operations

    # Chapter 9 operations
    chapter9_menu = st.sidebar.selectbox("Chapter 9", ["Choose your option","Erosion","Dilation", "OpeningClosing", "Boundary", "HoleFilling", "HoleFillingMouse", "ConnectedComponent", "CountRice"])

    if chapter9_menu == "Erosion":
        imgout = c9.Erosion(imgin)
        st.image(imgout, caption="Erosion Image")

    elif chapter9_menu == "Dilation":
        imgout = c9.Dilation(imgin)
        st.image(imgout, caption="Dilation Image")
    
    elif chapter9_menu == "OpeningClosing":
        imgout = c9.OpeningClosing(imgin)
        st.image(imgout, caption="OpeningClosing Image")

    elif chapter9_menu == "Boundary":
        imgout = c9.Boundary(imgin)
        st.image(imgout, caption="Boundary Image")

    elif chapter9_menu == "HoleFilling":
        c9.HoleFilling(imgin)

    elif chapter9_menu == "ConnectedComponent":
        imgout = c9.ConnectedComponent(imgin)
        st.image(imgout, caption="ConnectedComponent Image")

    elif chapter9_menu == "CountRice":
        imgout = c9.CountRice(imgin)
        st.image(imgout, caption="CountRice Image")
    
    # Add the rest of the chapter 9 operations