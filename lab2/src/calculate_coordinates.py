import math
from utils import get_coordinate
import cv2
import matplotlib.pyplot as plt


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 +
                     (point1[1] - point2[1]) ** 2)


def find_closest_points(set1, set2):
    closest_points = []
    remaining_points_1 = []
    remaining_points_2 = []
    while set1 and set2:
        min_x_diff = float('inf')
        min_y_diff = float('inf')
        closest_pair = None
        for point1 in set1:
            for point2 in set2:
                x_diff = abs(point1[0] - point2[0])
                y_diff = abs(point1[1] - point2[1])
                if x_diff < min_x_diff or (x_diff == min_x_diff and y_diff <
                                           min_y_diff):
                    min_x_diff = x_diff
                    min_y_diff = y_diff
                    closest_pair = (point1, point2)
        set1.remove(closest_pair[0])
        set2.remove(closest_pair[1])
        if closest_pair:
            closest_points.append(closest_pair)
    if set1:
        remaining_points_1.extend(set1)
    if set2:
        remaining_points_2.extend(set2)

    return closest_points, remaining_points_1, remaining_points_2


def calculate_difference(set1, set2):
    closest_points, remaining_points_1, remaining_points_2 \
        = find_closest_points(set1, set2)
    error_points = []
    for point1, point2 in closest_points:
        dis = euclidean_distance(point1, point2)
        if dis >= 6:
            error_points.append((point1, point2))
    return error_points, remaining_points_1, remaining_points_2


def error_histogram(error_points):
    histogram = []
    for point1, point2 in error_points:
        histogram.append(euclidean_distance(point1, point2) * 0.075)
    plt.hist(histogram, bins=20, color='steelblue', edgecolor='k')
    plt.xlabel('inaccuracies')
    plt.ylabel('number')
    plt.title('error histogram')
    plt.show()


if __name__ == '__main__':
    # 输入两组坐标集合
    coors = get_coordinate("image/scale.csv")
    key_point = get_coordinate("image/result.csv")
    result, remain_coors, remain_key = calculate_difference(coors, key_point)
    print(len(result))
    print("error points: ", result)
    print("remain_coors: ", remain_coors)
    print("remain_key: ", remain_key)
    coors = get_coordinate("image/scale.csv")
    key_point = get_coordinate("image/result.csv")

    error, _, _ = find_closest_points(coors, key_point)
    error_histogram(error)
