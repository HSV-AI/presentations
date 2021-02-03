#! /bin/bash -e
image_name=bugs
docker run -e WANDB_API_KEY=$WANDB_API_KEY $image_name python main.py --n_components 6 --lr_decay 0.1