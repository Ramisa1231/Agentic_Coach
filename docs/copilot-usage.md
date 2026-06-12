# GitHub Copilot Usage

## Overview

Agentic Coach was developed using GitHub Copilot as an AI-assisted development tool.

The project followed Microsoft Learn and GitHub Copilot best practices, including:

* Plan Mode
* Prompt engineering
* Human review of generated code
* Unit test generation
* Incremental development

All generated code was reviewed before being accepted into the project.

---

## Copilot Interaction Methods Used

### Plan Mode

Plan Mode was used to:

* scaffold the project structure
* create agent implementations
* design the Streamlit application structure
* generate documentation recommendations

### Generate Unit Tests

GitHub Copilot was used to generate unit tests for:

* planner_agent()
* resource_agent()
* creative_agent()
* documentation_agent()

Generated tests were reviewed and refined before execution.

---

## Prompt Engineering Strategy

The project followed several prompt engineering principles:

### 1. Provide Project Context

Example:

```text
Project context:
Agentic Coach is a Microsoft Agents League Creative Apps project.
```

### 2. Define Requirements Clearly

Example:

```text
Requirements:
- Input: string goal
- Output: List[Dict[str, str]]
- Include type hints
- Include docstrings
```

### 3. Specify Constraints

Example:

```text
- No APIs
- No LLM calls
- Keep implementation simple
```

### 4. Request Structured Output

Example:

```text
Return dictionaries containing:
- title
- source
- url
- reason
- how_to_use
```

---

## Agents Developed with Copilot

### Planner Agent

Purpose:

Generate a beginner-friendly learning roadmap.

### Resource Agent

Purpose:

Recommend trusted learning resources.

### Creative Agent

Purpose:

Generate creative project ideas.

### Documentation Agent

Purpose:

Generate documentation recommendations.

---

## Testing Support

GitHub Copilot assisted with:

* test generation
* edge case identification
* input validation testing
* output structure verification

Testing was performed using pytest.

---

## Human Oversight

GitHub Copilot was used as a development assistant rather than an autonomous coding system.

Responsibilities retained by the developer included:

* reviewing generated code
* validating logic
* selecting implementation approaches
* updating project-specific resources and URLs
* testing functionality
* maintaining documentation

---

## Learning Outcomes

Through this project, GitHub Copilot was used to support:

* project planning
* software development
* testing
* documentation
* Streamlit integration

The project demonstrates an AI-assisted development workflow that combines human decision-making with GitHub Copilot's code generation capabilities.
