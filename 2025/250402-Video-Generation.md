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

Here's the basic image and prompt used for all video generation for comparison:

![Remote-NeurIPS](https://hsv.ai/wp-content/uploads/2023/01/neurips-meetup-1024x576.jpg)
```
A cozy, informal classroom filled with natural light. Around 15 diverse attendees sit on mismatched chairs, casually dressed, some taking notes or holding coffee cups. At the front, a confident speaker stands beside a whiteboard and large screen, using a laptop to run an interactive demonstration—perhaps coding live or manipulating a 3D model. The speaker engages with the audience, answering questions and reacting naturally with hand gestures and facial expressions. Occasional audience questions spark short, thoughtful exchanges. The mood is curious and collaborative, with a modern, startup-like atmosphere.
```

## Publicly Available Tools

Started by using the free versions available for both Mochi-1 and Wan2.1.

### Sora
Tried Sora but OpenAI has blocked new account creation until further notice.

### Veo-2
Also attempted Google Veo-2, but I need some kind of special access for their Vertex AI is whitelisted: "Content access: This page is available to approved users that are signed in to their browser with an allowlisted email address. To get started with Veo on Vertex AI, reach out to your Google Cloud account representative."

### Mochi-1
https://www.genmo.ai/play

This is a cool text to video gen application that provides a limited number of video gen per day. It doesn't have a capability of starting from an image or video. I don't think they have a paid option.

### Wan
https://wan.video/wanxiang/videoCreation

Similar to the Mochi-1 model, you can generate a small number of videos per day. The process seems to take much longer, probably because of the queue for processing. Also don't have a paid option, appear to be using this to gain user feedback.

### Runway ML
https://app.runwayml.com/

This is the first free app I came across that also has paid options. It costs 25 credits per 5 seconds of video:
- $15/monthly - Includes 625 Credits monthly
- $35/monthly - Includes 2250 Credits monthly
- $95/monthly - Unlimited


[![IMAGE ALT TEXT HERE](https://hsv.ai/wp-content/uploads/2023/01/neurips-meetup-1024x576.jpg)](https://app.runwayml.com/creation/26ff9d47-7311-4e37-b325-61843cc33b8a)

### Kling AI
https://app.klingai.com/

Cost is 35 credits per 5s video.

- $6.99/month - Includes 660 credits
- $25.99/month - Includes 3000 credits
- $64.99/month - Includes 8000 credits
- Can also purchase credits without a montly membership.

### Hailuoai
https://hailuoai.video/create

Cost is 30 credits per 5s video.

- $9.99/month - Includes 1000 credits
- $34.99/month - Includes 4500 credits
- $94.99/month - Unlimited

### Product thoughts
- Each product has a slightly different approach and set of capabilities. Some allow more control of specific aspects of video generation.
- It appears that these products are 'outrunning' their infrastructure. The last video I did with Kling AI took more than an hour.

## Runpod for Custom Models

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

Gave up again and now trying to step up to a later RTX 4090 and CUDA version. Still couldn't get that to work by default. Was able to use a custom template for Wan1.3B to get a gradio up and running. 

Now trying a different template for ComfyUI.

ComfyUI never got going. Looks like something to check out later though.

Retried using a standard pytorch 2.4 install and got further. Ran out of memory loading the model though, stepping up to an A6000. Still couldn't get there from here.

Bailed back out and started working with https://www.runpod.io/console/explore/758dsjwiqz

ComfyUI is a bit more complex than I would like at this point. Also for some reason, you have to wait a long time (5 minutes) for it to load.

### Wan2GP

Found this project, that appears to use a quantized version of Wan2.1 with gradio - https://github.com/deepbeepmeep/Wan2GP

This actually worked, but the gradio piece does not show the file correctly after it is generated. Had to transfer the file out of the runpod instance to view.