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
