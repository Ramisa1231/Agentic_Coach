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

    category = _detect_goal_category(goal)
    
    roadmaps = {
        'ai_engineer': [
            "Understand fundamental machine learning concepts: supervised vs. unsupervised learning",
            "Learn Python libraries: NumPy, Pandas, Scikit-learn for data processing and modeling",
            "Build a simple predictive model on a beginner-friendly dataset (e.g., Iris or Boston Housing)",
            "Explore neural networks basics and try a simple deep learning framework like TensorFlow/PyTorch",
            "Experiment with a real-world dataset and deploy your model in a simple web app",
        ],
        'software_developer': [
            "Set up your development environment: choose a language, install tools, and learn version control (Git)",
            "Master fundamentals: variables, loops, conditionals, functions, and basic data structures",
            "Build a small CLI or web project that solves a real problem for you",
            "Learn about testing, debugging, and code quality practices",
            "Deploy your project, gather feedback, and iterate on improvements",
        ],
        'product_owner': [
            "Understand core product management concepts: user needs, market research, and problem validation",
            "Learn how to define user stories, acceptance criteria, and prioritization frameworks",
            "Practice creating a simple product roadmap for a real or hypothetical product",
            "Study competitive analysis and customer feedback collection techniques",
            "Develop a product vision document and present it to stakeholders",
        ],
        'data_analyst': [
            "Learn SQL fundamentals: SELECT, JOIN, WHERE, and basic aggregations for querying databases",
            "Master data visualization tools: create compelling charts, dashboards, and reports",
            "Practice exploratory data analysis: identify patterns, outliers, and trends in datasets",
            "Learn statistical basics: distributions, correlation, hypothesis testing for data insights",
            "Build an end-to-end analytics project from raw data to actionable insights and presentation",
        ],
        'cybersecurity': [
            "Understand networking basics: TCP/IP, DNS, firewalls, and common network attacks",
            "Learn cryptography fundamentals: encryption, hashing, and secure communication protocols",
            "Practice identifying common vulnerabilities: SQL injection, XSS, CSRF, and password attacks",
            "Explore penetration testing tools and techniques in a controlled lab environment",
            "Develop a security assessment or build a hardened application with best practices",
        ],
        'general': [
            "Clarify the goal and define simple success criteria",
            "Learn the fundamental concepts and vocabulary",
            "Follow a short tutorial and build a focused mini-project",
            "Explore useful tools, libraries, and debugging techniques",
            "Practice, iterate on the project, and write a short summary",
        ]
    }
    
    return roadmaps.get(category, roadmaps['general'])
