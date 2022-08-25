
# Stable Diffusion JupyterLab Docker

Generate images with Stable Diffusion inside JupyterLab!

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker compose](https://docs.docker.com/compose/install/)
- [Nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
- Log into Huggin Face and accept [Stable Diffusion License](https://huggingface.co/CompVis/stable-diffusion-v1-4)
- Generate a [Hugging Face token](https://huggingface.co/settings/tokens)

## How to run
- Fire up a terminal and clone this repo

    ```
    git clone https://github.com/pieroit/stable-diffusion-jupyterlab-docker.git
    ```
 - Jump into the folder

    ```
    cd xxxxxxxxx
    ```
- Run container

    ```
    docker-compose up
    ```

- The first time (only) it will take a while. At the end you should see a link in the terminal, click on it and JupyterLab should open in the browser.

- Run the first notebook to download SD and save it on disk
- Use the second notebook to load SD from disk and use it. Enjoy!!!

- To stop the workstation, CTRL+c in the terminal and then

    ```
    docker-compose down
    ```
