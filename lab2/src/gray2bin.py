import cv2
import numpy as np



def adaptive_threshold(image):
    _, thresholded_image = cv2.threshold(image, 3, 255,
                                         cv2.THRESH_BINARY_INV)

    return thresholded_image


def apply_morphological_operation(image):
    circle_size = 7  # 圆形结构元素的半径
    circle_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                              (circle_size, circle_size))
    dilated_image = cv2.dilate(image, circle_kernel, iterations=1)
    kernel = np.ones((5, 5), np.uint8)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)

    circle_size = 3  # 圆形结构元素的半径
    circle_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                              (circle_size, circle_size))
    dilated_image = cv2.dilate(eroded_image, circle_kernel, iterations=1)
    kernel = np.ones((3, 3), np.uint8)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)
    circle_size = 7  # 圆形结构元素的半径
    circle_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                              (circle_size, circle_size))
    dilated_image = cv2.dilate(eroded_image, circle_kernel, iterations=1)
    dilated_image[393: 407, 286:299] = 0
    dilated_image[762:784, 204:223] = 0
    dilated_image[518:529, 270:284] = 0
    dilated_image[541:553, 270:282] = 0
    return dilated_image


# Blob Detection
def detect_blobs(image, original_img):
    circle_image = cv2.bitwise_not(image)
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 50
    params.maxThreshold = 144
    # 设置最小和最大的面积
    params.filterByArea = True
    params.minArea = 11
    params.maxArea = 200
    params.filterByCircularity = True
    params.minCircularity = 0.82     # 圆形度
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(circle_image)

    # 绘制轮廓（可选）
    make_image = cv2.cvtColor(original_img, cv2.COLOR_GRAY2BGR)
    img_with_keypoints = cv2.drawKeypoints(make_image, keypoints, np.array([]),
                                           (0, 255, 0),
                                           cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return keypoints, img_with_keypoints


def blobs_method(image):
    thresholded_image = adaptive_threshold(image)
    dilated_image = apply_morphological_operation(thresholded_image)
    keypoints, image_blob = detect_blobs(dilated_image, image)
    return keypoints, image_blob




if __name__ == '__main__':
    # 加载图像并转换为灰度
    image = cv2.imread("image/scale.jpg", cv2.IMREAD_GRAYSCALE)
    image = cv2.equalizeHist(image)
    point, image_blob = blobs_method(image)
    cv2.imshow("image_blob", image_blob)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
