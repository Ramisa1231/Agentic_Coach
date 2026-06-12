import pytest

from agents.planner_agent import planner_agent


def test_planner_returns_list_of_five():
    steps = planner_agent("learn Streamlit")
    assert isinstance(steps, list)
    assert len(steps) == 5


def test_planner_steps_are_strings():
    steps = planner_agent("build a small app")
    assert all(isinstance(s, str) for s in steps)


def test_planner_empty_string_ok():
    steps = planner_agent("")
    assert len(steps) == 5


def test_planner_non_string_raises_typeerror():
    with pytest.raises(TypeError):
        planner_agent(123)  # type: ignore


def test_steps_non_empty_and_short():
    steps = planner_agent("learn testing")
    assert all(isinstance(s, str) and s.strip() for s in steps)
    assert all(len(s) <= 120 for s in steps)


def test_steps_unique():
    steps = planner_agent("build something")
    assert len(steps) == len(set(steps))


def test_deterministic_for_same_input():
    a = planner_agent("make a demo")
    b = planner_agent("make a demo")
    assert a == b


# New tests for goal-specific behavior
def test_planner_returns_different_roadmaps_for_different_goals():
    ai_steps = planner_agent("machine learning")
    dev_steps = planner_agent("build an app")
    assert ai_steps != dev_steps


def test_planner_ai_engineer_goal():
    steps = planner_agent("learn machine learning")
    assert len(steps) == 5
    # AI Engineer roadmap should contain ML-specific terms
    combined = " ".join(steps).lower()
    assert any(kw in combined for kw in ["machine learning", "neural", "dataset"])


def test_planner_software_developer_goal():
    steps = planner_agent("build a web app")
    assert len(steps) == 5
    # Software Developer roadmap should contain development-specific terms
    combined = " ".join(steps).lower()
    assert any(kw in combined for kw in ["environment", "fundamentals", "testing", "deploy"])


def test_planner_product_owner_goal():
    steps = planner_agent("create a product strategy")
    assert len(steps) == 5
    # Product Owner roadmap should contain product-specific terms
    combined = " ".join(steps).lower()
    assert any(kw in combined for kw in ["product", "roadmap", "strategy", "user"])


def test_planner_data_analyst_goal():
    steps = planner_agent("learn data analysis")
    assert len(steps) == 5
    # Data Analyst roadmap should contain data-specific terms
    combined = " ".join(steps).lower()
    assert any(kw in combined for kw in ["sql", "visualization", "data", "analysis"])


def test_planner_cybersecurity_goal():
    steps = planner_agent("security training")
    assert len(steps) == 5
    # Cybersecurity roadmap should contain security-specific terms
    combined = " ".join(steps).lower()
    assert any(kw in combined for kw in ["security", "encryption", "network", "vulnerability"])
