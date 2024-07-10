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

With the main takeaways being that keeping the instructions at the bottom of the prompt is generally a good idea.

Staying away from the max context size is also a good idea.

# More information

- OpenAI Discussion - https://community.openai.com/t/prompt-engineering-for-rag
- Prompt Engineering Guide - https://www.promptingguide.ai/
- OpenAI Cookbook - https://cookbook.openai.com/ (Did not find this to be very useful)

# Examples for Tonight

## Global Warming

```
You are a helpful, respectful and honest assistant. Always answer
as helpfully as possible, while being safe. Your answers should not include any harmful, 
unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your
responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of 
answering something not correct. If you don't know the answer to a question, please don't share 
false information.

Generate the next agent response by answering the question. Answer it as succinctly as possible. 
You are provided several documents with titles. If the answer comes from different documents 
please mention all possibilities in your answer and use the titles to separate between topics 
or domains. If you cannot answer the question from the given documents, please state that you 
do not have an answer.

CONTEXT:

Reference 1: According to the Intergovernmental Panel on Climate Change (IPCC) 2021 report, climate change is expected to reduce crop yields significantly due to increased temperatures, changes in precipitation patterns, and more frequent extreme weather events (IPCC, 2021).

Reference 2: A study published in Nature in 2020 highlights that regions like Sub-Saharan Africa and South Asia are particularly vulnerable to climate change impacts on agriculture, potentially leading to food insecurity (Smith et al., 2020).

Reference 3: The Food and Agriculture Organization (FAO) states that climate change will exacerbate existing challenges in agricultural productivity and food security, with smallholder farmers being the most affected (FAO, 2019).

Reference 4: Research by the United States Department of Agriculture (USDA) indicates that rising CO2 levels can have both positive and negative effects on crop growth, but the overall impact is expected to be negative due to the associated changes in climate (USDA, 2020).

Reference 5: The Journal of Agricultural and Environmental Ethics published an article in 2021 discussing the ethical implications of climate change on agriculture, emphasizing the need for adaptive strategies to support vulnerable populations (Brown et al., 2021).

Reference 6: According to a report by the World Bank, investment in climate-resilient agricultural practices is crucial to mitigate the adverse effects of climate change on food production (World Bank, 2021).

Reference 7: A 2018 report from the National Aeronautics and Space Administration (NASA) discusses how satellite data is being used to monitor the effects of climate change on agricultural land and to inform policy decisions (NASA, 2018).

Reference 8: An article in Global Environmental Change (2019) highlights that traditional agricultural practices and knowledge can play a vital role in adapting to climate change (Jones et al., 2019).

QUESTION:
how is climate change expected to impact global agriculture, and what measures can be taken to mitigate these effects?
```

## Eiffel Tower

```
CONTEXT:
[1] The Eiffel Tower, constructed in 1889, stands 324 meters tall and was designed by Gustave Eiffel. It was built as the entrance arch for the 1889 World's Fair in Paris.
[2] The tower's construction took 2 years, 2 months, and 5 days, involving 300 workers and 2.5 million rivets. It was the world's tallest man-made structure until 1930.
[3] Initially criticized by some of France's leading artists and intellectuals, the Eiffel Tower has become a global cultural icon of France and one of the most recognizable structures in the world.
[4] The tower receives about 7 million visitors annually, making it the most-visited paid monument globally. It has three levels for visitors, with restaurants on the first and second levels.

INSTRUCTIONS:

Answer the question using ONLY the information provided in the CONTEXT above.
Cite your sources using bracketed numbers at the end of relevant sentences, like this [1].
If the answer to any part of the question is not in the CONTEXT, state that the information is not provided.
Provide a concise, factual response without additional commentary.
Do not use phrases like "According to the context" or "The provided information states." Simply present the facts with citations.

QUESTION:
Why is the Eiffel Tower so popular?
```