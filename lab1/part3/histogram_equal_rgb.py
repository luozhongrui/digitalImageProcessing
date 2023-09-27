import cv2
import numpy as np
import matplotlib.pyplot as plt


def add_fog(image, fog_intensity=0.5, fog_color=(255, 255, 255)):
    """
    添加雾化效果

    :param image: 输入的图像
    :param fog_intensity: 雾的浓度，范围[0, 1]，值越大雾越浓
    :param fog_color: 雾的颜色，默认为白色
    :return: 添加雾后的图像
    """

    # 根据雾的浓度和颜色创建一个雾化层
    fog_layer = np.ones_like(image, dtype=np.uint8) * \
        np.array(fog_color, dtype=np.uint8)

    # 使用加权和合并原始图像和雾化层
    fogged_image = cv2.addWeighted(
        image,
        1 - fog_intensity,
        fog_layer,
        fog_intensity,
        0)

    return fogged_image


if __name__ == '__main__':
    cap = cv2.VideoCapture(1)

    # Initialize the matplotlib window
    plt.ion()
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = add_fog(frame, fog_intensity=0.4)
        # Convert to grayscale image
        channels = cv2.split(frame)
        equ_channels = [cv2.equalizeHist(ch) for ch in channels]
        equ = cv2.merge(equ_channels)

        # Calculate Histogram
        colors = ('b', 'g', 'r')
        for i, col in enumerate(colors):
            hist_frame = cv2.calcHist([frame], [i], None, [256], [0, 256])
            axs[1, 0].plot(hist_frame, color=col)

            hist_equ = cv2.calcHist([equ], [i], None, [256], [0, 256])
            axs[1, 1].plot(hist_equ, color=col)

        # Display original image and equalized image
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

        # Clear previous image for next frame
        for ax in axs.ravel():
            ax.clear()

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    plt.close(fig)
    plt.ioff()
