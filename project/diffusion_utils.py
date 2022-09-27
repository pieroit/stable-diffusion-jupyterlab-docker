import inspect
from typing import List, Optional, Union
from tqdm.auto import tqdm
from torch import autocast
import torch

import PIL
from PIL import Image
import numpy as np  
    
# image preprocessing
def stable_diffusion_preprocess_image(image):
    
    w, h = image.size
    w, h = map(lambda x: x - x % 32, (w, h))  # resize to integer multiple of 32
    image = image.resize((w, h), resample=PIL.Image.LANCZOS)
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.*image - 1.