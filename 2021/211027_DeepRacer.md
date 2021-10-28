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


1. PPO & why we chose it
    * Parallelizable
    * Easier to Tune
    * Sounds cool - lots of recent papers - most popular at the moment
    * For J - may want to try off policy methods
2. PyTorch Lightning vs Baselines
    * Lightning provides a way to structure in a common way that is modular.
    * Lightning may not work the best for RL
    * Baselines provided an easier way to vectorize environments - turned out to be "not as hard"
    * Really confusing trying to figure out which version of baselines to use - "baselines", "stable baselines", "stable baselines 2", "stable baselines 3"
3. Reward functions and why they are hard
    * Need to determine this early
4. Using evaluation
    * Lightning provides a fit method, but doesn't have a way to stop based on a parameter - need to implement a callback to evaluate.
    * Baselines also has manual callbacks that have to be used.
5. Model checkpoints and saving - why it's hard to say "when"
    * Need to determine this early
6. Submission agent structure
7. Frame stacking?
    * Gives a way to add "motion"
8. Environment provided and scoring function did not match the documented approach.

# Lessons Learned

* Find a way to capture and visualize the inputs early on in the work.
* Don't wait so long to submit something
* Need better monitoring and testing

# Notes

Didn't try this yet, but thought about throwing the image through the edge detection from OpenCV and the straight to the linear layer.

Need to take another look at stopping when done to make sure I wasn't running multiple agents at the same time.
