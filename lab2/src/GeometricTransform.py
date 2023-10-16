import cv2
import numpy as np
from utils import get_coordinate

points = []
img = np.ones((1000, 1000, 3), np.uint8)
wrap_img = np.ones((750, 750, 3), np.uint8)
dump = np.ones((1000, 1000, 3), np.uint8)
flag = True


def click_event(event, x, y, flags, param):
    global points, img, wrap_img, flag
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow("Geometric", img)
        points.append([x, y])
        if len(points) == 8:
            # print("Projected change origin and target")
            # print(points)
            wrap_img = warp_image()
            flag = False
            cv2.destroyAllWindows()


def warp_image():
    global points, dump
    target_points = points[4:]
    points = points[:4]
    dst_points = np.array(target_points, dtype=np.float32)

    matrix, _ = cv2.findHomography(np.array(points, dtype=np.float32),
                                   dst_points, cv2.RANSAC, 5.0)
    # np.save("image/matrix.npy", matrix)
    result = cv2.warpPerspective(dump, matrix, (600, 600))
    # cv2.imwrite("image/warp.jpg", result)
    points = []
    return result


def get_geometric_transform(image):
    global wrap_img, dump, img, flag, points
    dump = image.copy()
    img = image
    coordinates = get_coordinate()
    for coordinate in coordinates:
        cv2.circle(img, (int(coordinate[0]), int(coordinate[1])), 3,
                   (0, 255, 0), -1)
    cv2.imshow("Geometric", img)
    cv2.setMouseCallback("Geometric", click_event)
    while flag:
        cv2.waitKey(1)
    points = []
    flag = True
    return wrap_img


if __name__ == '__main__':
    img = cv2.imread("image/pcb.bmp")
    img = cv2.resize(img, (1280, 720))
    wrap_img = get_geometric_transform(img)
    coordinates = get_coordinate()
    for coordinate in coordinates:
        cv2.circle(wrap_img, (int(coordinate[0]), int(coordinate[1])), 3,
                   (0, 255, 0), -1)

    cv2.imshow("wrap", wrap_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
