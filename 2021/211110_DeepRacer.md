![HSV-AI Logo](https://github.com/HSV-AI/hugo-website/blob/master/static/images/logo_v9.png?raw=true)

# NeurIPS 2021 AWS DeepRacer Challenge

This week we will cover our approach to completing the DeepRacer Challenge.

More info on:
* [The Challenge](https://www.aicrowd.com/challenges/neurips-2021-aws-deepracer-ai-driving-olympics-challenge)
* [DeepRacer](https://aws.amazon.com/deepracer/)

# Agenda

Agenda:
- Welcome
- Project Updates
- DeepRacer Challenge
- NeurIPS 2021
- Q&A
- Future Topic Discussion
- Schedule Next Meetup
- Close

[OpenAI Spinning Up with Deep Reinforcement Learning](https://spinningup.openai.com/en/latest)

Types of RL:
![Image](https://spinningup.openai.com/en/latest/_images/rl_algorithms_9_15.svg)

# Discussion

1. Used PPO primarily. Tried DQN and some others, but nothing worked as well.

2. Evaluation criteria was not what was specified.

3. Training environment was also not what was specified.

4. Training environment could be much easier to use and modify.

5. Looked at different commercial use cases of DRL. Might want to look at building better tools for DRL training, evaluation, measurement.

# Lessons Learned

Next time, may want to generate a large sample buffer to preload training and then switch to the environment.
Is there a pytorch tool that will tell me what parts of an image triggered a layer?
Automate feature selection
Don't watch graphs
Automate recording of data
Scale fast

# Notes

There may be some interesting to run different tracks and put together a project for this.

Not able to modify the reward.