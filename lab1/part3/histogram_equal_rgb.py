import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(1)

# 初始化matplotlib窗口
plt.ion()
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 对每个通道进行直方图均衡化
    channels = cv2.split(frame)
    equ_channels = [cv2.equalizeHist(ch) for ch in channels]
    equ = cv2.merge(equ_channels)

    # 计算直方图
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist_frame = cv2.calcHist([frame], [i], None, [256], [0, 256])
        axs[1, 0].plot(hist_frame, color=col)

        hist_equ = cv2.calcHist([equ], [i], None, [256], [0, 256])
        axs[1, 1].plot(hist_equ, color=col)

    # 显示原始图像和均衡化后的图像
    axs[0, 0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Original Image')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title('Equalized Image')
    axs[0, 1].axis('off')

    axs[1, 0].set_title('Histogram - Original Image')
    axs[1, 0].set_xlim([0, 256])
    axs[1, 0].legend(colors)

    axs[1, 1].set_title('Histogram - Equalized Image')
    axs[1, 1].set_xlim([0, 256])
    axs[1, 1].legend(colors)

    plt.draw()
    plt.pause(0.01)

    # 清除之前的图像，为下一帧做准备
    for ax in axs.ravel():
        ax.clear()

    # 按'q'退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
plt.close(fig)
plt.ioff()
