import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load the image or video
    image_path = "myBoard.jpg"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:  # If the image loading failed, try video
        cap = cv2.VideoCapture(image_path)
        ret, image = cap.read()
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original histogram
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    plt.figure()
    plt.title('Original Histogram')
    plt.bar(bins[:-1], hist, width=0.8, align='center')
    plt.show()

    # Histogram Equalization
    equalized_image = cv2.equalizeHist(image)

    # Display the equalized histogram
    hist, bins = np.histogram(equalized_image.flatten(), 256, [0,256])
    plt.figure()
    plt.title('Equalized Histogram')
    plt.bar(bins[:-1], hist, width=0.8, align='center')
    plt.show()

    # Display the original and equalized images side by side
    combined = np.hstack((image, equalized_image))
    cv2.imshow("Original vs Equalized", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
