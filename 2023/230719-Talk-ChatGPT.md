![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# Now for the talk...

There are several reasons to want something like a ChatGPT in your own company. We don't have to go through all of those tonight - we'll just note that some projects in town operate on data that they can't send to a ChatGPT API.

If you were able to obtain a copy of ChatGPT (you can't, but use your imagination):

- Inference time can be somewhere along the lines of 5 seconds, so if you plan to serve multiple users, you would also need to build a mechanism to queue requests (assuming a single model execution)

- About that model execution - with 175B parameters, you would need (4x175B=) 700GB of GPU RAM  to run inference. Current pricing on nVidia A100 (64GB each) would come in around $250k based on a quick internet estimate for a system to set up 12 in a cluster format.

​------

An alternative approach is to build a similar capability with a smaller size model that is fine tuned for the specific domain.

A good starting point for model selection and evaluation is the HuggingFace OpenLLM leaderboard - https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

The "Open" in OpenLLM means that the model weights are available for download. You can then fine tune (if needed) and deploy these models on your own hardware.

The larger OpenLLM models seem to have converged somewhere between 30B and 60B parameters.

You will also need to take into account the license that the model is released under. Some are released under the Apache license - Falcon and MPT, while others are released under a strict non-commercial license (LLaMA, Alpaca).

In addition to the models themselves, you would need to be aware of the licensing that applies to any dataset that you intend to use for fine-tuning the model.

# What ChatGPT says to talk about:

Slide 1: Title: Exploring ChatGPT: Empowering Conversational AI within Your Company

Slide 2: Introduction: - Briefly introduce the topic of the overall event, focusing on ChatGPT as the central subject. - Highlight the purpose of the presentation: to shed light on what ChatGPT does and how it can be utilized effectively.

Slide 3: The Need for ChatGPT in Your Company: - Emphasize the importance of having a ChatGPT-like system within an organization. - Mention that certain projects might deal with sensitive data that cannot be shared with external ChatGPT APIs.

Slide 4: Challenges of Implementing ChatGPT In-House: - Discuss the inference time associated with ChatGPT, noting that it can take around 5 seconds. - Highlight the necessity of implementing a request queue mechanism when serving multiple users simultaneously.

Slide 5: Challenges of Implementing ChatGPT In-House (contd.): - Explain the resource requirements, specifically the substantial GPU RAM needed (700GB for a 175B parameter model). - Provide a rough estimate of the cost involved in setting up a cluster-based system to accommodate these requirements.

Slide 6: Exploring Alternative Approaches: - Propose the use of smaller-sized models that are fine-tuned for specific domains as an alternative to the large ChatGPT model. - Discuss the advantages of this approach, including reduced resource requirements and faster inference times.

Slide 7: Exploring Alternative Approaches (contd.): - Mention that model selection and evaluation can be facilitated through the HuggingFace OpenLLM leaderboard. - Provide a link to the leaderboard for reference.

Slide 8: The HuggingFace OpenLLM Leaderboard: - Highlight the OpenLLM leaderboard as a valuable resource for model selection and evaluation. - Emphasize that the "Open" in OpenLLM signifies the availability of model weights for download and deployment on your own hardware.

Slide 9: The HuggingFace OpenLLM Leaderboard (contd.): - Mention the importance of considering the licensing associated with different models, distinguishing between Apache and non-commercial licenses.

Slide 10: Licensing Considerations: - Explain the significance of understanding the licensing terms applied to the models used in your organization. - Provide examples of different licenses, such as the Apache license for models like Falcon and MPT, and non-commercial licenses like LLaMA and Alpaca.

Slide 11: Licensing Considerations (contd.): - Stress the need to be mindful of dataset licensing when fine-tuning models.

Slide 12: Conclusion: - Recap the key points discussed, including the benefits of implementing ChatGPT in-house and the challenges associated with resource requirements. - Encourage attendees to explore alternative approaches and leverage the OpenLLM leaderboard for model selection and evaluation. - Emphasize the importance of considering licensing terms for both models and datasets used in fine-tuning. - Conclude by highlighting the potential for conversational AI to enhance and empower companies in their respective domains.