![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

## AI Huntsville Taskforce

- Moved to the Workforce Development committee - trying to put together a community wide session for April 10th.

## American Planning Association

North Alabama chair reached out, and we're planning a lunch-and-learn session for them on April 25th. We can bring folks from our group to interact, but I need to know who beforehand.

# Video Generation

Started by using the free versions available for both Mochi-1 and Wan2.1. Tried Sora but OpenAI has blocked new account creation until further notice.

https://www.genmo.ai/play

https://wan.video/wanxiang/videoCreation

Image ![Remote-NeurIPS](https://hsv.ai/wp-content/uploads/2023/01/neurips-meetup-1024x576.jpg)
Prompt:
```
A cozy, informal classroom filled with natural light. Around 15 diverse attendees sit on mismatched chairs, casually dressed, some taking notes or holding coffee cups. At the front, a confident speaker stands beside a whiteboard and large screen, using a laptop to run an interactive demonstration—perhaps coding live or manipulating a 3D model. The speaker engages with the audience, answering questions and reacting naturally with hand gestures and facial expressions. Occasional audience questions spark short, thoughtful exchanges. The mood is curious and collaborative, with a modern, startup-like atmosphere.
```

Moved to Runpod to try and run the Wan2.1 model myself. Used the RTX A5000 24G (cheap) along with a python 3.11 / pytorch 2.4.0 template.

Then ran into an issue where I had to set up billing first, and then add $25 to my credits - and then start over to deploy a pod.

Pricing Summary
- GPU Cost: $0.29 / hr
- Running Pod Disk Cost: $0.006 / hr
- Stopped Pod Disk Cost: $0.006 / hr

Pod was up an running within a minute.

Followed instructions from the Wan2.1 Hugging Face page - https://huggingface.co/Wan-AI/Wan2.1-T2V-14B

Didn't get too far before running out of space on device.

Upped the container storage from 20G to 100G and started over. Total use after downloading the model was 65G.

Gave up trying the 14B model and switched to the 1.3B. Max download size is now 17G.

Model is still not using GPU.

Gave up again and now trying to step up to a later RTX 4090 and CUDA version. Still couldn't get that to work by default. Was able to use a custom template for Wan1.3B to get a gradio up and running. Now trying a different template for ComfyUI.

ComfyUI never got going. Looks like something to check out later though.

Retried using a standard pytorch 2.4 install and got further. Ran out of memory loading the model though, stepping up to an A6000. Still couldn't get there from here.

Bailed back out and started working with https://www.runpod.io/console/explore/758dsjwiqz