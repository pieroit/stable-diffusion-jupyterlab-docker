
# official pytorch + GPU image
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

# install git
RUN apt-get -y update
RUN apt-get -y install git

# base libs
RUN pip install \
    scikit-learn \
    pandas \
    seaborn \
    jupyterlab \
    jupyterlab_widgets \
    "ipywidgets>=7,<8" \
    jupyter-dash

# install stable diffusion from source
RUN pip install git+https://github.com/huggingface/diffusers.git@main

# install utilities
RUN pip install --upgrade transformers scipy ftfy python-slugify

RUN mkdir project
WORKDIR /project
