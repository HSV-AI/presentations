![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)


# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Weaviate Setup

- Create an account
- Create a sandbox (valid for 14 days) on the free tier
- Install the weaviate python library
- Find the url and api key for your cluster

# Quickstart

It looks like weaviate doesn't have a way to get_or_create a collection. Instead, we may have to check for an existing and then create if we don't find one.

Initially had a problem with the gprc call for inserting object timing out. Had to figure out how to update the Configuration of the client to add timeout values. Assuming these are in seconds, since the documentation doesn't specify the unit of measure.

[Quickstart](https://weaviate.io/developers/weaviate/quickstart)