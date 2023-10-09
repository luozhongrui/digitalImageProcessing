import math
import cv2
import numpy as np
from GeometricTransform import get_geometric_transform
from scale import resize_image
from gray2bin import blobs_method, contours_image_method, adaptive_threshold
from calculate_coordinates import  calculate_difference, error_histogram, find_closest_points




if __name__ == '__main__':
    img = cv2.imread("image/pcb.bmp")
    wrap_img = get_geometric_transform(img)
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
    print("Number of Points with an error of more than 3mm: ", len(result))
    print("error coordinate: ", result)
    print("Number of Redundant predetermined coordinates: ", len(remain_coors))
    print("Redundant predetermined coordinates: ", remain_coors)
    print("Number of Redundant key points: ", len(remain_key))
    print("Redundant key points: ", remain_key)



    cv2.imshow("blob_img", blob_img)
    errors, _, _, = find_closest_points(coors.copy(), key_points.copy())
    error_histogram(errors)
    cv2.waitKey(0)
    cv2.destroyAllWindows()