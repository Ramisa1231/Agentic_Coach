"""
Creative Agent

Purpose:
    Generate creative project ideas based on a user goal.

Input:
    User goal (string)

Output:
    List of creative project ideas

Used by:
    Agentic Coach Streamlit application
"""
from typing import Dict, List


def creative_agent(goal: str) -> List[Dict[str, str]]:
    """Generate three creative project ideas to help achieve a user goal.

    Args:
        goal: A short user-stated goal or area to learn (e.g. "build a Streamlit app").

    Returns:
        A list containing exactly three dictionaries. Each dictionary has the
        keys: `title`, `problem`, `solution`, and `why_it_is_creative`.

    Raises:
        TypeError: If `goal` is not a string.

    Notes:
        Implementation is deterministic and simple — suitable for unit testing
        and later enhancement. No external APIs or LLM calls are used.
    """
    if not isinstance(goal, str):
        raise TypeError("goal must be a string")

    # Keep ideas brief and focused; include the user's goal for relevance.
    ideas: List[Dict[str, str]] = [
        {
            "title": f"Mini interactive demo: {goal}",
            "problem": f"Hard to explain what '{goal}' looks like in practice.",
            "solution": (
                f"Build a compact interactive demo that showcases the core idea of '{goal}', "
                "with step-by-step controls and explanatory notes."
            ),
            "why_it_is_creative": (
                "Transforms an abstract goal into a tangible, playable experience, "
                "making learning immediate and shareable."
            ),
        },
        {
            "title": f"Guided micro-course around {goal}",
            "problem": f"Learners need a short, actionable path to practice '{goal}'.",
            "solution": (
                f"Create 3–5 bite-sized lessons or notebooks that teach one concept each, "
                f"ending with a small project that applies '{goal}'."
            ),
            "why_it_is_creative": (
                "Combines learning and creation into repeatable micro-sprints, "
                "reducing friction for beginners."
            ),
        },
        {
            "title": f"Challenge-driven portfolio piece for {goal}",
            "problem": (
                "Beginners struggle to demonstrate skills with a short, meaningful project."
            ),
            "solution": (
                f"Design a challenge with clear constraints inspired by '{goal}', "
                "then build and document the solution as a portfolio entry."
            ),
            "why_it_is_creative": (
                "Frames learning as a design constraint, encouraging inventive solutions "
                "that are easy to evaluate and showcase."
            ),
        },
    ]

    return ideas

