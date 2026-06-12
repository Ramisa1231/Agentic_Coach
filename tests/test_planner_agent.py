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
