![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# OpenHands Agents for Developing Code

## Overview

- OpenHands provides a suite of AI agents to streamline development workflows.
- Agents can generate code, tests, and perform code reviews.
- Community-driven framework: https://github.com/All-Hands-AI/OpenHands

## Installation

```bash
pip install openhands
```

or:

```bash
pip install git+https://github.com/All-Hands-AI/OpenHands.git
```

## Setup

- Export your OpenHands API key:

```bash
export OH_API_KEY=<YOUR_API_KEY>
```

- Initialize project configuration:

```bash
openhands init
```

## Code Generation Agent

- Generate boilerplate code from natural language prompts.

```bash
openhands agent run code-gen \
  --prompt "Create a Flask API with SQLAlchemy models"
```

## Test Generation Agent

- Automatically create unit tests for existing modules.

```bash
openhands agent run test-gen \
  --path path/to/module.py
```

## Code Review Agent

- Review code and suggest improvements or optimizations.

```bash
openhands agent run review \
  --path path/to/module.py
```

## Custom Agents

- Define custom workflows in `.openhands.yaml`:

```yaml
agents:
  feature-workflow:
    steps:
      - code-gen
      - test-gen
      - review
```

## Resources

- Documentation: https://docs.all-hands.dev/
- GitHub: https://github.com/All-Hands-AI/OpenHands
