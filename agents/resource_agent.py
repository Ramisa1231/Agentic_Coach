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


def _detect_goal_category(goal: str) -> str:
    """Detect the learning goal category using simple keyword matching.
    
    Args:
        goal: The user's goal string (case-insensitive matching).
        
    Returns:
        One of: 'ai_engineer', 'software_developer', 'product_owner', 
        'data_analyst', 'cybersecurity', or 'general'.
    """
    goal_lower = goal.lower()
    
    # AI Engineer keywords
    if any(kw in goal_lower for kw in ['ai', 'machine learning', 'ml', 'neural', 'deep learning', 'transformer', 'llm', 'agent']):
        return 'ai_engineer'
    
    # Software Developer keywords
    if any(kw in goal_lower for kw in ['app', 'software', 'code', 'development', 'backend', 'frontend', 'full stack', 'api', 'database']):
        return 'software_developer'
    
    # Product Owner keywords
    if any(kw in goal_lower for kw in ['product', 'strategy', 'roadmap', 'business', 'user experience', 'ux', 'feature', 'requirement']):
        return 'product_owner'
    
    # Data Analyst keywords
    if any(kw in goal_lower for kw in ['data', 'analytics', 'sql', 'visualization', 'insight', 'report', 'dashboard', 'excel', 'tableau', 'power bi']):
        return 'data_analyst'
    
    # Cybersecurity keywords
    if any(kw in goal_lower for kw in ['security', 'cyber', 'encryption', 'penetration', 'vulnerability', 'firewall', 'network security', 'hacking']):
        return 'cybersecurity'
    
    return 'general'


