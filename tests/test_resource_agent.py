import pytest

from agents.resource_agent import resource_agent


REQUIRED_URLS = {
    "https://learn.microsoft.com/en-gb/collections/3gwqi467467e23/",
    "https://learn.microsoft.com/en-gb/users/syedaramisafariha-1856/",
    "https://github.com/microsoft/agentsleague/tree/main/starter-kits/1-creative-apps",
    "https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering",
    "https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/completions/code-suggestions",
    "https://learn.microsoft.com/en-gb/training/modules/introduction-to-github-copilot/3-interacting-with-copilot",
    "https://www.oreilly.com/",
}


def test_returns_list():
    res = resource_agent("build an AI agent")
    assert isinstance(res, list)


def test_items_are_dicts_and_have_keys():
    res = resource_agent("build an AI agent")
    assert len(res) == 7
    for item in res:
        assert isinstance(item, dict)
        for key in ("title", "source", "url", "reason", "how_to_use"):
            assert key in item


def test_includes_required_urls():
    res = resource_agent("build an AI agent")
    urls = {item.get("url") for item in res}
    assert REQUIRED_URLS.issubset(urls)


def test_empty_string_returns_resources():
    res = resource_agent("")
    assert isinstance(res, list)
    assert len(res) == 7


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        resource_agent(None)
