# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

from typing import Tuple

import numpy as np


def evc_prepare_histogram_range(input_image: np.ndarray, low: float, high: float) -> Tuple[float, float]:
    """evc_prepare_histogram_range first calculates the new upper- and lower-
    bounds. During the normalization, those two values are then mapped to [0,1].
    If 'low' < 0, it should be set to 0.
    If 'high' > than the maximum intensity in the image, it should be set
    to the maximum intensity.

      INPUT
      input_image	... image
      low   		... current black value
      high  		... current white value

      OUTPUT
      newLow        ... new black value
      newHigh       ... new white value"""

    ### STUDENT CODE
    imageMax = np.max(input_image)

    if imageMax < high:
        newHigh = imageMax
    else:
        newHigh = high
    if low < 0:
        newLow = 0
    else:
        newLow = low
    ### END STUDENT CODE

    return newLow, newHigh


def evc_transform_histogram(input_image: np.ndarray, newLow: float, newHigh: float) -> np.ndarray:
    """ evc_transform_histogram performs the 'histogram normalization' and
        maps the interval [newLow, newHigh] to [0, 1].

        INPUT
        input_image ... image
        newLow   	... black value
        newHigh  	... white value

        OUTPUT
        result		... image after the histogram normalization"""

    ### STUDENT CODE

    result = input_image * ((input_image - newLow) / (newHigh - newLow))

    ### END STUDENT CODE

    return result


def evc_clip_histogram(input_image: np.ndarray) -> np.ndarray:
    """ After the transformation of the histogram, evc_clip_histogram sets all
    values that are < 0 to 0 and values that are > 1 to 1.

      INPUT
      input_image   ... image after the histogram normalization

      OUTPUT
      result		... image after the clipping operation"""

    ### STUDENT CODE

    result = np.where(input_image < 0., 0., input_image)
    result = np.where(result > 1., 1., result)
    ### END STUDENT CODE

    return result
