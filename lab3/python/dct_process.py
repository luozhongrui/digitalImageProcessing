# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.metrics import peak_signal_noise_ratio as psnr
#
#
# def process_block(block, matrix):
#     # Apply DCT
#     dct_block = cv2.dct(np.float32(block))
#     # Multiply by the specified matrix
#     processed_block = cv2.multiply(dct_block, matrix)
#     # Apply inverse DCT
#     idct_block = cv2.idct(processed_block)
#     return idct_block
#
#
# def process_block_dft(block, matrix):
#     # Apply DFT
#     dft_block = cv2.dft(np.float32(block), flags=cv2.DFT_COMPLEX_OUTPUT)
#     # Multiply by the specified matrix
#     processed_block = cv2.multiply(dft_block, np.dstack([matrix, matrix]))  # Repeat matrix for both channels
#     # Apply inverse DFT
#     idft_block = cv2.idft(processed_block)
#     return cv2.magnitude(idft_block[:, :, 0], idft_block[:, :, 1])  # Convert complex to magnitude
#
#
# def process_image(img, matrix):
#     block_size = 8
#     blocks_vert = img.shape[0] // block_size
#     blocks_horz = img.shape[1] // block_size
#     processed_image = np.zeros_like(img, dtype=np.float32)
#
#     for i in range(blocks_vert):
#         for j in range(blocks_horz):
#             block = img[i * block_size:(i + 1) * block_size,
#                     j * block_size:(j + 1) * block_size]
#             processed_block = process_block(block, matrix)
#             processed_image[i * block_size:(i + 1) * block_size,
#             j * block_size:(j + 1) * block_size] = processed_block
#
#     return np.float32(processed_image)
#
#
# def process_image_dft(img, matrix):
#     block_size = 8
#     blocks_vert = img.shape[0] // block_size
#     blocks_horz = img.shape[1] // block_size
#     processed_image = np.zeros_like(img, dtype=np.float32)
#
#     for i in range(blocks_vert):
#         for j in range(blocks_horz):
#             block = img[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size]
#             processed_block = process_block_dft(block, matrix)
#             processed_image[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size] = processed_block
#
#     return np.float32(processed_image)
#
#
# def create_matrix(dia):
#     matrix = np.zeros((8, 8), dtype=np.float32)
#     for i in range(8):
#         for j in range(8):
#             if i + j < dia:
#                 matrix[i][j] = 1
#     return matrix
#
#
# def DCT_processing(img):
#     psnr_values = []
#     for i in range(1, 16):
#         matrix = create_matrix(i)
#         # print('Number of Diagonal Lines: ' + str(i))
#         # print(matrix)
#         processed_image = process_image(img, matrix)
#         psnr_value = psnr(img.astype(np.float32), processed_image.astype(
#             np.float32), data_range=processed_image.max() - processed_image.min())
#         psnr_values.append(psnr_value)
#     plt.plot(range(1, 16), psnr_values, marker='o')
#     plt.title('PSNR vs. Number of Diagonal Lines')
#     plt.xlabel('Number of Diagonal Lines')
#     plt.ylabel('PSNR (dB)')
#     plt.grid(True)
#     plt.show()
#
#
# if __name__ == '__main__':
#     # Load the grayscale image
#     img = cv2.imread('image/lena_gray.png', cv2.IMREAD_GRAYSCALE)
#     if img is None:
#         raise FileNotFoundError('Image file not found')
#     img_double = img.astype(np.float64) / 255.0
#     DCT_processing(img_double)


import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr


def create_matrix(dia):
    matrix = np.zeros((8, 8), dtype=np.float64)
    for i in range(8):
        for j in range(8):
            if i + j < dia:
                matrix[i][j] = 1
    return matrix


def process_image_dct(img, matrix):
    # Prepare the mask (repeat the matrix for the entire image)
    mask = np.repeat(np.repeat(matrix, img.shape[0] // 8, axis=0),
                     img.shape[1] // 8, axis=1)

    # Apply DCT
    dct_image = cv2.dct(img)
    # Apply the mask
    filtered_image = cv2.multiply(dct_image, mask)
    # Apply inverse DCT
    idct_image = cv2.idct(filtered_image)

    return np.float64(idct_image)


def DCT_processing(img):
    psnr_values = []
    for i in range(1, 16):
        matrix = create_matrix(i)
        processed_image = process_image_dct(img, matrix)
        psnr_value = psnr(img, processed_image,
                          data_range=processed_image.max() - processed_image.min())
        psnr_values.append(psnr_value)

    print(psnr_values)

    plt.plot(range(1, 16), psnr_values, marker='o')
    plt.title('PSNR vs. Number of Diagonal Lines (DCT)')
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

    DCT_processing(img_double)
