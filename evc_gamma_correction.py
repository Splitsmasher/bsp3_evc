# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np

def rgb2gray(rgb : np.ndarray):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return np.clip(gray, 0, 1)

def evc_compute_brightness(input_image: np.ndarray) -> np.ndarray:
    """evc_compute_brightness calculates the brightness of the input image.
       First the image is normalized by multiplying it with the reciprocal of
       the maximum value of all three color channels. The brightness is then
       retrieved by computing a gray-scale image. Afterwards the result
       is multiplied by the maximum value.
    
      INPUT
      input_image ... image matrix of dimension: (n, m, 3)
    
      OUTPUT
      brightness  ... brightness of the image, matrix of dimension (n, m)"""

    ### STUDENT CODE

    normalized = input_image / np.max(input_image)
    brightness = rgb2gray(normalized)
    brightness *= np.max(input_image)

    ### END STUDENT CODE


    return brightness

def evc_compute_chromaticity(input_image: np.ndarray, brightness: np.ndarray) -> np.ndarray:
    """ evc_compute_chromaticity calculates the chromaticity of the 'input' image
    using the 'brightness' values. Therefore the color channels of the input
    image are individually divided by the brightness values.
    
      INPUT
      input_image   ... image, dimension (n, m, 3)
      brightness    ... brightness values, dimension (n, m)

      OUTPUT
      chromaticity  ... chromaticity of the image, dimension (n, m, 3)"""

    ### STUDENT CODE

    chromaticity = np.copy(input_image)

    chromaticity[:, :, 0] /= brightness
    chromaticity[:, :, 1] /= brightness
    chromaticity[:, :, 2] /= brightness

    ### END STUDENT CODE


    return chromaticity

def evc_gamma_correct(input_image: np.ndarray, gamma: float) -> np.ndarray:
    """evc_gamma_correct performs gamma correction on the 'input_image' image.
    This is done by raising it to the power of the reciprocal value of gamma
    (gamma**(-1)).
    
      INPUT
      input_image ... image
      gamma       ... gamma value
    
      OUTPUT
      corrected   ... image after gamma correction"""

    ### STUDENT CODE
    if gamma < 0.0000000001:
        gamma = 0.0000000001

    corrected = input_image * (gamma**(-1))
    ### END STUDENT CODE


    return corrected

def evc_reconstruct(brightness_corrected: np.ndarray, chromaticity) -> np.ndarray:
    """ evc_reconstruct reconstructs the color values by multiplying the corrected
    brightness with the chromaticity.
    
      INPUT
      brightness_corrected  ... gamma-corrected brightness values
      chromaticity          ... chromaticity
    
      OUTPUT
      result                ... reconstructed image"""

    ### STUDENT CODE
    result = np.copy(chromaticity)

    result[:, :, 0] *= brightness_corrected
    result[:, :, 1] *= brightness_corrected
    result[:, :, 2] *= brightness_corrected

    ### END STUDENT CODE


    return result
