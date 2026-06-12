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
    # Should return 7 core + 3 goal-specific = 10 resources
    assert len(res) == 10
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
    # Empty string should fall back to general, which returns 7 core + 3 generic = 10
    assert len(res) == 10


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        resource_agent(None)


# New tests for goal-specific behavior
def test_resource_returns_more_than_seven():
    res = resource_agent("machine learning")
    assert len(res) == 10  # 7 core + 3 goal-specific


def test_resource_includes_all_core_urls():
    """Verify all 7 core URLs are always present regardless of goal"""
    for goal in ["AI", "software development", "product", "data", "security", "generic"]:
        res = resource_agent(goal)
        urls = {item.get("url") for item in res}
        assert REQUIRED_URLS.issubset(urls), f"Missing core URLs for goal: {goal}"


def test_resource_ai_engineer_has_specific_resources():
    res = resource_agent("machine learning and AI")
    assert len(res) == 10
    urls = {item.get("url") for item in res}
    # Should include AI-specific resources
    assert any("fast.ai" in url or "paperswithcode" in url or "huggingface" in url for url in urls)


def test_resource_software_developer_has_specific_resources():
    res = resource_agent("build a web application")
    assert len(res) == 10
    urls = {item.get("url") for item in res}
    # Should include software development resources
    assert any("eloquentjavascript" in url or "stackoverflow" in url or "refactoring.guru" in url for url in urls)


def test_resource_product_owner_has_specific_resources():
    res = resource_agent("product strategy and management")
    assert len(res) == 10
    urls = {item.get("url") for item in res}
    # Should include product-specific resources
    assert any("amazon.com" in url or "leanproductplaybook" in url or "producthunt" in url for url in urls)


def test_resource_data_analyst_has_specific_resources():
    res = resource_agent("data analytics and visualization")
    assert len(res) == 10
    urls = {item.get("url") for item in res}
    # Should include data analysis resources
    assert any("mode.com" in url or "tableau.com" in url or "kaggle" in url for url in urls)


def test_resource_cybersecurity_has_specific_resources():
    res = resource_agent("cybersecurity and network security")
    assert len(res) == 10
    urls = {item.get("url") for item in res}
    # Should include cybersecurity resources
    assert any("owasp.org" in url or "hackthebox" in url or "tryhackme" in url for url in urls)


def test_resource_generic_goal_returns_ten():
    """Verify generic fallback returns 10 resources"""
    res = resource_agent("learn something new")
    assert len(res) == 10
    urls = {item.get("url") for item in res}
    # Still includes all core URLs
    assert REQUIRED_URLS.issubset(urls)
