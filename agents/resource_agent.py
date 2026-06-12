"""Resource Agent

Purpose:
    Recommend trusted learning resources based on a user goal.

Input:
    User goal (string)

Output:
    List of recommended resources (List[Dict[str, str]])

Used by:
    Agentic Coach Streamlit application
"""

from typing import List, Dict


def resource_agent(goal: str) -> List[Dict[str, str]]:
    """Return seven recommended resources for a user goal.

    Parameters
    ----------
    goal:
        The user's learning or project goal as a short string.

    Returns
    -------
    List[Dict[str, str]]
        Exactly seven resource dictionaries, each with keys: ``title``,
        ``source``, ``url``, ``reason``, and ``how_to_use``.
    """

    if not isinstance(goal, str):
        raise TypeError("goal must be a string")

    goal_text = goal.strip() or "your goal"

    resources: List[Dict[str, str]] = [
        {
            "title": "Microsoft Learn collection",
            "source": "Microsoft Learn",
            "url": "https://learn.microsoft.com/en-gb/collections/3gwqi467467e23/",
            "reason": f"Curated learning paths and modules useful for {goal_text}.",
            "how_to_use": f"Browse the collection and follow a short path related to '{goal_text}'."
        },
        {
            "title": "My Microsoft Learn profile",
            "source": "Microsoft Learn",
            "url": "https://learn.microsoft.com/en-gb/users/syedaramisafariha-1856/",
            "reason": "Personalized learning dashboard showing completed modules and achievements.",
            "how_to_use": "Sign in to review your progress and bookmark modules to support your learning."
        },
        {
            "title": "Microsoft Agents League Creative Apps starter kit",
            "source": "Agents League",
            "url": "https://github.com/microsoft/agentsleague/tree/main/starter-kits/1-creative-apps",
            "reason": "Starter templates and examples for creative agent-based applications.",
            "how_to_use": f"Clone the starter kit and run examples to prototype ideas for '{goal_text}'."
        },
        {
            "title": "GitHub Copilot prompt engineering documentation",
            "source": "GitHub Docs",
            "url": "https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering",
            "reason": "Best practices for writing prompts that produce better Copilot outputs.",
            "how_to_use": f"Apply these prompt patterns when designing prompts for tasks related to '{goal_text}'."
        },
        {
            "title": "GitHub Copilot code suggestions documentation",
            "source": "GitHub Docs",
            "url": "https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/completions/code-suggestions",
            "reason": "Official guidance on Copilot's code completion and suggestion features.",
            "how_to_use": f"Use the documentation to configure and interpret Copilot suggestions while building '{goal_text}'."
        },
        {
            "title": "Microsoft Learn: Interacting with GitHub Copilot",
            "source": "Microsoft Learn",
            "url": "https://learn.microsoft.com/en-gb/training/modules/introduction-to-github-copilot/3-interacting-with-copilot",
            "reason": "A hands-on module that demonstrates practical Copilot interaction patterns.",
            "how_to_use": f"Complete the module to learn workflows you can apply when developing features for '{goal_text}'."
        },
        {
            "title": "O'Reilly book on AI agents, RAG, and knowledge graphs",
            "source": "O'Reilly Media",
            "url": "https://www.oreilly.com/",
            "reason": "Responsive, in-depth coverage of agent design, retrieval-augmented generation (RAG), and knowledge graphs.",
            "how_to_use": f"Read chapters on agents and RAG to inform architecture decisions for '{goal_text}'."
        }
    ]

    return resources
