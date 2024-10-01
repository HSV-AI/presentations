![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Faster Whisper

https://github.com/SYSTRAN/faster-whisper

This library is a wrapper around the CTranslate2 model that provides an easy way to run pre-translated models stored on HuggingFace, as well as an easy way to translate your own models or load from disk.

Installation was extremely easy following the Github page and had a minimal list of dependencies.

Local testing:

CPU
Beam size = 1
INFO:faster_whisper:Processing audio with duration 30:30.240

| Model      | CPU Time (int8)  | GPU Time (fp16) | GPU Time (fp16_int8) |
|------------|------------|----------|-------------|
| tiny.en    | 0m41.472s  | 2m35.015s | NOTHING |
| tiny       | 1m3.565s   | JUNK |  NOTHING | |
| base.en    | 1m21.794s  | 1m15.815s | 0m41.122s |
| base       | 1m42.560s  | 1m4.441s |  0m52.531s |
| small.en   | 3m33.196s  | 2m57.525s | 1m31.475s |
| small      | 4m23.787s  | 3m4.312s | 1m36.967s |
| medium.en  | 11m12.849s | 7m54.802s | 3m11.600s |
| medium     | 13m10.812s | 7m54.106s | 3m32.465s |
| large-v3   | 40m44.508s | OOM | 10m56.605s |
| large-v3-distil | 10m33.813s | 9m22.329s | 2m38.854s |


Blog post - https://mysoly.nl/speech-to-text-with-faster-whisper-the-high-speed-alternative-to-openai-whisper/

Had to modify my library path to run with GPU enabled - followed this post for instructions - https://github.com/SYSTRAN/faster-whisper/issues/516#issuecomment-1921527758


# AWS Lambda

There are some constraints with using AWS Lambda that you will run into when trying to use anything with a large deployment footprint.

The main hard constraint affecting faster-whisper is the size limit. Because of this, I had to use a docker image to host the function and it's dependencies.

Here's a good article that covers the constraints: https://blog.awsfundamentals.com/lambda-limitations

The main ones that affect us are:
- Max size of the function and all dependencies is 250M
- Limited runtime to 15 minutes
- Max 10G RAM and 6 CPU

| Configured Memory (MB) |	Allocated cores |
|------------------------|------------------|
| 128-1769 |	1 |
|1770-3538	| 2 |
|3539-5307	| 3 |
|5308-7076	| 4 |
|7077-8845	| 5 |
|8846-10240 |	6 |

Lambda lifecycle - https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html#runtimes-lifecycle

https://hub.docker.com/r/amazon/aws-lambda-python

A hidden constraint that will cost you a bit of time is that docker images run with AWS have a read-only file system except for /tmp. This means that everything that downloads artifacts (like HuggingFace models) needs to use /tmp for storage. For testing, I wound up running docker with a read-only flag locally:

```bash
?>docker run --read-only -v /tmp:/tmp -p 9000:8080 --env-file /home/jlangley/git/transcribe/.test-env-file faster-whisper:latest
```

# Tips & Tricks

- Logging - I spent way too long trying to figure this out:
```python
if logging.getLogger().hasHandlers():
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)
```

- Reset Image with each change. Each time you upload a new docker image, you also have to update the image used by the lambda. This also cost me an hour or so.

- Loading a local model - The API for the Faster Whisper model uses a path to the directory containing the model.bin file, not the full path to the model.bin file.

# Questions, Thoughts, Cries of Heresy?