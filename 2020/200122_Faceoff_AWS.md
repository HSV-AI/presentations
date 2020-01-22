# Object Recognition Face-off

This week we will start a series of tutorials intended to evaluate different frameworks for object detection. Rather than just looking at the various models for implementation, we will consider the entire framework for deployment.

Agenda:
* Intro & Welcome
* Teams for Hudson Alpha Tech Challenge
* Fast.ai Lesson 1 announcement
* Amazon configuration for object detection

Here are the details on the [2020 Hudson Alpha Tech Challenge](https://www.eventbrite.com/e/2020-hatch-hudsonalpha-tech-challenge-tickets-84916091315?aff=ebdssbdestsearch)

For next week - here's a link to [Lesson 1](https://course.fast.ai/videos/?lesson=1) of the Fast.ai Deep Learning Course.

## Steps from tutorial

Install AWS CLI in a python virtual environment [Instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-virtualenv.html)

Created a user for the AWS CLI.

Set up the CLI following these [instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration)

Clone the sample repository from [Github](https://github.com/aws-samples/amazon-rekognition-reviewing-user-content)

Don't forget to set a budget!!! [Link](https://console.aws.amazon.com/billing/home?region=us-east-1#/budgets)

StackFormation information [here](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks)

## Initial thoughts:

I don't know much about the AWS CloudFormation, but I do know that it's SLOW. This isn't some free tier thing - I'm actually paying for this. So far, I'm over an hour into this setup and CloudFormation has failed twice. Both times for valid reason, but the failure/rollback cycle is taking > 20 minutes each. Then you have to delete the stack manually (after you figure out how to do that) which takes several more minutes before you can try the CloudFormation again.
