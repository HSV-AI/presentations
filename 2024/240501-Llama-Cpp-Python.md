![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Llama-Cpp-Python

Outline provided by perplexity.ai

I'm giving a talk this week about llama-cpp-python. What outline should I use?

Here is a suggested outline for your talk on llama-cpp-python:

## Introduction
- Brief overview of llama.cpp and its purpose
- Importance of running large language models locally

## Installation

- Requirements: Python 3.8+, C compiler
- Installing llama-cpp-python via pip
- Installing with CUDA, Metal, BLAS support[1][2]


**I was only able to get CUDA to work by installing with:**
```
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

![Image](https://private-user-images.githubusercontent.com/6886690/326299396-a9a1f8e5-52f8-4b4a-840d-1f3761f49839.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTQ2MDMyODQsIm5iZiI6MTcxNDYwMjk4NCwicGF0aCI6Ii82ODg2NjkwLzMyNjI5OTM5Ni1hOWExZjhlNS01MmY4LTRiNGEtODQwZC0xZjM3NjFmNDk4MzkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MDUwMSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDA1MDFUMjIzNjI0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OWFiYzliMDg4MmNlYWUzMWM5OTY5NTYwODc2MWVjMzk0MzkyYmFmM2UzNmVjYTZlY2RlNzEwNTYyN2Y0YjMyNCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.vViiXZoOTHHwb-zt3Qiw983wtA2B_KQTRgeAoco6-XI)

** Or install it to use as a service **

```
pip install 'llama-cpp-python[server]'
```

## Loading the Model
- Downloading model files from Hugging Face - currently using [llama-2-7b-chat.Q4_K_M.gguf](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
- Initializing the model using llama-cpp-python[1]
- Setting context length and other parameters

## Using the API
- High-level Python API for text completion
- OpenAI-like API

```
python3 -m llama_cpp.server --model models/7B/llama-model.gguf
```

The server provides documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

## Stuff I haven't looked at yet
- Performance Considerations
  - Importance of using the correct number of threads[4]
  - Comparing CPU vs GPU performance
  - Quantization and its impact on speed[1]

## Examples and Use Cases
- Running inference on sample prompts
- Integrating llama-cpp-python with other libraries
- Deploying models in standalone apps[5]

## Conclusion
- Recap of llama-cpp-python's key features
- Future developments and roadmap


## Citations:
- [1] Llama.cpp - Outlines 〰️ https://outlines-dev.github.io/outlines/reference/models/llamacpp/
- [2] Python bindings for llama.cpp - GitHub https://github.com/abetlen/llama-cpp-python
- [3] How to Run LLaMA Locally on CPU or GPU - YouTube https://www.youtube.com/watch?v=SvjWDX2NqiM
- [4] Poor performance - How do I use LlamCpp in python correctly ... ggerganov/llama.cpp#6322
- [5] Poll: Why do you choose llama.cpp over vLLM or vice-versa? - Reddit https://www.reddit.com/r/LocalLLaMA/comments/1bub23v/poll_why_do_you_choose_llamacpp_over_vllm_or/

