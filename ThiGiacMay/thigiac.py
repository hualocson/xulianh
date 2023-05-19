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
    image_file = st.file_uploader("Choose an GRAY image file", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        # Read the image and display it
        imgin = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        st.image(imgin, caption="GRAY Image")

    # Chapter 3 operations
    chapter3_menu = st.sidebar.selectbox("Chapter 3", ["Choose your option","Negative", "Logarit", "PiecewiseLinear", "Histogram", "HistEqual", "HistEqualColor", "LocalHist", "HistStat", "BoxFilter", "LowpassGauss", "Threshold", "MedianFilter", "Sharpen", "Gradient"])

    if chapter3_menu == "Negative":
      
      imgout = c3.Negative(imgin)
      st.image(imgout, caption="Negative Image")

    elif chapter3_menu == "Logarit":
        imgout = c3.Logarit(imgin)
        st.image(imgout, caption="Logarit Image")
    elif chapter3_menu == "PiecewiseLinear":
        imgout = c3.PiecewiseLinear(imgin)
        st.image(imgout, caption="PiecewiseLinear Image")
    elif chapter3_menu == "Histogram":
        imgout = c3.Histogram(imgin)
        st.image(imgout, caption="Histogram Image")
    elif chapter3_menu == "HistEqual":
        imgout = c3.HistEqual(imgin)
        st.image(imgout, caption="HistEqual Image")
    elif chapter3_menu == "HistEqualColor":
        imgout = c3.HistEqualColor(imgin)
        st.image(imgout, caption="HistEqualColor Image")
    elif chapter3_menu == "LocalHist":
        imgout = c3.LocalHist(imgin)
        st.image(imgout, caption="LocalHist Image")
    elif chapter3_menu == "HistStat":
        imgout = c3.HistStat(imgin)
        st.image(imgout, caption="HistStat Image")
    elif chapter3_menu == "BoxFilter":
        imgout = c3.BoxFilter(imgin)
        st.image(imgout, caption="BoxFilter Image")
    elif chapter3_menu == "LowpassGauss":
        imgout = cv2.GaussianBlur(imgin,(43,43),7.0)
        st.image(imgout, caption="LowpassGauss Image")
    elif chapter3_menu == "Threshold":
        imgout = c3.Threshold(imgin)
        st.image(imgout, caption="Threshold Image")
    elif chapter3_menu == "MedianFilter":
        imgout = c3.MedianFilter(imgin)
        st.image(imgout, caption="MedianFilter Image")
    elif chapter3_menu == "Sharpen":
        imgout = c3.Sharpen(imgin)
        st.image(imgout, caption="Sharpen Image")
    elif chapter3_menu == "Gradient":
        imgout = c3.Gradient(imgin)
        st.image(imgout, caption="Gradient Image")

    # Chapter 4 operations
    chapter4_menu = st.sidebar.selectbox("Chapter 4", ["Choose your option","Spectrum", "FrequencyFilter", "DrawNotchRejectFilter", "RemoveMoire"])

    if chapter4_menu == "Spectrum":
        # Perform spectrum operation
        imgout = c4.Spectrum(imgin)
        st.image(imgout, caption="Spectrum Image")
        # Your code here
    elif chapter4_menu == "FrequencyFilter":
        # Perform frequency filter operation
        imgout = c4.FrequencyFilter(imgin)
        st.image(imgout, caption="FrequencyFilter Image")
    elif chapter4_menu == "DrawNotchRejectFilter":
        imgout = c4.DrawNotchRejectFilter()
        st.image(imgout, caption="DrawNotchRejectFilter Image")
    elif chapter4_menu == "RemoveMoire":
        imgout = c4.RemoveMoire(imgin)
        st.image(imgout, caption="RemoveMoire Image")

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