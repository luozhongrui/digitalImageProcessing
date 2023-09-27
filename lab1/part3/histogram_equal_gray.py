import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)

    # Initialize the matplotlib window
    plt.ion()
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform histogram equalization
        equ = cv2.equalizeHist(gray)

        # Calculate Histogram
        hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])

        # Display original image and equalized image
        axs[0, 0].imshow(gray, cmap='gray')
        axs[0, 0].set_title('Original Image')
        axs[0, 0].axis('off')

        axs[0, 1].imshow(equ, cmap='gray')
        axs[0, 1].set_title('Equalized Image')
        axs[0, 1].axis('off')

        # Display histogram
        axs[1, 0].plot(hist_gray)
        axs[1, 0].set_title('Histogram - Original Image')
        axs[1, 0].set_xlim([0, 256])

        axs[1, 1].plot(hist_equ, color='r')
        axs[1, 1].set_title('Histogram - Equalized Image')
        axs[1, 1].set_xlim([0, 256])

        plt.draw()
        plt.pause(0.01)

        # Clear previous image for next frame
        for ax in axs.ravel():
            ax.clear()

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    plt.ioff()
    plt.close(fig)
