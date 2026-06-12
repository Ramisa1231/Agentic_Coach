import streamlit as st

from agents.planner_agent import planner_agent
from agents.resource_agent import resource_agent
from agents.creative_agent import creative_agent
from agents.documentation_agent import documentation_agent


def main() -> None:
    st.set_page_config(page_title="Agentic Coach", layout="centered")
    st.title("Agentic Coach")
    st.write(
        "A lightweight assistant that converts a learning or project goal into a "
        "beginner-friendly plan, resource list, creative project ideas, and "
        "documentation suggestions. No external APIs or LLMs are used yet."
    )

    goal = st.text_area("Describe your learning or project goal", height=120)

    if st.button("Generate Agentic Plan"):
        if not isinstance(goal, str) or not goal.strip():
            st.warning("Please enter a short goal or objective to generate a plan.")
            return

        with st.spinner("Generating plan..."):
            try:
                roadmap = planner_agent(goal)
                resources = resource_agent(goal)
                ideas = creative_agent(goal)
                docs = documentation_agent(goal)
            except Exception as e:
                st.error(f"Error generating plan: {e}")
                return

        st.markdown(f"**Goal:** {goal}")

        with st.expander("1. Learning Roadmap", expanded=True):
            for i, step in enumerate(roadmap, start=1):
                st.write(f"{i}. {step}")

        with st.expander("2. Recommended Resources"):
            for r in resources:
                title = r.get("title") or r.get("source")
                url = r.get("url")
                reason = r.get("reason") or r.get("how_to_use") or ""
                st.markdown(f"**{title}**")
                if url:
                    st.write(url)
                if reason:
                    st.write(reason)
                st.write("---")

        with st.expander("3. Creative Project Ideas"):
            for idea in ideas:
                st.subheader(idea.get("title", "Idea"))
                st.write("**Problem:**", idea.get("problem", ""))
                st.write("**Solution:**", idea.get("solution", ""))
                st.write("**Why it's creative:**", idea.get("why_it_is_creative", ""))

        with st.expander("4. Documentation Suggestions"):
            for section, items in docs.items():
                st.write(f"**{section.title()}**")
                for item in items:
                    st.write(f"- {item}")


if __name__ == "__main__":
    main()
# Placeholder Streamlit app entrypoint for Agentic_Coach
# TODO: implement Streamlit UI and app logic
