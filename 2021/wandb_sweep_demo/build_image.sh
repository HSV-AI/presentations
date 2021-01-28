#! /bin/bash -e
image_name=bugs
image_tag=0.1
full_image_name=${image_name}:${image_tag}

cd "$(dirname "$0")" 
docker build -t "${image_name}:latest" -t "${full_image_name}" .