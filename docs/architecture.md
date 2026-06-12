# Architecture

```mermaid
flowchart LR
	subgraph U[User]
		user["User\n(enter goal)"]
	end

	subgraph S[Streamlit App]
		app["app.py\n(Streamlit UI)"]
	end

	subgraph A[Agents]
		planner["Planner Agent\n(planner_agent)"]
		resource["Resource Agent\n(resource_agent)"]
		creative["Creative Agent\n(creative_agent)"]
		docs["Documentation Agent\n(documentation_agent)"]
	end

	subgraph O[Outputs]
		roadmap["Learning Roadmap"]
		resources["Recommended Resources"]
		ideas["Creative Project Ideas"]
		documentation["Documentation Suggestions"]
	end

	user -->|"goal text"| app
	app -->|"call planner_agent(goal)"| planner
	app -->|"call resource_agent(goal)"| resource
	app -->|"call creative_agent(goal)"| creative
	app -->|"call documentation_agent(goal)"| docs

	planner -->|"roadmap list"| app
	resource -->|"resource list"| app
	creative -->|"ideas list"| app
	docs -->|"doc suggestions"| app

	app --> roadmap
	app --> resources
	app --> ideas
	app --> documentation

	classDef agent fill:#f9f,stroke:#333,stroke-width:1px;
	class planner,resource,creative,docs agent;
```

**Explanation**

- User enters a short learning or project goal into the Streamlit UI (`app.py`).
- The Streamlit app calls each agent function with the same `goal` string:
	- `planner_agent` → produces a five-step learning roadmap.
	- `resource_agent` → returns recommended learning resources.
	- `creative_agent` → suggests three creative project ideas.
	- `documentation_agent` → suggests README, architecture, testing, and references sections.
- Each agent returns deterministic, display-ready data that the Streamlit app renders inside expandable sections for the user to read, copy, or act on.

This diagram and explanation are suitable to include in the project README or `docs/architecture.md` on GitHub.

