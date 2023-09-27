import cv2

# 鼠标回调函数
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"坐标：({x}, {y})")
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)  # 画一个小圆标记所点击的位置
        cv2.imshow('image', img)


if __name__ == '__main__':
    image_path = "myBoard.jpg"
    img = cv2.imread(image_path)
    cv2.imshow('image', img)

    # 设置鼠标回调函数
    cv2.setMouseCallback('image', click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
