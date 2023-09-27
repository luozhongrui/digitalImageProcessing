import cv2
import numpy as np

# List to store the clicked points
points = []


def click_event(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        print("----------------------------------")
        print(f"coordinate：({x}, {y})")
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(img, f"({x}, {y})", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Original Image', img)

        points.append([x, y])

        # Check if we have 4 points
        if len(points) == 4:
            perform_projection(points)


def perform_projection(pts):
    # Convert list to numpy array
    src_pts = np.array(pts, dtype='float32')

    # Compute bounding box of the selected points
    min_x, min_y = np.min(src_pts, axis=0)
    max_x, max_y = np.max(src_pts, axis=0)

    width = int(max_x - min_x)
    height = int(max_y - min_y)

    # Define destination points based on bounding box dimensions
    dst_pts = np.array([[0, 0], [width, 0], [width, height], [
                       0, height]], dtype='float32')

    # Estimate the homography transformation
    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Apply the transformation
    warped_img = cv2.warpPerspective(img, M, (width, height))

    # Display the rectified image
    cv2.imshow("Rectified Image", warped_img)


if __name__ == '__main__':
    image_path = "myBoard.jpg"
    img = cv2.imread(image_path)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback('Original Image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
