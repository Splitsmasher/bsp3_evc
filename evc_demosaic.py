# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

from typing import Tuple

import numpy as np
import numpy.matlib as matlib
import scipy.ndimage


def evc_demosaic_pattern(input_image: np.ndarray, pattern = 'RGGB') -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """ evc_demosaic_pattern extracts the red, green and blue values of the
     'input' image. Results are stored in the R, G, B variables.
    
      INPUT
      input_image   ... Bayer-Pattern image
      pattern       ... Bayer-Pattern

      OUTPUT
      R             ... red channel of the image (without interpolation)
      G             ... green channel of the image (without interpolation)
      B             ... blue channel of the image (without interpolation)"""

    ### STUDENT CODE

    R = np.zeros(input_image.shape)
    G = np.zeros(input_image.shape)
    B = np.zeros(input_image.shape)
    if pattern == 'RGGB':
        R[::2, ::2] = input_image[::2, ::2]
        G[::2, 1::2]= input_image[::2, 1::2]
        G[1::2, ::2]= input_image[1::2, ::2]
        B[1::2, 1::2] = input_image[1::2, 1::2]
    if pattern == 'BGGR':
        B[::2, ::2] = input_image[::2, ::2]
        G[::2, 1::2] = input_image[::2, 1::2]
        G[1::2, ::2] = input_image[1::2, ::2]
        R[1::2, 1::2] = input_image[1::2, 1::2]
    if pattern == 'GRBG':
        G[::2, ::2] = input_image[::2, ::2]
        R[::2, 1::2] = input_image[::2, 1::2]
        B[1::2, ::2] = input_image[1::2, ::2]
        G[1::2, 1::2] = input_image[1::2, 1::2]
    if pattern == 'GBRG':
        G[::2, ::2] = input_image[::2, ::2]
        B[::2, 1::2] = input_image[::2, 1::2]
        R[1::2, ::2] = input_image[1::2, ::2]
        G[1::2, 1::2] = input_image[1::2, 1::2]

    ### END STUDENT CODE


    return  R,G,B

def evc_transform_neutral(R: np.ndarray, G: np.ndarray, B: np.ndarray, asShotNeutral: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """evc_transform_neutral changes the red, green and blue channels depending
       on the neutral white value (asShotNeutral). Therefore every channel needs
       to be divided by the respective channel of the white value.
    
      INPUT
      R             ... red channel of the image
      G             ... green channel of the image
      B             ... blue channel of the image
      asShotNeutral ... neutral white value (RGB vector)
    
      OUTPUT
      R_trans       ... red channel of the image (changed by neutral white value)
      G_trans       ... green channel of the image (changed by neutral white value)
      B_trans       ... blue channel of the image (changed by neutral white value)"""

    ### STUDENT CODE

    R_trans = R / asShotNeutral[0]
    G_trans = G / asShotNeutral[1]
    B_trans = B / asShotNeutral[2]

    ### END STUDENT CODE


    return R_trans, G_trans, B_trans

def evc_interpolate(red : np.ndarray, green : np.ndarray, blue : np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """evc_interpolate interpolates the red, green and blue channels. In the
       final image, every pixel now has red, green and blue values.
        
        INPUT
        red         ... red channel of the image
        green       ... green channel of the image
        blue        ... blue channel of the image
        
        OUTPUT
        R_inter     ... red channel of the image (without missing values)
        G_inter     ... green channel of the image (without missing values)
        B_inter     ... blue channel of the image (without missing values)"""

    ### STUDENT CODE
    filterGreen = np.array([[0.0, 0.25, 0.0], [0.25, 1.0, 0.25], [0.0, 0.25, 0.0]])
    filterBlueRed = np.array([[0.25, 0.5, 0.25], [0.5, 1.0, 0.5], [0.25, 0.5, 0.25]])
    #https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=7af2ccdb66af0efec7b9db14c41c310c44ac2a84 page 13

    R_inter = scipy.ndimage.correlate(red, filterBlueRed, mode='constant')
    G_inter = scipy.ndimage.correlate(green, filterGreen, mode='constant')
    B_inter = scipy.ndimage.correlate(blue, filterBlueRed, mode='constant')
    ### END STUDENT CODE


    
    return R_inter, G_inter, B_inter

def evc_concat(R: np.ndarray, G: np.ndarray, B: np.ndarray) -> np.ndarray:
    """evc_concat combines the three individual red, green and blue channels to a
    single image.
    
      INPUT
      R             ... red channel of the image
      G             ... green channel of the image
      B             ... blue channel of the image
    
      OUTPUT
      result        ... resulting image"""

    ### STUDENT CODE
    result = np.stack([R, G, B], axis=2)
    ### END STUDENT CODE


    return result
