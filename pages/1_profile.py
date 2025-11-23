"""
This is the Profile page module.
"""

import streamlit as st
import json
from components.navbar import render_navbar
from components.theme import load_css, get_colors

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Nafisat Ibrahim - Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()
colors = get_colors()

render_navbar()

# ==================== LOAD DATA ====================
def load_data():
    with open("data/profile.json", "r") as f:
        return json.load(f)

data = load_data()
profile = data["profile"]
socials = data["socials"]
skills = data["skills"]
stats = data["stats"]

# ==================== PROFILE HEADER SECTION ====================
st.markdown(
f"""
<div style="text-align:center; margin-top:60px;">
<img src="{profile['profile_image']}"
style="width:180px; height:180px; border-radius:50%; object-fit:cover; border:3px solid {colors['neon_cyan']}; box-shadow:0 0 25px rgba(0, 246, 255, 0.4);" />

<h1 style="font-size:48px; margin-top:25px; font-weight:700; 
background:linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
-webkit-background-clip:text; -webkit-text-fill-color:transparent;">
{profile['name']}
</h1>

<h3 style="font-size:22px; margin-top:-8px; color:{colors['neon_cyan']}; font-weight:500;">
{profile['title']}
</h3>

<p style="font-size:18px; max-width:750px; margin:25px auto; color:{colors['text_secondary']}; line-height:1.6;">
{profile['bio']}
</p>
</div>
""",
unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ==================== SOCIAL LINKS SECTION ====================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <a href="{socials['email']}" class="neon-button" style="display:block; text-align:center;">
            📧 Email
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <a href="{socials['github']}" class="neon-button" style="display:block; text-align:center;" target="_blank">
            🔗 GitHub
        </a>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <a href="{socials['linkedin']}" class="neon-button" style="display:block; text-align:center;" target="_blank">
            💼 LinkedIn
        </a>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <a href="{socials['medium']}" class="neon-button" style="display:block; text-align:center;" target="_blank">
            ✍️ Medium
        </a>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='margin-top:28px'></div>", unsafe_allow_html=True)

# ==================== RESUME DOWNLOAD SECTION ====================
col_resume_left, col_resume_center, col_resume_right = st.columns([1,2,1])

with col_resume_center:
    try:
        with open(socials["resume"], "rb") as pdf:
            st.download_button(
                label="📄 Download Resume",
                data=pdf,
                file_name="Nafisat_Ibrahim_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
                type="primary"
            )
    except FileNotFoundError:
        st.info("Resume file not found. Please add your resume PDF to the assets folder.")

# ==================== PORTFOLIO STATS SECTION ====================
st.markdown(f"""
<div style='text-align:center; margin-top:60px;'>
    <h2 style='font-size:36px; background:linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']}); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>Portfolio Stats</h2>
    <p style='font-size:18px; color:{colors['text_secondary']};'>
        Key achievements and contributions
    </p>
</div>
""", unsafe_allow_html=True)

stat_col1, stat_col2, stat_col3 = st.columns(3)

with stat_col1:
    st.markdown(f"""
    <div class="tech-card" style="text-align:center; padding:32px; background:rgba(0,246,255,0.05);">
        <div style="font-size:56px; font-weight:700; color:{colors['neon_cyan']}; margin-bottom:12px;">
            {stats['projects_completed']}
        </div>
        <h3 style="font-size:18px; margin:8px 0; color:{colors['text_primary']};">Projects Completed</h3>
        <p style="color:{colors['text_secondary']}; font-size:14px; margin-top:8px;">
            End-to-end ML & AI solutions
        </p>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    st.markdown(f"""
    <div class="tech-card" style="text-align:center; padding:32px; background:rgba(157,75,255,0.05);">
        <div style="font-size:56px; font-weight:700; color:{colors['neon_purple']}; margin-bottom:12px;">
            {stats['models_trained']}
        </div>
        <h3 style="font-size:18px; margin:8px 0; color:{colors['text_primary']};">Models Trained</h3>
        <p style="color:{colors['text_secondary']}; font-size:14px; margin-top:8px;">
            Data Science, Machine Learning, Computer Vision & NLP models
        </p>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    st.markdown(f"""
    <div class="tech-card" style="text-align:center; padding:32px; background:rgba(255,0,255,0.05);">
        <div style="font-size:56px; font-weight:700; color:{colors['neon_pink']}; margin-bottom:12px;">
            {stats['github_commits']}
        </div>
        <h3 style="font-size:18px; margin:8px 0; color:{colors['text_primary']};">GitHub Commits</h3>
        <p style="color:{colors['text_secondary']}; font-size:14px; margin-top:8px;">
            Active open-source contributor
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== FEATURED TOOLS SECTION ====================
st.markdown(f"""
<div style='text-align:center; margin-top:80px;'>
    <h2 style='font-size:36px; background:linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']}); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>Featured Tools</h2>
    <p style='font-size:18px; color:{colors['text_secondary']};'>
        My core technical tools — always in motion
    </p>
</div>
""", unsafe_allow_html=True)

floating = data.get("Data Tools", [])

html_floating = '<div style="text-align:center; margin-top:30px;">'

delay = 0
for tool in floating:
    html_floating += f'<span class="skill-animate" style="animation-delay:{delay}s;">{tool}</span>'
    delay += 0.35

html_floating += '</div>'

st.markdown(html_floating, unsafe_allow_html=True)

# ==================== TECHNICAL SKILLS SECTION ====================
st.markdown(f"""
<div style='text-align:center; margin-top:80px;'>
    <h2 style='font-size:36px; background:linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']}); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>Technical Skills</h2>
    <p style='font-size:18px; color:{colors['text_secondary']};'>
        Full technology stack and expertise areas
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)

skill_categories = skills

col_left, col_right = st.columns(2)

skill_items = list(skill_categories.items())
half = len(skill_items) // 2

with col_left:
    for category, skill_list in skill_items[:half]:
        st.markdown(f"""
        <div class="tech-card" style="margin-bottom:24px;">
            <h3 style="font-size:20px; margin-bottom:16px; color:{colors['neon_cyan']};">
                {category}
            </h3>
            <div>
                {''.join([f'<span style="display:inline-block; padding:8px 16px; margin:6px; background:rgba(0,246,255,0.1); border:2px solid {colors["neon_cyan"]}; border-radius:20px; font-size:14px; color:{colors["text_primary"]}; transition:all 0.3s ease;">{skill}</span>' for skill in skill_list])}
            </div>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    for category, skill_list in skill_items[half:]:
        st.markdown(f"""
        <div class="tech-card" style="margin-bottom:24px;">
            <h3 style="font-size:20px; margin-bottom:16px; color:{colors['neon_purple']};">
                {category}
            </h3>
            <div>
                {''.join([f'<span style="display:inline-block; padding:8px 16px; margin:6px; background:rgba(157,75,255,0.1); border:2px solid {colors["neon_purple"]}; border-radius:20px; font-size:14px; color:{colors["text_primary"]}; transition:all 0.3s ease;">{skill}</span>' for skill in skill_list])}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
