"""
This module contains projects
"""

# Import libraries
import streamlit as st
import json
from components.theme import inject_custom_css, get_theme_colors
from components.navbar import render_navbar
from components.card import ProjectCard

st.set_page_config(
    page_title="Projects - Personal Website",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize theme from URL parameter or session state
query_params = st.query_params
if "theme" in query_params:
    st.session_state.theme = query_params["theme"]
elif "theme" not in st.session_state:
    st.session_state.theme = "dark"

inject_custom_css()
colors = get_theme_colors(st.session_state.theme)
render_navbar()

# Track page view
track_page_view("Projects")

st.markdown(f"""
<div style="text-align: center; margin-bottom: 40px;">
    <h1 style="font-size: 48px;">Projects Portfolio</h1>
    <p style="color: {colors['text_secondary']}; font-size: 18px;">
        A showcase of my technical projects and contributions
    </p>
</div>
""", unsafe_allow_html=True)

# Load projects data
with open("data/projects.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    projects = data.get("projects", [])

# Extract unique tags and skills
all_tags = sorted(list(set([tag for proj in projects for tag in proj.get('tags', [])])))
all_skills = sorted(list(set([skill for proj in projects for skill in proj.get('technical_skills', [])])))

# Filter by Tags
st.markdown("**Filter by Tags**")
selected_tags = st.multiselect(
    "Select tags",
    options=all_tags,
    default=[],
    label_visibility="collapsed",
    key="tags_filter"
)

# Filter by Skills
st.markdown("**Filter by Skills**")
selected_skills = st.multiselect(
    "Select skills",
    options=all_skills,
    default=[],
    label_visibility="collapsed",
    key="skills_filter"
)

# Search Projects
st.markdown("**Search Projects**")
search_query = st.text_input(
    "Search by title or description",
    placeholder="Search projects...",
    label_visibility="collapsed",
    key="search_projects"
)

st.markdown("<br/>", unsafe_allow_html=True)

# Apply filters
filtered_projects = projects.copy()

if selected_tags:
    filtered_projects = [
        proj for proj in filtered_projects
        if any(tag in proj.get('tags', []) for tag in selected_tags)
    ]
    track_interaction("Projects", "filter_by_tags", {"tags": selected_tags})

if selected_skills:
    filtered_projects = [
        proj for proj in filtered_projects
        if any(skill in proj.get('technical_skills', []) for skill in selected_skills)
    ]
    track_interaction("Projects", "filter_by_skills", {"skills": selected_skills})

if search_query:
    filtered_projects = [
        proj for proj in filtered_projects
        if search_query.lower() in proj.get('title', '').lower()
        or search_query.lower() in proj.get('description', '').lower()
    ]
    track_interaction("Projects", "search", {"query": search_query})

# Display results
st.markdown(f"### Showing {len(filtered_projects)} of {len(projects)} projects")
st.markdown("<br/>", unsafe_allow_html=True)

if filtered_projects:
    cols = st.columns(2)
    for idx, project in enumerate(filtered_projects):
        with cols[idx % 2]:
            ProjectCard(project, st.session_state.theme)
else:
    st.info("🔍 No projects match your filters. Try adjusting your search criteria.")

st.markdown("<br/><br/>", unsafe_allow_html=True)
