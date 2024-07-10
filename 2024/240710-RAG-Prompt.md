![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Prompt Engineering for RAG

If you have ever tried to prompt an LLM to give you what you want, you have probably run into some frustrating challenges. This can range from trying to write what you want in pseudo-code to arguing with a child about putting their toys away.

This week we will focus on some guidelines for building successful prompts for a RAG system. There is a lot of art and craft associated, and the answer to most questions is "it depends". To help understand this better, we will pull back the curtain about and talk about WHY certain prompts are effective and what types of situations they may apply to.

## Base model vs Instruct model

Many AI years ago (a few months), the best approach was to use an Instruct version of an LLM. These were base LLM models that have been fine-tuned to more precisely follow instructions. As LLMs have become larger and more complex, they are usually able to follow instructions as well as the instruct versions, and do not require the same level of formatting in the prompt.

Here's an example from the Prompt Engineering Guide: 
https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-rag.ipynb

There are a few interesting things to pick up from the example:
- Keyword Substitution
- Control Flow Logic (looping over a set of inputs)

# Differences between models

For most of what I have tried to do with GPT4o and GPT3.5, I have not seen too many differences with prompt structure. I have seen some changes with using a local llama-7b quantized model though.

# Basic RAG Prompt

Here is the basic RAG prompt that I have put together after scouring the web, discord, and other scary places:

```
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

Generate the next agent response by answering the question. Answer it as succinctly as possible. You are provided several documents with titles. If the answer comes from different documents please mention all possibilities in your answer and use the titles to separate between topics or domains. If you cannot answer the question from the given documents, please state that you do not have an answer.
```

Here's another prompt that expects to have CONTEXT above it. I have found that this causes issues if the CONTEXT is provided below instead. It also includes negative statements, which can be used to remove some of the usual "AI Generated" tone for answers.
```
Answer the question using ONLY the information provided in the CONTEXT above. Cite your sources using bracketed numbers at the end of relevant sentences, like this [1].
If the answer to any part of the question is not in the CONTEXT, state that the information is not provided.
Provide a concise, factual response without additional commentary.

Do not use phrases like "According to the context" or "The provided information states." Simply present the facts with citations.
```

# Recency

There's also a concept of recency with LLMs that can affect how you may want to prompt:

![Image](https://global.discourse-cdn.com/openai1/original/4X/1/f/9/1f9966765542ec3c75516cb30968e80d5f42adab.jpeg)

# More information

- OpenAI Discussion - https://community.openai.com/t/prompt-engineering-for-rag
- Prompt Engineering Guide - https://www.promptingguide.ai/
- OpenAI Cookbook - https://cookbook.openai.com/ (Did not find this to be very useful)
