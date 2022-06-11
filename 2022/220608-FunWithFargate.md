![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# AWS Fargate

- Welcome
- Review last week
- Create Lambda Function
- Test Function
- Evaluate Cost
- Questions / Comments
- Close

# Overview

**Agenda:**

- Welcome
- Fun with Fargate
- Lambda Containers & AWS Container Registry
- Test & Evaluate Cost

Things you have to know to get Fargate up and working:

1. Docker & Containers
2. AWS ECR
3. VPC
4. Availability Regions
5. Subnets
6. CIDR
7. Internet Gateways
8. Route Tables
9. Security Groups
10. Load Balancers
11. Access Control List (ACL)
12. Endpoints
13. Clusters
14. Task Definitions
15. Services
16. Tasks
17. Target Groups
18. AIM Roles
19. AIM Permissions

# Diagram of Pieces

![Image](https://github.com/HSV-AI/presentations/raw/master/2022/fargate2.drawio.png)

# Cost

Several of the items above have a cost associated with them, which might not be apparent from an initial observation.

- AWS ECR - 0.10 per GB-month of data storage
- Fargate / ECS - CPU & Memory time
- Cloudwatch
- Data Transfer
- Load Balancing
  - $0.008 per used Application load balancer capacity unit-hour (or partial hour)
  - $0.0225 per Application LoadBalancer-hour (or partial hour)
- Lambda
- S3
- VPC
  - $0.01 per GB for upto 1 PB monthly data processed by VPC Endpoints
  - $0.01 per VPC Endpoint Hour

# Discussion


