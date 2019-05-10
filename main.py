import numpy
import numpy as np
import cv2
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir = "D:\Downlaods\cgip\photos")

img = cv2.imread(file_path)

hsi = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
cie = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)

pil_img = Image.open(file_path).convert('CMYK')

opencvImage = cv2.cvtColor(numpy.array(pil_img), cv2.COLOR_RGB2BGR)


# Display Original Image
cv2.imshow('Original', img)

# Display HSI Image
cv2.imshow('HSI', hsi)

# Display CIE Lab Image
cv2.imshow('CIE_Lab', cie)

# Display CMYK Image
cv2.imshow('CMYK', opencvImage)


# Wait for a key press and then terminate the program
cv2.waitKey(0)
cv2.destroyAllWindows()

