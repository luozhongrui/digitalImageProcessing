import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("----------------------------------")
        print(f"coordinate：({x}, {y})")
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow('Original Image', img)

if __name__ == '__main__':
    image_path = "myBoard.jpg"
    img = cv2.imread(image_path)

    # Define source points from the input image
    # Initially set to [0 0;100 0;100 100;0 100]
    # src_pts = np.array([[0, 0], [100, 0], [100, 100], [0, 100]], dtype='float32')

    # After inspecting the actual image,
    src_pts = np.array([[1347, 248], [1153, 698], [475, 423], [810, 77]], dtype='float32')

    # Define destination points for the projected output
    dst_pts = np.array([[0, 0], [500, 0], [500, 500], [0, 500]], dtype='float32')

    # Estimate the homography transformation
    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Apply the transformation
    warped_img = cv2.warpPerspective(img, M, (500, 500))

    # Display the rectified image
    cv2.imshow("Original Image", img)
    cv2.setMouseCallback('Original Image', click_event)
    cv2.imshow("Rectified Image", warped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


