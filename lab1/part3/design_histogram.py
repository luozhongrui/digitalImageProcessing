import cv2
import numpy as np


def compute_histogram(image):
    histogram = [0] * 256
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram


def histogram_equalization(image):
    histogram = compute_histogram(image)
    cdf = np.cumsum(histogram)
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    image_equalized = cdf[image]
    return image_equalized


if __name__ == "__main__":
    img = cv2.imread('myBoard.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equal = histogram_equalization(image=gray)
    cv2.imshow('Original', gray)
    cv2.imshow('Equalized', equal)
    cv2.waitKey(0)