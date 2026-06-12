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

    category = _detect_goal_category(goal)
    
    ideas_map = {
        'ai_engineer': [
            {
                "title": "Build a custom sentiment analyzer for your niche",
                "problem": "Sentiment analysis models are often trained on generic text and don't capture domain-specific language.",
                "solution": (
                    "Fine-tune a pre-trained model (like BERT) on domain-specific reviews or feedback, "
                    "then deploy it as an interactive web app where users can test predictions."
                ),
                "why_it_is_creative": (
                    "Combines transfer learning with practical deployment, showing how pre-trained models "
                    "can be adapted for specific industries."
                ),
            },
            {
                "title": "Create an AI chatbot that learns from user interactions",
                "problem": "Static chatbots don't adapt to new patterns or user preferences.",
                "solution": (
                    "Build a simple chatbot using transformers that logs interactions and uses feedback "
                    "to improve responses over time, with a feedback loop integrated into the UI."
                ),
                "why_it_is_creative": (
                    "Demonstrates reinforcement learning principles and human-in-the-loop AI, "
                    "making ML tangible and collaborative."
                ),
            },
            {
                "title": "Develop a recommender system for an online marketplace",
                "problem": "E-commerce platforms need to recommend products but lack personalization.",
                "solution": (
                    "Build a hybrid recommender (content-based + collaborative filtering) using a sample dataset, "
                    "then visualize recommendations and explain why each product was suggested."
                ),
                "why_it_is_creative": (
                    "Applies real-world ML techniques to a practical problem and focuses on explainability, "
                    "which is critical for user trust."
                ),
            },
        ],
        'software_developer': [
            {
                "title": "Build a personal task automation CLI tool",
                "problem": "Developers repeat routine tasks (file cleanup, deployment, backups) manually.",
                "solution": (
                    "Create a command-line tool that automates your daily workflow: file organization, "
                    "git operations, deployment scripts, with a config file for customization."
                ),
                "why_it_is_creative": (
                    "Solves a real personal pain point, teaches CLI design and configuration management, "
                    "and builds a tool you'll actually use."
                ),
            },
            {
                "title": "Create a collaborative code snippet sharing platform",
                "problem": "Developers scatter useful snippets across notes and never find them again.",
                "solution": (
                    "Build a full-stack web app where users can upload, tag, search, and share code snippets "
                    "with syntax highlighting, comments, and version history."
                ),
                "why_it_is_creative": (
                    "Combines frontend, backend, database, and search logic; teaches API design, "
                    "user authentication, and building for a community."
                ),
            },
            {
                "title": "Develop a real-time notification system",
                "problem": "Apps need to push timely updates to users but polling is inefficient.",
                "solution": (
                    "Build a backend service with WebSockets or Server-Sent Events that notifies clients "
                    "in real time, with a simple dashboard to monitor events."
                ),
                "why_it_is_creative": (
                    "Teaches modern asynchronous communication, scaling considerations, "
                    "and critical infrastructure patterns used in production systems."
                ),
            },
        ],
        'product_owner': [
            {
                "title": "Design a feature roadmap for an AI-powered productivity app",
                "problem": "Product teams struggle to prioritize AI features while balancing user needs and technical feasibility.",
                "solution": (
                    "Create a 6-month roadmap with hypothesis-driven features: define user personas, pain points, "
                    "success metrics, and validate assumptions through user interviews."
                ),
                "why_it_is_creative": (
                    "Practices strategic thinking, data-driven prioritization, and cross-functional collaboration; "
                    "teaches how to communicate technical constraints to non-technical teams."
                ),
            },
            {
                "title": "Build a competitive analysis dashboard",
                "problem": "Product teams need to monitor competitors but manually tracking is error-prone.",
                "solution": (
                    "Create a dashboard that tracks competitor features, pricing, and messaging; "
                    "organize insights by feature parity, differentiation, and gaps."
                ),
                "why_it_is_creative": (
                    "Develops market intelligence skills and turns raw data into actionable strategy, "
                    "showing how to stay ahead of the competition."
                ),
            },
            {
                "title": "Define a user research and feedback system",
                "problem": "Product teams collect feedback but fail to act on it systematically.",
                "solution": (
                    "Design a framework for collecting, analyzing, and prioritizing user feedback: set up surveys, "
                    "user interviews, NPS tracking, and a feedback loop tied to roadmap decisions."
                ),
                "why_it_is_creative": (
                    "Places user voice at the center of product decisions and demonstrates how to validate "
                    "assumptions before building; essential for product-market fit."
                ),
            },
        ],
        'data_analyst': [
            {
                "title": "Analyze and visualize public health trends",
                "problem": "Health organizations struggle to communicate complex disease trends to the public.",
                "solution": (
                    "Fetch public datasets (COVID-19, flu trends, etc.), clean and analyze them, "
                    "then create an interactive dashboard showing trends over time and geographic patterns."
                ),
                "why_it_is_creative": (
                    "Combines real-world data, storytelling, and visualization to communicate insights "
                    "that matter to society."
                ),
            },
            {
                "title": "Build a customer churn prediction model and analysis",
                "problem": "Businesses lose customers but don't know why or how to prevent it.",
                "solution": (
                    "Use a public subscription dataset, perform cohort analysis, calculate churn rates, "
                    "identify at-risk customers, and visualize drivers of churn in a report."
                ),
                "why_it_is_creative": (
                    "Teaches business analytics, statistical analysis, and how to turn insights into retention "
                    "strategies; directly impacts business decisions."
                ),
            },
            {
                "title": "Create a personal spending analyzer",
                "problem": "People don't understand their spending patterns and budgeting remains guesswork.",
                "solution": (
                    "Build a tool that categorizes transactions from a CSV file, visualizes spending by category "
                    "over time, and identifies trends or anomalies with alerts."
                ),
                "why_it_is_creative": (
                    "Applies analytics to personal finance, teaches ETL and data cleaning, and builds something "
                    "immediately useful for financial literacy."
                ),
            },
        ],
        'cybersecurity': [
            {
                "title": "Build a password strength analyzer and cracking simulator",
                "problem": "Users choose weak passwords without understanding why they're vulnerable.",
                "solution": (
                    "Create a tool that analyzes password strength using entropy calculations, "
                    "simulates common cracking attacks (brute force, dictionary), and educates on better practices."
                ),
                "why_it_is_creative": (
                    "Makes cryptography tangible and teaches users why security practices matter; "
                    "combines education with security awareness."
                ),
            },
            {
                "title": "Develop a vulnerability scanner for web applications",
                "problem": "Web apps often have common vulnerabilities that go undetected.",
                "solution": (
                    "Build a scanner that tests for SQL injection, XSS, CSRF, and other OWASP Top 10 vulnerabilities, "
                    "then generates a report with remediation suggestions."
                ),
                "why_it_is_creative": (
                    "Teaches offensive security thinking and practical penetration testing skills; "
                    "helps developers build more secure code."
                ),
            },
            {
                "title": "Create a network security lab and intrusion detection simulator",
                "problem": "Cybersecurity students need hands-on practice but fear real attacks.",
                "solution": (
                    "Build a sandboxed lab environment that simulates network traffic, allows students to set up "
                    "defenses, and then attack it; logs show what was detected and what was missed."
                ),
                "why_it_is_creative": (
                    "Provides safe experimentation, teaches blue team (defensive) thinking, and builds muscle memory "
                    "for security monitoring."
                ),
            },
        ],
        'general': [
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
    }
    
    return ideas_map.get(category, ideas_map['general'])
