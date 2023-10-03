![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Llama.cpp and Code Llama

There have been a few updates for Llama.cpp since we covered it last in August. The main change has been a switch from using the GGML format for storing weights and the GGUF format that was implmented.

There's a good reddit thread that covers this here [https://www.reddit.com/r/LocalLLaMA/comments/15xycn2/llamacpp_gguf_merged/](https://www.reddit.com/r/LocalLLaMA/comments/15xycn2/llamacpp_gguf_merged/)

Description of GGUF:
- binary file format for storing models for inference
- designed for fast loading and saving of models
- easy to use (with a few lines of code)
- mmap (memory mapping) compatibility: models can be loaded using mmap for fast loading and saving.

This was really hard to find, so you may want to bookmark it if you really want the details for the GGUF Format - [https://github.com/philpax/ggml/blob/gguf-spec/docs/gguf.md](https://github.com/philpax/ggml/blob/gguf-spec/docs/gguf.md)

Current models in GGUF format on HuggingFace - [https://huggingface.co/models?search=gguf](https://huggingface.co/models?search=gguf)

Really good writeup of the quanization methods available in GGUF - [https://towardsdatascience.com/quantize-llama-models-with-ggml-and-llama-cpp-3612dfbcc172](https://towardsdatascience.com/quantize-llama-models-with-ggml-and-llama-cpp-3612dfbcc172)

# Important

Another item that GGUF enables, but hasn't been discussed much is that the GGUF format is not constrained to llama based models like the GGML format was. There are other architectures being converted to GGUF format and able to run inference with llama.cpp.