def resource_agent(goal: str) -> List[Dict[str, str]]:
    """Return recommended resources for a user goal.

    Returns the 7 core resources plus 3 goal-specific resources based on the detected category.
    May return more than 7 resources depending on the goal.

    Parameters
    ----------
    goal:
        The user's learning or project goal as a short string.

    Returns
    -------
    List[Dict[str, str]]
        Resource dictionaries with keys: ``title``, ``source``, ``url``, ``reason``, 
        and ``how_to_use``. Includes all 7 core resources plus 3 goal-specific resources
        (total: 10 resources).
    """

    if not isinstance(goal, str):
        raise TypeError("goal must be a string")

    goal_text = goal.strip() or "your goal"

    # Core resources - always included (exactly as specified)
    core_resources: List[Dict[str, str]] = [
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

    # Goal-specific resources
    category = _detect_goal_category(goal)
    
    goal_specific_map = {
        'ai_engineer': [
            {
                "title": "Fast.ai: Practical Deep Learning for Coders",
                "source": "fast.ai",
                "url": "https://course.fast.ai/",
                "reason": "Top-down approach to deep learning with PyTorch; learn by building projects first.",
                "how_to_use": "Start with lesson 1, code along, and build a project at each step."
            },
            {
                "title": "Papers with Code",
                "source": "Papers with Code",
                "url": "https://paperswithcode.com/",
                "reason": "Browse cutting-edge ML research papers paired with open-source implementations.",
                "how_to_use": "Pick a paper that interests you, read the abstract, find the code, and experiment with it."
            },
            {
                "title": "Hugging Face Model Hub",
                "source": "Hugging Face",
                "url": "https://huggingface.co/models",
                "reason": "Pre-trained models for NLP, vision, and audio; use them directly or fine-tune them.",
                "how_to_use": "Search for a task, load a model in 3 lines of code, and start experimenting."
            },
        ],
        'software_developer': [
            {
                "title": "Eloquent JavaScript (free online book)",
                "source": "Eloquent JavaScript",
                "url": "https://eloquentjavascript.net/",
                "reason": "Comprehensive guide to JavaScript fundamentals, DOM, and asynchronous programming.",
                "how_to_use": "Read chapters in order, try all interactive examples, and complete the exercises."
            },
            {
                "title": "Stack Overflow",
                "source": "Stack Overflow",
                "url": "https://stackoverflow.com/",
                "reason": "Searchable Q&A for common coding problems; most questions are already answered.",
                "how_to_use": "Search for your error message or use case; read multiple answers to understand trade-offs."
            },
            {
                "title": "Refactoring Guru: Design Patterns",
                "source": "Refactoring Guru",
                "url": "https://refactoring.guru/design-patterns",
                "reason": "Visual, interactive guide to software design patterns with code examples.",
                "how_to_use": "Learn one pattern per project and apply it to improve your architecture."
            },
        ],
        'product_owner': [
            {
                "title": "Inspired: How to Create Digital Products That Customers Love",
                "source": "Book by Marty Cagan",
                "url": "https://www.amazon.com/Inspired-Create-Products-Customers-Love/dp/0134461924",
                "reason": "Industry-leading framework for product strategy, discovery, and team dynamics.",
                "how_to_use": "Read one chapter per week and apply concepts to your product roadmap."
            },
            {
                "title": "The Lean Product Playbook",
                "source": "Book by Dan Olsen",
                "url": "https://leanproductplaybook.com/",
                "reason": "Practical guide to validating ideas and achieving product-market fit.",
                "how_to_use": "Use the Lean Product Canvas to define your hypothesis and test it with users."
            },
            {
                "title": "Product Hunt",
                "source": "Product Hunt",
                "url": "https://www.producthunt.com/",
                "reason": "See what's launching today; study successful product launches and community feedback.",
                "how_to_use": "Browse daily launches, read comments, and analyze why certain products gain traction."
            },
        ],
        'data_analyst': [
            {
                "title": "SQL Tutorial by Mode Analytics",
                "source": "Mode Analytics",
                "url": "https://mode.com/sql-tutorial/",
                "reason": "Interactive, beginner-friendly SQL guide with hands-on practice queries.",
                "how_to_use": "Complete all lessons; spend extra time on JOINs and GROUP BY, the foundations of data analysis."
            },
            {
                "title": "Tableau Public Gallery",
                "source": "Tableau",
                "url": "https://public.tableau.com/",
                "reason": "Thousands of public dashboards; study design patterns and best practices.",
                "how_to_use": "Find dashboards in your industry, reverse-engineer them, and build something similar."
            },
            {
                "title": "Kaggle",
                "source": "Kaggle",
                "url": "https://www.kaggle.com/",
                "reason": "Datasets, competitions, and notebooks (code) for hands-on data analysis practice.",
                "how_to_use": "Start with an easy competition, study top solutions, and replicate their approach."
            },
        ],
        'cybersecurity': [
            {
                "title": "OWASP Top 10 and WebGoat",
                "source": "OWASP",
                "url": "https://owasp.org/www-project-top-ten/",
                "reason": "The 10 most critical web security risks; educational project for practicing attacks.",
                "how_to_use": "Study each vulnerability in the Top 10 and learn how to exploit and defend against it."
            },
            {
                "title": "HackTheBox",
                "source": "HackTheBox",
                "url": "https://www.hackthebox.com/",
                "reason": "Hands-on penetration testing lab with vulnerable machines and guided labs.",
                "how_to_use": "Start with easy machines to build skills; work through the tutorial VMs first."
            },
            {
                "title": "TryHackMe",
                "source": "TryHackMe",
                "url": "https://tryhackme.com/",
                "reason": "Gamified cybersecurity training with guided rooms (labs) from beginner to advanced.",
                "how_to_use": "Follow the learning paths (e.g., 'Intro to Cybersecurity') room by room."
            },
        ],
        'general': [
            {
                "title": "GitHub Copilot Code Completions",
                "source": "GitHub",
                "url": "https://docs.github.com/en/copilot",
                "reason": "Learn how to use Copilot effectively across different programming tasks.",
                "how_to_use": "Explore Copilot's capabilities and integrate it into your development workflow."
            },
            {
                "title": "Developer Communities and Forums",
                "source": "Multiple platforms",
                "url": "https://stackoverflow.com/",
                "reason": "Connect with other learners and get answers to domain-specific questions.",
                "how_to_use": "Ask questions, help others, and build your professional network."
            },
            {
                "title": "Official Documentation and Tutorials",
                "source": "Various",
                "url": "https://learn.microsoft.com/",
                "reason": "Primary source for learning tools, frameworks, and technologies directly from creators.",
                "how_to_use": "Bookmark the tutorials and reference sections for quick lookups."
            },
        ]
    }

    # Get goal-specific resources or fall back to general
    goal_specific = goal_specific_map.get(category, goal_specific_map['general'])
    
    # Combine core resources with goal-specific resources
    all_resources = core_resources + goal_specific
    
    return all_resources
