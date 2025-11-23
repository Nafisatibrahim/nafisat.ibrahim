"""
Navbar component for the portfolio website.
"""

# Import libraries
import streamlit as st
from components.theme import get_theme_colors, toggle_theme # Import theme functions
from components.language import toggle_language # Import language function

# Render navbar function
def render_navbar():
    """Render the navigation bar with theme and language toggles"""
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    
    colors = get_theme_colors(st.session_state.theme)
    
    # Navbar CSS
    navbar_css = f"""
    <style>
    .navbar {{
        padding: 24px 40px;
        margin-bottom: 0px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
    }}
    
    .nav-pill {{
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 15px;
        padding: 12px 28px;
        border-radius: 24px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 246, 255, 0.3);
        display: inline-block;
    }}
    
    .nav-pill:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 246, 255, 0.5);
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_pink']});
    }}
    </style>
    """
    
    st.markdown(navbar_css, unsafe_allow_html=True)
    
    # Main navigation links
    navbar_html = f"""
    <div class="navbar">
        <a href="/" class="nav-pill" target="_self">Home</a>
        <a href="/profile" class="nav-pill" target="_self">Profile</a>
        <a href="/projects" class="nav-pill" target="_self">Projects</a>
        <a href="/research" class="nav-pill" target="_self">Research</a>
        <a href="/experience" class="nav-pill" target="_self">Experience</a>
        <a href="/linktree" class="nav-pill" target="_self">Connect</a>
    </div>
    """
    
    st.markdown(navbar_html, unsafe_allow_html=True)
    
    # Toggle buttons in columns (positioned separately below navbar)
    col1, col2, col3 = st.columns([8, 1, 1])
    
    with col2:
        if 'language' not in st.session_state:
            st.session_state.language = 'en'
        lang_button = "🇫🇷 FR" if st.session_state.language == 'en' else "🇬🇧 EN"
        if st.button(lang_button, key="lang_toggle", help="Toggle Language"):
            toggle_language()
            st.rerun()
    
    with col3:
        theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
        if st.button(theme_icon, key="theme_toggle", help="Toggle Theme"):
            toggle_theme()
            st.rerun()
    
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

