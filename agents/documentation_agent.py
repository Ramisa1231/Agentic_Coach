"""
Documentation Agent

Purpose:
    Generate documentation recommendations for a user goal.

Input:
    User goal (string)

Output:
    Documentation suggestions

Used by:
    Agentic Coach Streamlit application
"""
from typing import Dict, List


def documentation_agent(goal: str) -> Dict[str, List[str]]:
    """Generate simple documentation section suggestions for a project goal.

    Args:
        goal: A short user-stated goal or project description.

    Returns:
        A dictionary mapping section categories to ordered lists of section
        headings or checklist items. Keys returned:
        - 'readme'
        - 'architecture'
        - 'testing'
        - 'references'

    Raises:
        TypeError: If `goal` is not a string.

    The implementation is intentionally simple and deterministic to support
    unit testing and later enhancement.
    """
    if not isinstance(goal, str):
        raise TypeError("goal must be a string")

    readme: List[str] = [
        f"Project: {goal}",
        "Short Description",
        "Getting Started / Installation",
        "Usage Examples",
        "Configuration",
        "Contributing",
        "License",
    ]

    architecture: List[str] = [
        "Architecture Overview",
        "High-level Components",
        "Data Flow and Interfaces",
        "Deployment Diagram",
        "Security and Permissions",
    ]

    testing: List[str] = [
        "Unit tests (what to test and where)",
        "Integration tests (critical paths)",
        "Manual and exploratory testing checklist",
        "How to run tests (commands)",
        "Test data and fixtures",
    ]

    references: List[str] = [
        "Relevant tutorials and walkthroughs",
        "API / library docs (if applicable)",
        "Design references and inspiration",
        "Glossary of terms",
    ]

    return {
        "readme": readme,
        "architecture": architecture,
        "testing": testing,
        "references": references,
    }


