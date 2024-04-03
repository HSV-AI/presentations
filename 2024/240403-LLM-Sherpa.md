![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# LLM Sherpa

When building the initial SpaceApps submission, we attempted to split the PDFs into paragraphs using PyPDF, but came up short of anything useful. It provided nearly the same text that we get from the NASA API. For example:

```Theoretical models of star formation do not provide a complete account of the evolution of```

So when we started working on the update of the app, I took another look at potential ways to split a PDF into paragraphs or other manageable chunks. Along those lines, I came across LLM-Sherpa - which is released under the Apache 2.0 license.

As it turns out, LLM Sherpa is very similar to something I built many years ago at CohesionForce for a similar task of chunking PDFs and other documents. It's a web wrapper around the Apache Tika library, with some additional modifications. This means that the chunking is done in Java instead of pure python - making it much faster.

The key here is that LLM Sherpa provides the wrapped Apache Tika library that can run as a container along with a python libary to interface directly with it.

The best way to get started is by going directly to the source: [LLM Sherpa](https://github.com/nlmatics/llmsherpa)

The documentation for LLM Sherpa leads down a path using LLamaIndex and OpenAI APIs, but we will just use the direct chunking capability and stop at that point.