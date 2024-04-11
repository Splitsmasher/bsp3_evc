# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np

def evc_white_balance(input_image: np.ndarray, white: np.ndarray) -> np.ndarray:
    """evc_white_balance performs white balancing manually.
    
      INPUT
      input_image ... image
      white       ... a color (as RGB vector) that should become the new white
    
      OUTPUT
      result      ... result after white balance"""
    
    
    ### STUDENT CODE

    result = np.copy(input_image)

    if white[0] != 0.:
        result[:, :, 0] = result[:, :, 0] * (1 / white[0])
    if white[1] != 0.:
        result[:, :, 1] = result[:, :, 1] * (1 / white[1])
    if white[2] != 0.:
        result[:, :, 2] = result[:, :, 2] * (1 / white[2])
    ### END STUDENT CODE
    
    result = np.minimum(result, 1)
    return result
