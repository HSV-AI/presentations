![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# AI Workloads with Runpod

## Current AWS Architecture - Whiteboard

## Why Leave AWS?

- Cost
- GPU Workers

## Interface Similarity

Lambda:
```python
def lambda_handler(event, context):
    
    # Get the length and width parameters from the event object. The 
    # runtime converts the event object to a Python dictionary
    length = event['length']
    width = event['width']
    
    area = calculate_area(length, width)
    print(f"The area is {area}")
        
    logger.info(f"CloudWatch logs group: {context.log_group_name}")
    
    # return the calculated area as a JSON string
    data = {"area": area}
    return json.dumps(data)
```

Runpod:
```python
def handler(event):
#   This function processes incoming requests to your Serverless endpoint.
#
#    Args:
#        event (dict): Contains the input data and request metadata
#       
#    Returns:
#       Any: The result to be returned to the client
    
    # Extract input data
    print(f"Worker Start")
    input = event['input']
    
    prompt = input.get('prompt')  
    seconds = input.get('seconds', 0)  

    print(f"Received prompt: {prompt}")
    print(f"Sleeping for {seconds} seconds...")
    
    # You can replace this sleep call with your own Python code
    time.sleep(seconds)  
    
    return prompt 
```

Use Docker with both, so no big deal there

## Endpoint Configuration - Demonstration

## Variables (Exposed vs Secure) - Demonstration

## Cold Start Time

- With AWS (Fargate or Lambda) this was measured in minutes, occasionally up to 5 minutes.
- With Runpod, this is measured in seconds - with an option to keep workers active for a period of time after they complete.

## Community

- Very active Discord server
- Lots of pre-built workers for many tasks

## Negatives

- No global budget for auto-pay
- Very limited Terraform or CI/CD integration
- Logging