![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

## AI Huntsville Taskforce

- Moved to the Workforce Development committee - trying to put together a community wide session for April 24th.
- Looking for help evaluating submissions for the AI Track of the Cyber Summit. Please let me know if you are interested.

## HATCH

- [https://devpost.com/software/deep-learning-microscopy-for-dummies](https://devpost.com/software/deep-learning-microscopy-for-dummies)
- [https://github.com/HSV-AI/hatch-2025](https://github.com/HSV-AI/hatch-2025)

## American Planning Association

North Alabama chair reached out, and we're planning a lunch-and-learn session for them on April 25th. We can bring folks from our group to interact, but I need to know who beforehand.

# Agentic AI with HuggingFace

Information in this section is copied directly from the course:

[https://huggingface.co/learn/agents-course/en/unit0/introduction](https://huggingface.co/learn/agents-course/en/unit0/introduction)

```
An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.
```

They use an LLM as the brain:
- Understand natural language: Interpret and respond to human instructions in a meaningful way.
- Reason and plan: Analyze information, make decisions, and devise strategies to solve problems.
- Interact with its environment: Gather information, take actions, and observe the results of those actions.

Does a very good job of giving an overview of:

[What are LLMs?](https://huggingface.co/learn/agents-course/en/unit1/what-are-llms#what-are-llms)

[What are Tools?](https://huggingface.co/learn/agents-course/en/unit1/tools#what-are-tools)

[Think-Act-Observe](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure)

The course goes through a good bit of detail on how an agent calls tools without using a third-party library. We can skip this if we want - [Do it the hard way](https://huggingface.co/learn/agents-course/en/unit1/dummy-agent-library)

Followed the instructions to create a HuggingFace Space with a template agent - [smolagents](https://huggingface.co/learn/agents-course/en/unit1/tutorial)

# Interactive Demo

J's opinion - so far, this is kind of like writing a function and then prompting an LLM to get it to call your function the right way.

Here's the space I created [https://huggingface.co/spaces/J-Period/First_agent_template](https://huggingface.co/spaces/J-Period/First_agent_template) - it's private, so you'll need to make your own.

## Note - if you navigate away from the space, it may be hard to find again.

I created a secret containing my HuggingFace token and cloned the repo for the space. Also had to set up my ssh key to be able to push with git.

After running a few attempts at building my own tool and connecting some other pre-built tools, I ran into a limit of some sort:
```
You have exceeded your monthly included credits for Inference Providers. 
Subscribe to PRO to get 20x more monthly allowance.
```

I exceeded my monthly allowance on the Free tier in about 10 minutes. Researching the options available from HuggingFace leads me to believe that it is not a viable approach for developing and integrating agents.