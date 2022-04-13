![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Self Hosted Runners

- Welcome
- Review
- Self Hosted Runners
- Questions / Comments
- Close

# Overview

- [Product Recommendation repo](https://github.com/HSV-AI/product-recommendation)
- [GitHub Runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
- [Security for Runners?](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#hardening-for-self-hosted-runners)
- [CML for Self Hosted Runners](https://cml.dev/doc/self-hosted-runners)


# Setup

## Permissions

Don't forget to set a budget!!!

[Environment Variables](https://cml.dev/doc/self-hosted-runners#environment-variables)
[EC2 Permissions](https://aws.amazon.com/blogs/security/resource-level-permissions-for-ec2-controlling-management-access-on-specific-instances/)

The EC2 Permissions were a serious pain, and I'm still not sure I did that correctly.


Current pricing:

| Name | GPUs | Price/Hour* |
|-------------|---|-------|
| p2.xlarge | 1 | $0.900 |
| p2.8xlarge | 8 | $7.200 |
| p2.16xlarge | 16 | $14.400 |

| Amazon EC2 | Price (On Demand) | Amazon EMR Price |
|------------|-------------------|------------------|
| m4.large | $0.10 per hour | $0.03 per hour |
| m4.xlarge | $0.20 per hour | $0.06 per hour |
| m4.2xlarge | $0.40 per hour | $0.12 per hour |
| m4.4xlarge | $0.80 per hour | $0.24 per hour |

Currently trying the m4.2xlarge to keep prices down during experimentation.

Trial and error helped determine that you also have to give the runner "DescribeInstances" and "DescribeImages" permissions for EC2.

Actually ran into a weird segfault issue with cml-runner until I relented and added "ALL EC2 PERMISSIONS".

# Discussion


