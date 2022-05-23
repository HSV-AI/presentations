![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# AWS Lambda Function

- Welcome
- Review last week
- Create Lambda Function
- Test Function
- Evaluate Cost
- Questions / Comments
- Close

# Overview

S3 Example [Link](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)


Lambda with Containers [Link](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html)

Uploading Images [Link](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-upload)

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com    
```

That didn't work, so I resorted to creating the container registry through the AWS console.

More info - https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html

I think I need to add a permission to the role that I'm using, so now trying to figure that out. Wound up creating a key related to my admin account and resumed following the tutorial steps.

The initial python function worked fine, but a copy of the python function in the container did not. This was the error, after I figured out how to see it:

```
{
  "errorMessage": "An error occurred (AccessDenied) when calling the GetObject operation: Access Denied",
  "errorType": "ClientError",
  "requestId": "9e85ab7f-9101-48c5-ae68-b8d4e9e67b52",
  "stackTrace": [
    "  File \"/var/task/app.py\", line 22, in handler\n    raise e\n",
    "  File \"/var/task/app.py\", line 16, in handler\n    response = s3.get_object(Bucket=bucket, Key=key)\n",
    "  File \"/var/task/botocore/client.py\", line 508, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",
    "  File \"/var/task/botocore/client.py\", line 911, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"
  ]
  ```

I had to update the permission applied to the lambda function to include S3 read/write. Then I was able to successfully trigger the job.

# Discussion


