import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr


def create_matrix(dia):
    matrix = np.zeros((8, 8), dtype=np.float32)
    for i in range(8):
        for j in range(8):
            if i + j < dia:
                matrix[i][j] = 1
    return matrix


def process_image_dft(img, matrix):
    # Apply DFT
    dft_image = np.fft.fft2(img)
    # Shift zero frequency components to the center
    dft_shift = np.fft.fftshift(dft_image)

    # Prepare the mask (repeat the matrix for both real and imaginary parts)
    mask = np.repeat(np.repeat(matrix, img.shape[0] // 8, axis=0),
                     img.shape[1] // 8, axis=1)

    # Apply the mask
    filtered_shift = dft_shift * mask

    # Inverse shift
    filtered_ishift = np.fft.ifftshift(filtered_shift)
    # Inverse DFT
    idft_image = np.fft.ifft2(filtered_ishift)
    # Get magnitude (as the result may have imaginary part due to numerical errors)
    processed_image = np.abs(idft_image)

    return np.float64(processed_image)


def DFT_processing(img):
    psnr_values = []
    for i in range(1, 16):
        matrix = create_matrix(i)
        processed_image = process_image_dft(img, matrix)
        psnr_value = cv2.PSNR(img, processed_image)
        psnr_values.append(psnr_value)

    print(psnr_values)

    plt.plot(range(1, 16), psnr_values, marker='o')
    plt.title('PSNR vs. Number of Diagonal Lines (DFT)')
    plt.xlabel('Number of Diagonal Lines')
    plt.ylabel('PSNR (dB)')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # Load the grayscale image
    img = cv2.imread('image/lena_gray.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError('Image file not found')

    # Convert the image to double (float64) and normalize to [0, 1]
    img_double = img.astype(np.float64) / 255.0

    DFT_processing(img_double)
