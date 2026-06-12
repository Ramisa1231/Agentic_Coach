# Learning Log

## Task 1 - Project Scaffolding

### Date

12 June 2026

### Copilot Interaction Method

Plan Agent Mode

### Objective

Create the initial project structure for Agentic Coach.

### Prompting Strategy Used

* Provided project context
* Specified desired folder structure
* Specified file names
* Requested placeholder content only
* Delayed implementation until after review

### Outcome

Copilot generated:

* app.py
* README.md
* requirements.txt
* agents folder
* docs folder
* screenshots folder

### Human Review

Reviewed the proposed structure before implementation and confirmed it aligned with project requirements.

### Reflection

Using Plan Mode first helped establish project architecture before generating code.

## Task 2 - Planner Agent

### File

agents/planner_agent.py

### Copilot Interaction Method

Plan Mode

### Objective

Generate a beginner-friendly roadmap generator.

### Prompting Strategy

Used:

* project context
* function requirements
* output constraints
* type hint requirements

### Outcome

Generated a planner_agent(goal) function that:

* accepts a user goal
* validates input
* returns five ordered learning steps
* includes type hints and documentation

### Human Review

Reviewed the generated code and verified that:

* output format is correct
* roadmap contains exactly five steps
* code remains beginner-friendly

### Reflection

Providing context and output requirements resulted in a useful first implementation with minimal modifications.
