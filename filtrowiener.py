import numpy as np
import matplotlib.pyplot as plt
from skimage import color, data, restoration
from scipy.signal import convolve2d
from skimage.util import random_noise
class FiltroWiener:
        # Carrega e converte para tons de cinza
        img = color.rgb2gray(data.astronaut())  # imagem de exemplo

        # define o efeito de borrado (blur)
        psf = np.ones((5, 5)) / 25
        img_blur = convolve2d(img, psf, mode='same')  # desfoque por média 

        # Adiciona ruído gaussiano
        img_noisy = random_noise(img_blur, mode='gaussian', var=0.001)  # ruído 

        #  Wiener deconvolution
        deconvolved, _ = restoration.unsupervised_wiener(img_noisy, psf)  # filtro de wiener não supervisionado 

        #Exibe os modelos resultante
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        axes[0].imshow(img_noisy, cmap='gray'); axes[0].set_title('Degradada (ruído+desfoque)'); axes[0].axis('off')
        axes[1].imshow(deconvolved, cmap='gray'); axes[1].set_title('Wiener deconvolution'); axes[1].axis('off')

        # Comparação com filtro adaptativo no SciPy
        from scipy.signal import wiener
        wiener_adapt = wiener(img_noisy, mysize=(5,5), noise=None)  # filtro local
        axes[2].imshow(wiener_adapt, cmap='gray'); axes[2].set_title('Wiener local (SciPy)'); axes[2].axis('off')

        plt.tight_layout()
        plt.show()
