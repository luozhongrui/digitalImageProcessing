import cv2
from GeometricTransform import get_geometric_transform
from scale import resize_image
from gray2bin import blobs_method
from calculate_coordinates import calculate_difference, error_histogram, find_closest_points
from prettytable import PrettyTable
import numpy as np

if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    # cap.set(3, 1280)  # Set the width (3) property of the camera
    # cap.set(4, 720)
    img = cv2.imread("image/pcb6.jpg")
    img = cv2.resize(img, (1280, 720))
    # img.resize((1280, 720))
    # while True:
    #     ret, frame = cap.read()
    #     img = frame.copy()
    #     cv2.imshow("frame", frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # # matrix = np.load("image/matrix.npy")
    # cap.release()
    wrap_img = get_geometric_transform(img)
    # wrap_img = cv2.warpPerspective(img, matrix, (600, 600))
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
                                                              "Redundant predetermined coordinates", "Number of Redundant real points"]
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
