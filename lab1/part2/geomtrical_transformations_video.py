# import cv2
# import numpy as np
#
# # List to store the clicked points
# points = []
#
#
# def click_event(event, x, y, flags, param):
#     global points, frame
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("----------------------------------")
#         print(f"coordinate：({x}, {y})")
#         cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
#         cv2.putText(frame, f"({x}, {y})", (x, y),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#         cv2.imshow('Camera Feed', frame)
#
#         points.append([x, y])
#
#         # Check if we have 4 points
#         if len(points) == 4:
#             perform_projection(points)
#
#
# def perform_projection(pts):
#     global frame
#     # Convert list to numpy array
#     src_pts = np.array(pts, dtype='float32')
#
#     # Compute bounding box of the selected points
#     min_x, min_y = np.min(src_pts, axis=0)
#     max_x, max_y = np.max(src_pts, axis=0)
#
#     width = int(max_x - min_x)
#     height = int(max_y - min_y)
#
#     # Define destination points based on bounding box dimensions
#     dst_pts = np.array([[0, 0], [width, 0], [width, height], [
#                        0, height]], dtype='float32')
#
#     # Estimate the homography transformation
#     M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
#
#     # Apply the transformation
#     warped_img = cv2.warpPerspective(frame, M, (width, height))
#
#     # Display the rectified image
#     cv2.imshow("Rectified Image", warped_img)
#
#
# if __name__ == '__main__':
#     cap = cv2.VideoCapture(1)
#
#     if not cap.isOpened():
#         print("Error: Camera not found!")
#         exit()
#
#     cv2.namedWindow("Camera Feed")
#     cv2.setMouseCallback('Camera Feed', click_event)
#
#     while True:
#         ret, frame = cap.read()
#
#         if not ret:
#             print("Failed to grab frame")
#             break
#
#         cv2.imshow("Camera Feed", frame)
#
#         key = cv2.waitKey(1)
#         if key == 27:  # Press ESC key to exit
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()

import cv2
import numpy as np

# List to store the clicked points
points = []


def click_event(event, x, y, flags, param):
    global points, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        print("----------------------------------")
        print(f"coordinate：({x}, {y})")
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(frame, f"({x}, {y})", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        points.append([x, y])

        # Check if we have 4 points
        if len(points) == 4:
            perform_projection(points)


def perform_projection(pts):
    global frame
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
    warped_img = cv2.warpPerspective(frame, M, (width, height))

    # Display the rectified image
    cv2.imshow("Rectified Image", warped_img)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not found!")
        exit()

    cv2.namedWindow("Camera Feed")
    cv2.setMouseCallback('Camera Feed', click_event)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Draw the clicked points on the frame
        for pt in points:
            cv2.circle(frame, tuple(pt), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"({pt[0]}, {pt[1]})", tuple(pt),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1)
        if key == 27:  # Press ESC key to exit
            break

    cap.release()
    cv2.destroyAllWindows()
