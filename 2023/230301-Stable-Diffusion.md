![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Agenda

- Welcome
- Stable Diffusion
- Questions / Comments
- Plan for next week
- Close

# Welcome

- Vision
- Mission
- How to Connect

![Meetup Image](https://user-images.githubusercontent.com/6886690/221392704-e6b3f46f-5bac-4224-843e-e90ae68e9e2a.png)

# Stable Diffusion

Before using Stable Diffusion in a product, or to produce images that you may use in your product - be sure to read the [LICENSE](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

As an extension of the session from last week, use ChatGPT to generate a description of Stable Diffusion and see how well it works.

---

Just kidding - Stable Diffusion didn't exist when the current ChatGPT model was trained. We'll have to use the old standby:

[WIKIPEDIA!](https://en.wikipedia.org/wiki/Stable_Diffusion)

Stable Diffusion is primarily used to generate detailed images conditioned on text descriptions, though it can also be applied to other tasks such as inpainting, outpainting, and generating image-to-image translations guided by a text prompt.

Stable Diffusion uses a latent diffusion model that is trained with the objective of removing successive applications of Gaussian noise on training images.

## Architecture:

 Stable Diffusion consists of 3 parts: the variational autoencoder (VAE), U-Net, and an optional text encoder.

 The VAE encoder compresses the image from pixel space to a smaller dimensional latent space. Gaussian noise is iteratively applied to the compressed latent representation during forward diffusion. The U-Net block denoises the output from forward diffusion backwards to obtain a latent representation. Finally, the VAE decoder generates the final image by converting the representation back into pixel space.

Maybe a diagram will help: ![Diagram](https://upload.wikimedia.org/wikipedia/commons/f/f6/Stable_Diffusion_architecture.png)

The denoising step can be conditioned on a string of text, an image, or another modality. The encoded conditioning data is exposed to denoising U-Nets with a cross-attention mechanism. For conditioning on text, the fixed, pretrained CLIP ViT-L/14 text encoder is used to transform text prompts to an embedding space.

## The Usual Problems:

- Data bias - Certain types of images are difficult to generate, due to having limited examples in the training data.
- Image Dimensions - Hope you really love 512x512 or 768x768 images.
- Combined bias between the training images as well as the CLIP text encoder can create some interesting outputs.

## Training:
The model was trained using 256 Nvidia A100 GPUs on Amazon Web Services for a total of 150,000 GPU-hours, at a cost of $600,000.

It can be fine tuned, such as this project which created a new Stable Diffusion model for Anime - [https://huggingface.co/hakurei/waifu-diffusion](https://huggingface.co/hakurei/waifu-diffusion)

![New Astronaut](https://user-images.githubusercontent.com/6886690/222052430-16c74585-7239-4036-a263-d90d98151e41.png)

## Running in the Cloud:

[https://huggingface.co/spaces/stabilityai/stable-diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion)

## Running Locally:

[https://huggingface.co/spaces/stabilityai/stable-diffusion/blob/main/app.py](https://huggingface.co/spaces/stabilityai/stable-diffusion/blob/main/app.py)

# Discussion

# Plan for next week

[Kanban Board](https://github.com/HSV-AI/presentations/projects/1)

