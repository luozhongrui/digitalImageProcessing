import cv2
import time
import numpy as np
import matplotlib.pyplot as plt


def setUp():
    cam = cv2.VideoCapture(1)
    if not cam.isOpened():
        print("can't open the camera")
        exit(-1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ret, frame = cam.read()
        print(frame.shape)
        yCrCb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

        bgr_frame = cv2.cvtColor(yCrCb_frame, cv2.COLOR_YCrCb2BGR)
        cv2.imshow("video", bgr_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


def YCrCb():
    cam = cv2.VideoCapture("./myBoard.jpg")
    if not cam.isOpened():
        print("can't open the camera")
        exit(-1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cam.read()
    yCrCb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    yCrCb_frame_copy = yCrCb_frame.copy()
    y, cr, cb = cv2.split(yCrCb_frame)
    # adjust the Cr channel
    i = 0.0
    while i < 10.0:
        i += 0.1
        print("Cr gain: {}".format(i))
        yCrCb_frame[:, :, 1] = cr * i
        bgr_frame = cv2.cvtColor(yCrCb_frame, cv2.COLOR_YCrCb2BGR)
        cv2.imshow("YCrCb_Cr", bgr_frame)
        cv2.waitKey(10)
        time.sleep(0.01)
    cv2.destroyWindow("YCrCb_Cr")
    print("--------------------")
    # adjust the Cb channel
    i = 0.0
    yCrCb_frame = yCrCb_frame_copy.copy()
    while i < 10.0:
        i += 0.1
        print("Cb gain: {}".format(i))
        yCrCb_frame[:, :, 2] = cb * i
        bgr_frame = cv2.cvtColor(yCrCb_frame, cv2.COLOR_YCrCb2BGR)
        cv2.imshow("YCrCb_Cb", bgr_frame)
        cv2.waitKey(10)
        time.sleep(0.01)
    print("--------------------")
    cam.release()
    cv2.destroyAllWindows()


def HSV():
    cam = cv2.VideoCapture("./myBoard.jpg")
    if not cam.isOpened():
        print("can't open the camera")
        exit(-1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cam.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_frame)
    hsv_frame_copy = hsv_frame.copy()
    # adjust the H channel
    i = 0.0
    while i < 10.0:
        i += 0.1
        print("H gain: {}".format(i))
        hsv_frame[:, :, 0] = h * i
        bgr_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
        cv2.imshow("HSV_H", bgr_frame)
        cv2.waitKey(10)
        time.sleep(0.1)
    cv2.destroyWindow("HSV_H")
    # adjust the S channel
    i = 0.0
    hsv_frame = hsv_frame_copy.copy()
    while i < 10.0:
        i += 0.1
        print("S gain: {}".format(i))
        hsv_frame[:, :, 1] = s * i
        bgr_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
        cv2.imshow("HSV_S", bgr_frame)
        cv2.waitKey(10)
        time.sleep(0.5)
    cv2.destroyWindow("HSV_S")


def filter_ycbcr():
    cam = cv2.VideoCapture("./myBoard.jpg")
    if not cam.isOpened():
        print("can't open the camera")
        exit(-1)
    kernel = np.ones((3, 3), np.float16) / 9
    print(kernel)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cam.read()
    yCrCb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(yCrCb_frame)
    # filter the Y channel
    y_filter = cv2.filter2D(y, -1, kernel)
    filter_frame = yCrCb_frame.copy()
    filter_frame[:, :, 0] = y_filter
    bgr_frame_y = cv2.cvtColor(yCrCb_frame, cv2.COLOR_YCrCb2BGR)

    # filter the Cr channel
    cr_filter = cv2.filter2D(cr, -1, kernel)
    print(cr_filter)
    print(cr_filter.shape)

    filter_frame = yCrCb_frame.copy()
    filter_frame[:, :, 1] = cr_filter
    bgr_frame_cr = cv2.cvtColor(filter_frame, cv2.COLOR_YCrCb2BGR)

    # filter the Cb channel
    cb_filter = cv2.filter2D(cb, -1, kernel)
    filter_frame = yCrCb_frame.copy()
    filter_frame[:, :, 2] = cb_filter
    bgr_frame_cb = cv2.cvtColor(filter_frame, cv2.COLOR_YCrCb2BGR)

    plt.subplot(2, 2, 1), plt.imshow(frame), plt.title("origin")
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(bgr_frame_y), plt.title("Y_filter")
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(bgr_frame_cr), plt.title("Cr_filter")
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(bgr_frame_cb), plt.title("Cb_filter")
    plt.xticks([]), plt.yticks([])
    plt.show()


def filter_hsv():
    cam = cv2.VideoCapture("./myBoard.jpg")
    if not cam.isOpened():
        print("can't open the camera")
        exit(-1)
    kernel = np.ones((3, 3), np.float16) / 9
    print(kernel)
    ret, frame = cam.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_frame)
    # filter the H channel
    h_filter = cv2.filter2D(h, -1, kernel)
    filter_frame = hsv_frame.copy()
    filter_frame[:, :, 0] = h_filter
    bgr_frame = cv2.cvtColor(filter_frame, cv2.COLOR_HSV2BGR)
    cv2.imshow("H_filter", bgr_frame)

    # filter the S channel
    s_filter = cv2.filter2D(s, -1, kernel)
    filter_frame = hsv_frame.copy()
    filter_frame[:, :, 1] = s_filter
    bgr_frame = cv2.cvtColor(filter_frame, cv2.COLOR_HSV2BGR)
    cv2.imshow("S_filter", bgr_frame)

    cv2.waitKey(0)
    cam.release()


if __name__ == "__main__":
    # setUp()
    # YCrCb()
    # HSV()
    filter_ycbcr()
    filter_hsv()
