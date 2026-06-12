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

## Task 3 - Planner Agent Unit Tests

### File

tests/test_planner_agent.py

### Copilot Interaction Method

Generate Unit Tests

### Objective

Use GitHub Copilot to generate unit tests for the planner_agent() function.

### Testing Framework

pytest

### Human Review

Reviewed the generated tests to confirm they check:

* output type
* number of returned learning steps
* empty string handling
* TypeError behavior
* roadmap structure consistency

### Reflection

Generating tests with Copilot helped validate the planner agent's behavior and demonstrated an AI-assisted testing workflow in addition to AI-assisted code generation.

## Task 4 - Resource Agent

### File

agents/resource_agent.py

### Copilot Interaction Method

Plan Mode

### Objective

Generate a curated learning resource recommendation agent.

### Prompting Strategy

Used:

* project context
* structured output requirements
* specific resource URLs
* type hint requirements
* implementation constraints
* explicit resource list
* exact URL preservation requirements

### Outcome

Generated a resource_agent(goal) function that:

* accepts a user goal
* validates input
* returns structured resource recommendations
* includes title, source, url, reason, and how_to_use fields
* incorporates Microsoft Learn, GitHub Copilot, Agents League, and O'Reilly resources
* uses type hints and documentation

### Human Review

Reviewed generated links and updated them to use project-specific resources, including:

* Microsoft Learn Collection
* Microsoft Learn Profile
* Microsoft Agents League Creative Apps Starter Kit
* GitHub Copilot Prompt Engineering Documentation
* GitHub Copilot Code Suggestions Documentation
* Microsoft Learn Copilot Interaction Module
* O'Reilly AI Agents, RAG, and Knowledge Graphs resources

### Reflection

Providing explicit resources and exact URLs significantly improved the relevance and quality of Copilot-generated recommendations. The structured dictionary output is well suited for future integration with the Streamlit user interface.


## Task 5 - Resource Agent Unit Tests

### Copilot Interaction Method
Generate Unit Tests

### Objective
Use GitHub Copilot to generate unit tests for the resource_agent() function.

### Testing Framework
pytest

### Human Review
Reviewed the generated tests to confirm they check output type, required keys, URLs, empty input handling, and TypeError behavior.

### Reflection
Added automated tests for the Resource Agent.

## Task 6 - Creative Agent

### File

agents/creative_agent.py

### Copilot Interaction Method

Plan Mode

### Objective

Generate creative project ideas based on a user's learning or project goal.

### Prompting Strategy

Used:

* project context
* clear agent purpose
* structured output requirements
* type hint requirements
* implementation constraints (no APIs, no LLM calls)

### Outcome

Generated a creative_agent(goal) function that:

* accepts a user goal
* validates input
* returns exactly three project ideas
* structures each idea using:

  * title
  * problem
  * solution
  * why_it_is_creative
* includes type hints and documentation

### Human Review

Reviewed the generated code and verified that:

* output format is consistent across all ideas
* ideas are relevant to the user's goal
* implementation remains deterministic and testable
* code follows the same style as Planner Agent and Resource Agent

### Reflection

Providing clear output requirements resulted in a reusable and well-structured agent. The dictionary-based output will be easy to display in the Streamlit interface and can be expanded later with more personalized idea generation logic.

## Task 7 - Creative Agent Unit Tests

### File

tests/test_creative_agent.py

### Copilot Interaction Method

Generate Unit Tests

### Objective

Use GitHub Copilot to generate unit tests for the creative_agent() function.

### Testing Framework

pytest

### Human Review

Reviewed the generated tests to confirm they check:

* output type
* exactly three project ideas are returned
* each idea is a dictionary
* required fields are present:

  * title
  * problem
  * solution
  * why_it_is_creative
* empty string handling
* TypeError behavior for non-string inputs
* output structure consistency across all ideas

### Reflection

Generating tests with Copilot helped verify that the Creative Agent consistently returns well-structured project ideas. The tests also improved confidence that the agent can be safely integrated into the Streamlit application while maintaining a predictable output format.

## Task 8 - Documentation Agent

### File

agents/documentation_agent.py

### Copilot Interaction Method

Plan Mode

### Objective

Generate documentation recommendations for a project goal.

### Prompting Strategy

Used:

* project context
* structured output requirements
* type hint requirements
* implementation constraints
* documentation-focused categories

### Outcome

Generated a documentation_agent(goal) function that:

* accepts a user goal
* validates input
* returns documentation recommendations
* organizes suggestions into:

  * readme
  * architecture
  * testing
  * references
* includes type hints and documentation

### Human Review

Reviewed the generated code and verified that:

* output structure is consistent
* documentation categories are relevant
* implementation remains deterministic and testable
* code follows the same style as the other agents

### Reflection

Creating a dedicated Documentation Agent reinforces the project's focus on structured development and knowledge sharing. The output can be used directly to guide README creation and future project documentation.

## Task 9 - Documentation Agent Unit Tests

### File

tests/test_documentation_agent.py

### Copilot Interaction Method

Generate Unit Tests

### Objective

Use GitHub Copilot to generate unit tests for the documentation_agent() function.

### Testing Framework

pytest

### Human Review

Reviewed the generated tests to confirm they check:

* output type
* required top-level keys:

  * readme
  * architecture
  * testing
  * references
* each value is a list
* documentation sections are returned in the expected format
* empty string handling
* TypeError behavior for non-string inputs
* output structure consistency

### Reflection

Generating tests with Copilot helped verify that the Documentation Agent consistently returns structured documentation recommendations. The tests also improved confidence that the agent can be integrated into the Streamlit application while maintaining a predictable and reusable output format.
