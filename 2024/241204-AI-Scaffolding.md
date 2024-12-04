![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# AI Application Scaffolding

This session could also be called "So you trained a model...". It can get tricky to figure out how to take a model that you've trained (or not) and put a public facing interface in front of it.

I ran into this issue about this time last year when I pushed out the first version of the transcription service. I built it initially because I needed it to transcribe these meetups. Most other services (and there are several) either do a poor job or require an account with a monthly service charge, etc. There are also ways to get a transcription for free, but require more uploads and such that I wasn't comfortable with.

## Version 1

- Flask App (pure python)
- Stripe Webform for payment processing
- S3 to store uploaded files
- Lambda triggered by file upload
- ECS task triggered by the Lambda
- DynamoDB for tracking progress and internal metadata
- SES for sending transcript over email

### Requirements:
- Dockerized ECS Tasks (couldn't run the full transcription in a Lambda)
- VPC
- Load Balancer
- Subnets
- Internet Gateway
- AIM
- ECR

### Problems:
- Insanely steep learning curve if you're not a network engineer (VPC) or system admin (AIM)
- Sending people to a seperate Stripe website caused nearly 100% that made it that far to bail.

## Version 2 (currently live)

Changed from a pure Flask App with static pages to a React based front end. 

### Additional Requirements
- React
- SocketIO
- Stripe React Component
- GA React 

### Problems:
- Fixed issue with bailouts over payment form
- Introduced another technology

## Version 3 - currently in dev

Switch over to a faster-whisper model that can run within the constraints of a Lambda.

### Removed Requirements:
- Dockerized ECS Tasks (couldn't run the full transcription in a Lambda)
- VPC
- Load Balancer
- Subnets
- Internet Gateway

### Additional Requirements:
- Simple Queue Service

I'm pretty happy with the results so far. The spinup time with Lambda vs ECS is much faster (within a minute or two) and also provides a way to stream the text back to the website.


