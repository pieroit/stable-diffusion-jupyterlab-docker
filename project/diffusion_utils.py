import inspect
from typing import List, Optional, Union
from tqdm.auto import tqdm
from torch import autocast
import torch

import PIL
from PIL import Image
import numpy as np  

def stable_diffusion_preprocess_image(image_path, mask_path=None, width=512, height=512):
    
    # force width and height to be multiple of 32
    width, height = map(lambda x: x - x % 32, (width, height))
    
    image = Image.open(image_path).convert('RGB').resize((width, height))
    
    if mask_path:
        mask = Image.open(mask_path).convert('RGB').resize((width, height))
        side_by_side = Image.new('RGB', (width*2, height))
        side_by_side.paste(image, (0, 0))
        side_by_side.paste(mask, (width, 0))
        return image, mask, side_by_side
    
    return image

    