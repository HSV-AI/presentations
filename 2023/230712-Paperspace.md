![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Agenda

- Welcome
- Virtual GPU with Paperspace
- Questions / Comments
- Plan next meetup
- Close

# Welcome

- Vision
- Mission
- How to Connect

![Meetup Image](https://user-images.githubusercontent.com/6886690/252126546-17d4915c-153e-4a2a-99df-d7ba2e783612.png)

# Paperspace

DraGAN uses a conda environment to install, so started with that:

https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh

Requirements for DraGAN:

- Linux and Windows are supported, but we recommend Linux for performance and compatibility reasons.
- 1–8 high-end NVIDIA GPUs with at least 12 GB of memory. We have done all testing and development using Tesla V100 and A100 GPUs.
- 64-bit Python 3.8 and PyTorch 1.9.0 (or later). See https://pytorch.org for PyTorch install instructions.
- CUDA toolkit 11.1 or later. (Why is a separate CUDA toolkit installation required? See Troubleshooting).
- GCC 7 or later (Linux) or Visual Studio (Windows) compilers. Recommended GCC version depends on CUDA version, see for example CUDA 11.4 system requirements.
- Python libraries: see environment.yml for exact library dependencies. You can use the following commands with Miniconda3 to create and activate your StyleGAN3 Python environment:
```
conda env create -f environment.yml
conda activate stylegan3
```

Tried it at first with the P4000 (8GB RAM GPU) but couldn't get anywhere. Might try again later. Stepped up to the P5000 (16GB RAM GPU) and ran into this fun dialog:


![Problem](https://user-images.githubusercontent.com/6886690/252544871-477b5b43-abea-4e07-95bb-04fb09bb4fe9.png)


When done - File->Close Remote Connection

**Observiations**

- Network seems to be a little slow. Downloading model weights for DraGAN averaged about 55mbs - but that seems to be dragged down by the one model downloaded by nvidia hosting.

# Discussion

# Plan for next week

[Kanban Board](https://github.com/HSV-AI/presentations/projects/1)

