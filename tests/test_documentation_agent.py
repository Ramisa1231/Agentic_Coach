import pytest

from agents.documentation_agent import documentation_agent


def test_documentation_agent_structure_and_types():
    out = documentation_agent("build a demo")
    assert isinstance(out, dict)
    expected_keys = {"readme", "architecture", "testing", "references"}
    assert expected_keys.issubset(set(out.keys()))
    for k in expected_keys:
        assert isinstance(out[k], list)
        assert len(out[k]) > 0
        assert all(isinstance(item, str) and item.strip() for item in out[k])


def test_documentation_agent_includes_goal_in_readme():
    goal = "streamlit demo"
    out = documentation_agent(goal)
    assert any(goal in s for s in out["readme"]) or any(goal in s for s in out["readme"])


def test_non_string_raises_typeerror():
    with pytest.raises(TypeError):
        documentation_agent(123)  # type: ignore
