import cv2
import csv
from utils import get_coordinate, project_coordinates


def resize_image(img, target=1000):
    scale = target / img.shape[0]
    # print("scale:", scale)
    img_scale = cv2.resize(img, (target, target))
    coordinates = get_coordinate()
    new_coordinates = project_coordinates(coordinates, scale)
    return img_scale, new_coordinates


if __name__ == '__main__':
    img = cv2.imread("image/warp.jpg")
    scale_img, coors = resize_image(img, 1000)
    cv2.imwrite("image/scale.jpg", scale_img)
    with open("image/scale.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(coors)
    print("coordinate write to image/scale.csv")
    print("img shape:", scale_img.shape)
    print(coors[0])
    for coordinate in coors:
        cv2.circle(scale_img, (int(coordinate[0]), int(coordinate[1])), 2,
                   (0, 255, 0), -1)
    cv2.imshow("scale", scale_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

