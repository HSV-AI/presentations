![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

## AI Huntsville Taskforce

- Intro to AI community session moved to May 15. Next session tentatively in August.
- Looking for people to volunteer on a commitee to plan next year's AI Symposium.

## American Planning Association

North Alabama chair reached out, and we're planning a lunch-and-learn session for them on April 25th. We can bring folks from our group to interact, but I need to know who beforehand.

## Alabama Launchpad

- https://www.linkedin.com/posts/sr123456789_alabamalaunchpad-huntsvillestartups-innovationinal-activity-7317720461193216000-Ssap

# Agent Platforms

Reminder from our previous session on AI Agents:
```
An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.
```

**Opinion** - There is no clear architecture for these frameworks or which approach to start with. It appears that they all intertwine with each other, possibly with the exception of MCP. 

**Opinion** I believe that some of these platforms exist only to drive people to develop products using their hosted inference offerings. I'm looking at you HuggingFace :) Others exist to drive people to their hosting platform (LangGraph) or tracing tools (LangSmith, Llamatrace)

Other companies such as Weights and Biases have also built integrations to help trace through the steps taken by AI Agents for use in debuging or auditing.

## Hugging Face smolagents

The Hugging Face approach is a bit strange. It depends on the documentation you provide when defining your tools and agents and hopes that the underlying LLM will make good choices. 

https://huggingface.co/docs/smolagents/en/index

## LlamaIndex

LlamaIndex seems to be best suited for data ingestion and indexing - go figure! It has a massive amount of predefined tools to ingest data from several platforms and most common document types.

**Opinion** - This still feels more like search, chat, RAG, or Deep Research type of activity than an agent working on my behalf.

https://www.llamaindex.ai/

https://docs.llamaindex.ai/en/stable/examples/workflow/workflows_cookbook/

## LangChain

LangChain has a few nice items, including some type of workflow generation GUI that I haven't had time to try yet. It may be the most commercial ready platform for quickly creating and hosting AI Agents.

https://www.langchain.com/

## Model Context Protocol (MCP)

https://modelcontextprotocol.io/introduction

## Agent to Agent (A2A)

https://google.github.io/A2A/#/