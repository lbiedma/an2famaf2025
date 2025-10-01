from matplotlib.animation import ArtistAnimation
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def save_grayscale(I):
    I8 = (((I - I.min()) / (I.max() - I.min())) * 255.9).astype(np.uint8)
    img = Image.fromarray(I8)
    img.save("original_grayscale.png")

def read_image_and_compute_svd(path):
    # leer imagen
    image = imread(path)
    if image.shape[0] > 1000 and image.shape[1] > 500:
        image = image[::2, ::2]
    # transformar a escala de grises
    image = rgb2gray(image)
    save_grayscale(image)

    U, sigma, V = np.linalg.svd(image, )
    # Create list of images with increasing number of singular values
    return U, sigma, V

def animate_svd_approximation(U, sigma, V):
    possible_ks = [1, 5, 10, 15, 20, 40, 60, 100, 150, 200, 250, 300]

    fig = plt.figure(figsize=(8,8))
    plt.axis('off')
    ims = []
    middle = V.shape[1] / 3

    for r in possible_ks:
        if r > sigma.size:
            break
        reconstructed = (U[:, :r] * sigma[:r]) @ V[:r, :]
        im = plt.imshow(reconstructed, cmap='gray', animated=True)
        txt = plt.text(middle, 1.1, f"Aproximación de orden K = {r}")
        ims.append([im, txt])

    ani = ArtistAnimation(fig, ims, interval=1000, blit=True, repeat_delay=1000)

    # Save animation
    ani.save('svd_reconstruction.gif', writer='pillow')
    plt.close()

U, sigma, V = read_image_and_compute_svd("svd/foto_famaf.jpg")
animate_svd_approximation(U, sigma, V)
