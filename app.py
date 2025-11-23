"""
This is the main application module for the project.
"""

# Import libraries
import streamlit as st
from components.navbar import render_navbar # Import the navbar component
from components.theme import inject_custom_css, get_theme_colors # Import theme functions
from components.language import get_text # Import language function

# Page configuration
st.set_page_config(
    page_title="Nafisat Ibrahim - Portfolio",
    page_icon=":briefcase:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load custom CSS
inject_custom_css()

# Render navbar
render_navbar()

# Get theme colors
colors = get_theme_colors(st.session_state.theme)

# Light/Dark mode toggle button
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# Main content
st.markdown(f"""
<div style="text-align:center; padding:80px 20px;">
    <h1 style="
        font-size:72px;
        margin-bottom:24px;
        background:linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;">
        Welcome to My Digital Portfolio
    </h1>
    <p style="font-size:30px; color:{colors['text_secondary']}; max-width:800px; margin:auto;">
        Explore my journey in machine learning, research, and innovation.
    </p>
</div>
""", unsafe_allow_html=True)

# Feature cards
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.markdown("""
    <div class="tech-card" style="text-align:center;">
        <div style="font-size:64px;">👤</div>
        <h2>Profile</h2>
        <p>Learn about my background, skills, and journey.</p>
        <a href="/1_Profile" class="neon-button">View Profile →</a>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tech-card" style="text-align:center;">
        <div style="font-size:64px;">🚀</div>
        <h2>Projects</h2>
        <p>Explore the things I've built and contributed to.</p>
        <a href="/3_Projects" class="neon-button">View Projects →</a>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tech-card" style="text-align:center;">
        <div style="font-size:64px;">🔬</div>
        <h2>Research</h2>
        <p>Read about my academic and applied research work.</p>
        <a href="/4_Research" class="neon-button">View Research →</a>
    </div>""", unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="tech-card" style="text-align:center;">
        <div style="font-size:64px;">💼</div>
        <h2>Experience</h2>
        <p>See the roles and work that shaped my expertise.</p>
        <a href="/2_Experience" class="neon-button">View Experience →</a>
    </div>""", unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="tech-card" style="text-align:center;">
        <div style="font-size:64px;">📺</div>
        <h2>Media</h2>
        <p>Watch talks, interviews, and presentations.</p>
        <a href="/5_Media" class="neon-button">View Media →</a>
    </div>""", unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="tech-card" style="text-align:center;">
        <div style="font-size:64px;">🔗</div>
        <h2>Connect</h2>
        <p>Find me across professional and social platforms.</p>
        <a href="/5_Connect" class="neon-button">Connect →</a>
    </div>""", unsafe_allow_html=True)

st.markdown("<br/><br/>", unsafe_allow_html=True)

st.markdown(f"""
<div style="background: linear-gradient(135deg, {colors['neon_cyan']}22, {colors['neon_purple']}22); border: 2px solid {colors['neon_cyan']}; border-radius: 16px; padding: 48px; text-align: center; margin: 40px 0;">
    <h2 style="margin-bottom: 16px;">Let's Build Something Amazing Together</h2>
    <p style="color: {colors['text_secondary']}; font-size: 18px; margin-bottom: 32px;">
        I'm always interested in collaborating on innovative projects and discussing new opportunities
    </p>
    <a href="mailto:your.email@example.com" class="neon-button" style="font-size: 18px; padding: 16px 48px;">
        📧 Get In Touch
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; color: {colors['text_secondary']}; padding: 40px 0; border-top: 1px solid {colors['border_color']};">
    <p>Built with ❤️ using Streamlit | Designed with a futuristic aesthetic</p>
    <p style="font-size: 14px; margin-top: 8px;">© 2024 Your Name. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)