import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load the image or video
    image_path = "myBoard.jpg"
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original histogram
    hist, bins = np.histogram(gray.flatten(), 256, [0, 256])
    plt.figure()
    plt.title('Original Histogram')
    plt.bar(bins[:-1], hist, width=0.8, align='center')
    plt.show()

    b, g, r = cv2.split(image)

    # Histogram Equalization
    b = cv2.equalizeHist(b)
    g = cv2.equalizeHist(g)
    r = cv2.equalizeHist(r)
    equalized_image = cv2.merge((b, g, r))
    equal_gray = cv2.cvtColor(equalized_image, cv2.COLOR_BGR2GRAY)

    # Display the equalized histogram
    hist, bins = np.histogram(equal_gray.flatten(), 256, [0, 256])
    plt.figure()
    plt.title('Equalized Histogram')
    plt.bar(bins[:-1], hist, width=0.8, align='center')
    plt.show()

    # Display the original and equalized images side by side
    combined = np.hstack((image, equalized_image))
    cv2.imshow('Original vs. Equalized', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
