# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

from typing import Tuple

import PIL.TiffTags
import numpy as np
from PIL import Image
from PIL.TiffTags import TAGS


def evc_read_file_info(filename: str) -> Tuple[int, Tuple]:
    """evc_read_file_info extracts the black level (blackLevel) and the neutral
       white value (asShotNeutral) from the image file specified by filename.
    
      INPUT
      filename      ... filename of the image
    
      OUTPUT
      blackLevel    ... black level, which is stored in the image infos (pay attention to the typehint -> it should be an integer!)
      asShotNeutral ... neutral white value, which is stored in the image"""

    ### STUDENT CODE

    image = Image.open(filename)

    """
    Version without a "loop"
    tiffinfo = image.getexif()

    blackLevel = tiffinfo.get(50714)
    asShotNeutral = tiffinfo.get(50728)
    """
    """
    Does this for ... in count as loop?
    """

    meta_dict = {TAGS[key]: image.tag[key] for key in image.tag_v2}
    blackLevel: int = meta_dict['BlackLevel'][0]
    asShotNeutral: Tuple = meta_dict['AsShotNeutral']


    ### END STUDENT CODE
    
    
    return blackLevel, asShotNeutral
    
def evc_transform_colors(input_image: np.ndarray, blackLevel: float) -> np.ndarray:
    """evc_transform_colors adjusts the contrast such that black (blackLevel and
    values below) becomes 0 and white becomes 1.
    The white value of the input image is 65535.
    
      INPUT
      input_image   ... input image
      blackLevel    ... black level of the input image
    
      OUTPUT
      result        ... image in double format where all values are
                        transformed from the interval [blackLevel, 65535]
                        to [0, 1]. All values below the black level have to
                        be 0."""

    ### STUDENT CODE

    array = input_image - blackLevel
    result = array.astype(np.float32) / (65535 - blackLevel)

    ### END STUDENT CODE
    
    
    return result
