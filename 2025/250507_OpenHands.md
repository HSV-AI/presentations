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

## GitHub Actions Integration

Add the following workflow to `.github/workflows/openhands-fix.yml` to automatically run OpenHands agents on pull requests and apply code fixes:

```yaml
name: OpenHands Code Fix

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  openhands-fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install OpenHands
        run: pip install openhands
      - name: Run OpenHands Code Review and Fix
        run: |
          openhands agent run review --path . --fix
        env:
          OH_API_KEY: ${{ secrets.OH_API_KEY }}
      - name: Commit and Push Fixes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add .
          git commit -m "Apply OpenHands code fixes" || echo "No changes to commit"
          git push
```

Ensure that `OH_API_KEY` is set in your repository secrets and the workflow file is located under `.github/workflows/`.

