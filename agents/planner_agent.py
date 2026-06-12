"""
Planner Agent

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
    """Convert a user's learning or project goal into a beginner-friendly roadmap.

    Args:
        goal: A short user-stated goal or area to learn (e.g. "build a Streamlit app").

    Returns:
        A list of exactly five short, ordered learning steps (List[str]).

    Raises:
        TypeError: If `goal` is not a string.

    Example:
        >>> planner_agent("build a simple Streamlit app")
        ['Clarify the goal and success criteria', 'Learn the fundamental concepts',
         'Follow a small guided tutorial and build a mini-project',
         'Use developer tools and libraries to expand the project',
         'Practice, iterate, and document what you learned']
    """
    if not isinstance(goal, str):
        raise TypeError("goal must be a string")

    # Keep the implementation simple and deterministic. The same five-step
    # structure works for most beginner goals.
    steps: List[str] = [
        "Clarify the goal and define simple success criteria",
        "Learn the fundamental concepts and vocabulary",
        "Follow a short tutorial and build a focused mini-project",
        "Explore useful tools, libraries, and debugging techniques",
        "Practice, iterate on the project, and write a short summary",
    ]

    return steps
