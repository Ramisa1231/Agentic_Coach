import pytest

from agents.creative_agent import creative_agent


def test_creative_agent_returns_three_ideas():
    ideas = creative_agent("build a demo")
    assert isinstance(ideas, list)
    assert len(ideas) == 3


def test_each_idea_has_required_keys_and_strings():
    ideas = creative_agent("learn X")
    required = {"title", "problem", "solution", "why_it_is_creative"}
    for idea in ideas:
        assert isinstance(idea, dict)
        assert required.issubset(set(idea.keys()))
        for k in required:
            assert isinstance(idea[k], str)
            assert idea[k].strip()


def test_deterministic_for_same_input():
    a = creative_agent("make a portfolio")
    b = creative_agent("make a portfolio")
    assert a == b


def test_non_string_raises_typeerror():
    with pytest.raises(TypeError):
        creative_agent(42)  # type: ignore


# New tests for goal-specific behavior
def test_creative_returns_different_ideas_for_different_goals():
    ai_ideas = creative_agent("machine learning")
    dev_ideas = creative_agent("build an app")
    # At least one idea should be different
    assert ai_ideas != dev_ideas


def test_creative_ai_engineer_goal():
    ideas = creative_agent("learn AI and machine learning")
    assert len(ideas) == 3
    # Verify ideas contain ML-related concepts
    combined = " ".join([idea.get("title", "") for idea in ideas]).lower()
    assert any(kw in combined for kw in ["sentiment", "chatbot", "recommender", "ml", "ai"])


def test_creative_software_developer_goal():
    ideas = creative_agent("build a software application")
    assert len(ideas) == 3
    # Verify ideas contain software development concepts
    combined = " ".join([idea.get("title", "") for idea in ideas]).lower()
    assert any(kw in combined for kw in ["cli", "web app", "notification", "automation", "platform"])


def test_creative_product_owner_goal():
    ideas = creative_agent("develop product strategy")
    assert len(ideas) == 3
    # Verify ideas contain product concepts
    combined = " ".join([idea.get("title", "") for idea in ideas]).lower()
    assert any(kw in combined for kw in ["roadmap", "dashboard", "feedback", "product"])


def test_creative_data_analyst_goal():
    ideas = creative_agent("learn data analytics")
    assert len(ideas) == 3
    # Verify ideas contain data analysis concepts
    combined = " ".join([idea.get("title", "") for idea in ideas]).lower()
    assert any(kw in combined for kw in ["visualization", "churn", "spending", "analyzer", "trends"])


def test_creative_cybersecurity_goal():
    ideas = creative_agent("cybersecurity learning")
    assert len(ideas) == 3
    # Verify ideas contain cybersecurity concepts
    combined = " ".join([idea.get("title", "") for idea in ideas]).lower()
    assert any(kw in combined for kw in ["password", "vulnerability", "scanner", "security", "network"])
