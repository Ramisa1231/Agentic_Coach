"""Planner Agent

Purpose:
	Generate a beginner-friendly learning roadmap from a user goal.

Input:
	User goal (string)

Output:
	Five ordered learning steps (List[str])

Used by:
	Agentic Coach Streamlit application
"""

from typing import List


def planner_agent(goal: str) -> List[str]:
	"""Convert a user learning/project goal into a 5-step beginner roadmap.

	Parameters
	----------
	goal:
		A short description of the user's learning or project goal.

	Returns
	-------
	List[str]
		Exactly five short, ordered steps a beginner can follow.

	Example
	-------
	>>> planner_agent("build a personal website")
	[
		'Clarify the goal: define the scope and success criteria for "build a personal website".',
		'Learn fundamentals: study basic HTML, CSS, and responsive layout principles.',
		'Hands-on: build a simple multi-page site and host it using GitHub Pages or similar.',
		'Tools & resources: learn Git, a code editor, and deploy workflows; follow tutorials.',
		'Next steps: iterate with new features (contact form, blog), and practice regularly.'
	]
	"""

	if not isinstance(goal, str):
		raise TypeError("goal must be a string")

	goal_text = goal.strip()
	if not goal_text:
		goal_text = "your goal"

	# Build five clear, beginner-focused steps. Keep sentences short and actionable.
	steps: List[str] = [
		f'Clarify the goal: define the scope and success criteria for "{goal_text}".',
		'Learn fundamentals: study the core concepts and basics needed for this area.',
		f'Hands-on: create a small beginner project focused on "{goal_text}" to apply what you learned.',
		'Tools & resources: gather tutorials, documentation, and simple tools to speed learning.',
		'Practice & next steps: iterate on your project, get feedback, and pick extensions to master.'
	]

	return steps


