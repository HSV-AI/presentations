![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Private RAG Hosting & Cost

We have been covering a series this year based on how a RAG works, and how to build one. Now it's time to look at what it will cost to deploy it!

We will start with a basic use case with using OpenAI GPT4o and a Weaviate hosted vector store. We will move from there to a self hosted solution for all of the components and add up the month cost associated.

## Reference Points

- 490 NASA Documents
- 16,452 Chunks (Paragraph size)
- 4,921,201 Words
- ~300 words / chunk
- Embedding size of 384
- Prompt for LLM consists of:
  - 100 word system prompt
  - 10 x 300 word chunk context
  - ~ 3600 total word prompt
- 1.3 tokens per word

## Pure Webhost / OpenAI / Weaviate

Weaviate $0.095 per 1M dimensions per month
- 16,452 chunks x 384 / 1,000,000 x $0.095 = $0.60 / month
- Minimum is $25 / month
- Break even is around 685k chunks

OpenAI Pricing for GPT4o is $5 / 1M input tokens and $15 / 1M output tokens.
- Assuming the output is of similar size to the total prompt:
- (3600 * 1.3 / 1M * $5) + (3600 * 1.3 / 1M * $15)
- Total is $0.0936 per query

Web Host:
- Digital Ocean - $5/month
- Heroku - $7/month
- AWS Lightsail - $5/month