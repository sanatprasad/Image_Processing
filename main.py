from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from contrast import ImageContraster

# Read the image
img = Image.open("car.jpg")

# Convert the image to grayscale
gray_img = img.convert("L")

# Convert the grayscale image to a NumPy array
gray_arr = np.array(gray_img)

# Create an instance of the ImageContraster class
icter = ImageContraster()

# HE
he_eq_img = icter.enhance_contrast(img, method="HE")
he_hist = icter.calc_histogram_(np.array(he_eq_img.convert("L")))
plt.figure()
plt.subplot(121)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(he_eq_img)
plt.title("HE Equalized Image")
plt.figure()
plt.bar(range(len(he_hist)), he_hist)
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.title("Histogram - HE")
plt.show()

# AHE
ahe_eq_img = icter.enhance_contrast(img, method="AHE", window_size=32, affect_size=16)
ahe_hist = icter.calc_histogram_(np.array(ahe_eq_img.convert("L")))
plt.figure()
plt.subplot(121)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(ahe_eq_img)
plt.title("AHE Equalized Image")
plt.figure()
plt.bar(range(len(ahe_hist)), ahe_hist)
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.title("Histogram - AHE")
plt.show()

# CLAHE
clahe_eq_img = icter.enhance_contrast(img, method="CLAHE", blocks=8, threshold=10.0)
clahe_hist = icter.calc_histogram_(np.array(clahe_eq_img.convert("L")))
plt.figure()
plt.subplot(121)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(clahe_eq_img)
plt.title("CLAHE Equalized Image")
plt.figure()
plt.bar(range(len(clahe_hist)), clahe_hist)
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.title("Histogram - CLAHE")
plt.show()

# Local Region Stretch
lrs_eq_img = icter.enhance_contrast(img, method="Bright")
lrs_hist = icter.calc_histogram_(np.array(lrs_eq_img.convert("L")))
plt.figure()
plt.subplot(121)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(lrs_eq_img)
plt.title("LRS Equalized Image")
plt.figure()
plt.bar(range(len(lrs_hist)), lrs_hist)
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.title("Histogram - LRS")
plt.show()
