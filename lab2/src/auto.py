import cv2
from GeometricTransform import get_geometric_transform
from scale import resize_image
from gray2bin import blobs_method
from calculate_coordinates import calculate_difference, error_histogram, find_closest_points
from prettytable import PrettyTable
import numpy as np
from utils import get_coordinate


def get_marker(event, x, y, flags, param):
    location, img = param
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 6, (0, 0, 255), -1)
        cv2.imshow("setup", img)
        location.append([x, y])
        if len(location) == 8:
            # np.save("image/location.npy", np.array(location, dtype=np.int32))
            cv2.line(img, (location[0][0], location[0][1]),
                     (location[1][0], location[1][1]), (0, 0, 255), 2)
            cv2.line(img, (location[0][0], location[0][1]), (location[3][0],
                                                             location[3][1]),
                     (0, 0, 255), 2)
            cv2.line(img, (location[1][0], location[1][1]), (location[2][0],
                                                             location[2][1]), (0, 0, 255), 2)
            cv2.line(img, (location[2][0], location[2][1]), (location[3][0],
                                                             location[3][1]), (0, 0, 255), 2)
            cv2.imshow("setup", img)
            print("location saved")


def get_matrix(event, x, y, flags, param):
    label, image = param
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow("setup_matrix", image)
        label.append([x, y])
        if len(label) == 8:
            matrix, _ = cv2.findHomography(np.array(label[:4],
                                                    dtype=np.float32),
                                           np.array(label[4:], dtype=np.float32), cv2.RANSAC, 5.0)
            np.save("image/matrix_set.npy", np.array(matrix, dtype=np.float32))
            print("matrix saved")



def setup_location(img):
    loc = []
    cv2.imshow("setup", img)
    cv2.setMouseCallback("setup", get_marker, param=[loc, img])
    cv2.waitKey(0)
    cv2.destroyWindow("setup")
    np.save("image/location_set.npy", np.array(loc, dtype=np.int32))
    coordinates = get_coordinate()
    for coordinate in coordinates:
        cv2.circle(img, (int(coordinate[0]), int(coordinate[1])), 3,
                   (0, 255, 0), -1)
    label = []
    cv2.imshow("setup_matrix", img)
    cv2.setMouseCallback("setup_matrix", get_matrix, param=[label, img])
    cv2.waitKey(0)
    cv2.destroyWindow("setup_matrix")


def draw_roi(img, coors):
    location = coors[:4]
    cv2.line(img, (location[0][0], location[0][1]),
             (location[1][0], location[1][1]), (0, 0, 255), 2)
    cv2.line(img, (location[0][0], location[0][1]), (location[3][0],
                                                     location[3][1]),
             (0, 0, 255), 2)
    cv2.line(img, (location[1][0], location[1][1]), (location[2][0],
                                                     location[2][1]),
             (0, 0, 255), 2)
    cv2.line(img, (location[2][0], location[2][1]), (location[3][0],
                                                     location[3][1]),
             (0, 0, 255), 2)
    for coor in coors[4:]:
        cv2.circle(img, (coor[0], coor[1]), 5, (0, 0, 255), -1)

    return img


def run(img, matrix):
    wrap_img = cv2.warpPerspective(img, matrix, (600, 600))
    scale_img, coors = resize_image(wrap_img, 1000)
    scale_img = cv2.cvtColor(scale_img, cv2.COLOR_BGR2GRAY)
    scale_img = cv2.equalizeHist(scale_img)
    blob_points, blob_img = blobs_method(scale_img)
    for coor in coors:
        cv2.circle(blob_img, (coor[0], coor[1]), 5, (0, 0, 255), -1)
    key_points = []
    for point in blob_points:
        key_points.append(point.pt)
    result, remain_coors, remain_key = calculate_difference(coors.copy(),
                                                            key_points.copy())
    table = PrettyTable()
    table.field_names = ["Number of errors greater than 3mm", "Number of "
                                                              "Redundant predetermined coordinates",
                         "Number of Redundant real points"]
    table.add_row([len(result), len(remain_coors), len(remain_key)])
    print(table)
    table = PrettyTable()
    table.field_names = [
        "error coordinate",
        "Redundant predetermined coordinates",
        "Redundant real points"]
    table.add_row([result, remain_coors, remain_key])
    table.max_width = 50
    print(table)

    cv2.imshow("blob_img", blob_img)
    errors, _, _, = find_closest_points(coors.copy(), key_points.copy())
    error_histogram(errors)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # Set the width (3) property of the camera
    cap.set(4, 720)
    flag = False
    while True:
        ret, frame = cap.read()
        img = frame.copy()
        if flag:
            draw_roi(frame, location)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            setup_location(img.copy())
            flag = True
            location = np.load("image/location_set.npy")
        if cv2.waitKey(1) & 0xFF == ord('d'):
            matrix = np.load("image/matrix_set.npy")
            run(img.copy(), matrix)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow("frame")
            break


