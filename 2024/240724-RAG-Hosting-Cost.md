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
- 100 queries per month (totally made up number)

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

Total - starts at ~$40/month

## Self Hosting UI, Weaviate, LLM

Weaviate documentation recommends 4CPU & 16G RAM.

Approach for LLM is to use llama-cpp-python with a 13b size model on a GPU with 24G RAM.

Easiest approach is to get a GPU VM with enough CPU and System RAM to run the entire stack. Reduces network latency and cost of transfering data.

- Lambda Lab VM 1 GPU	24GB RAM 14 CPU 46G System RAM $0.50/hr ($360/month)
- AWS EC2 P2.xlarge - 1 GPU 12GB RAM 4 CPU 61G System RAM $0.90/hr ($657/month)
- AWS EC2 G5.xlarge - 1 GPU 24G RAM 4 CPU 16G RAM $1.00/hr ($720/month)

## Host at Your House

Assuming solid power, stable internet, and you know how to configure a firewall, reverse proxy, etc:

https://shop.lambdalabs.com/gpu-workstations/vector/customize

![Image](https://shop.lambdalabs.com/static/images/products/vector/vector_front_600.png)

## Absolute Cheapest

Maybe a use case for a quick demonstration capability:

- Web Host with Heroku, DigitalOcean Droplet, or Streamlit public GitHub approach
- Weaviate Free Tier cluster (can run up to 2, expire after 14 days)
- OpenAI API

# Questions, Thoughts, Cries of Heresy?