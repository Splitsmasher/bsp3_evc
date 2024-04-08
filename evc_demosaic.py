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
    # TODO: Implement this function.
    # HINT: For this task the "start:end:step" array slicing might be useful.
    #       Find the correct Bayer-Pattern depending on your dataset.
    #       No interpolation needs to be performed here!

	# NOTE: The following three lines can be removed. They prevent the framework
    #       from crashing.

    R = np.zeros(input_image.shape)
    G = np.zeros(input_image.shape)
    B = np.zeros(input_image.shape)
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
    # TODO: Implement this function.
	# NOTE: The following three lines can be removed. They prevent the framework
    #       from crashing.

    R_trans = np.zeros(R.shape)
    G_trans = np.zeros(G.shape)
    B_trans = np.zeros(B.shape)
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
    # TODO: Implement this function.
	# HINT: The function 'scipy.ndimage.correlate' might be useful.
	# NOTE: The following three lines can be removed. They prevent the framework
    #       from crashing.

    R_inter = np.zeros(np.shape(red))
    G_inter = np.zeros(np.shape(green))
    B_inter = np.zeros(np.shape(blue))
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
    # TODO: Implement this function.
    # HINT: The function 'np.stack' might be useful.
    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.

    result = np.zeros([*R.shape[:2], 3])
    ### END STUDENT CODE


    return result
