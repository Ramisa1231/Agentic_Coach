import importlib

modules = [
    "agents.planner_agent",
    "agents.resource_agent",
    "agents.creative_agent",
    "agents.documentation_agent",
]

for m in modules:
    importlib.import_module(m)

print("imports ok")
