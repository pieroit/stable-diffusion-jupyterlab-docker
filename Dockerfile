
# official pytorch + GPU image
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

# base libs
RUN pip install \
    scikit-learn \
    pandas \
    seaborn \
    jupyterlab \
    jupyterlab_widgets \
    "ipywidgets>=7,<8" \
    jupyter-dash

# stable diffusion stuff
RUN pip install --upgrade diffusers transformers scipy ftfy python-slugify

RUN mkdir project
WORKDIR /project
