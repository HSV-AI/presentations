![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Welcome

- Vision
- Mission
- How to Connect - [Signup](https://hsv.ai/subscribe)

# OpenHands Agents for Developing Code

## Architecture of OpenHands CodeAgent

![OpenHands CodeAgent Architecture](https://docs.all-hands.dev/assets/codeagent_architecture.png)

The CodeAgent is designed as a modular microservices architecture:

- **CLI Interface**: User-facing `openhands` command-line tool.
- **Orchestrator Service**: Coordinates workflows, state management, and step execution.
- **LLM Integrations**: Plugins for OpenAI GPT models, Hugging Face inference, and local LLMs.
- **Tool Plugins**: Extensible modules for code analysis, test generation, and version control.
- **Runtime Sandbox**: Isolated environment for executing generated code safely.
- **Monitoring & Logging**: Tracks execution traces, performance metrics, and audit logs.

### Tool Plugins Details

- **FileSystemTool**: Read and write files in the project workspace.
- **PythonREPLTool**: Execute Python code in an isolated Python REPL for quick testing and validation.
- **ShellTool**: Run shell commands (e.g., `pip install`, `git diff`) to manage dependencies and version control.
- **GitTool**: Automate Git operations, including staging, committing, and pushing code changes.
- **LinterTool**: Run code formatters and linters (e.g., `black`, `flake8`) to enforce style guidelines.
- **TestRunnerTool**: Execute test suites (e.g., `pytest`) and report coverage and failures.
- **DiffTool**: Generate diffs and patches to review changes before applying.

### Example LLM Prompts

The CodeAgent generates prompts to interact with the LLM based on the selected tool or agent workflow. Some examples include:

- **Code Generation**:
  ```
  You are a senior Python engineer. Create a Flask API with SQLAlchemy models for a User and Post resource. Include CRUD endpoints, validation, and JSON-based responses.
  ```
- **Test Generation**:
  ```
  Generate pytest unit tests for the module at `path/to/module.py`. Cover standard operations and edge cases; mock external dependencies where necessary.
  ```
- **Code Review**:
  ```
  Perform a thorough code review on the following file: `path/to/module.py`. Identify bugs, security issues, performance improvements, and ensure PEP8 compliance.
  ```


## History and Collaborators

- **2024 Q1**: Kickoff by All-Hands AI to leverage AI for code development workflows.
- **2024 Q2**: Integrated OpenAI GPT via the Copilot API for code generation and review.
- **2024 Q3**: Added support for Hugging Face Inference API and community-driven local LLMs.
- **2024 Q4**: Open-sourced the framework under MIT License on GitHub with community contributions.
- **Primary contributors and collaborators**:
  - **All-Hands AI**: Core framework architecture and orchestration.
  - **OpenAI**: Language model services and API integration.
  - **Hugging Face**: Hosted and on-premise LLM support.
  - **Microsoft/GitHub**: Version control integrations including GitHub Copilot and Codespaces.
  - **Weights & Biases**: Experiment tracking and monitoring integrations.


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

