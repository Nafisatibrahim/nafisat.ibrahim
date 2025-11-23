"""
This is the theme configuration module.
"""

# Import libraries
import streamlit as st

# Define theme colors
def get_theme_colors(theme):
    if theme == "dark":
        return {
            "bg_primary": "#0a0e27",
            "bg_secondary": "#141b3d",
            "bg_card": "#1a2347",
            "text_primary": "#ffffff",
            "text_secondary": "#b8c5d6",
            "neon_cyan": "#00f6ff",
            "neon_blue": "#00d7ff",
            "neon_pink": "#ff00ff",
            "neon_purple": "#9d4bff",
            "border_color": "rgba(0, 246, 255, 0.3)",
            "shadow_glow": "0 0 20px rgba(0, 246, 255, 0.4)"
        }
    else:
        return {
            "bg_primary": "#f5f7fa",
            "bg_secondary": "#ffffff",
            "bg_card": "#ffffff",
            "text_primary": "#1a1a1a",
            "text_secondary": "#4a5568",
            "neon_cyan": "#00b8d4",
            "neon_blue": "#0091ea",
            "neon_pink": "#d500f9",
            "neon_purple": "#651fff",
            "border_color": "rgba(0, 145, 234, 0.3)",
            "shadow_glow": "0 0 15px rgba(0, 145, 234, 0.3)"
        }

# Inject custom CSS for theming
def inject_custom_css():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"
    
    colors = get_theme_colors(st.session_state.theme)
    
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    /* Global Styles */
    .stApp {{
        background-color: {colors['bg_primary']};
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><defs><pattern id="tech-pattern" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{colors["neon_cyan"]}" opacity="0.1"/><line x1="0" y1="20" x2="40" y2="20" stroke="{colors["neon_cyan"]}" stroke-width="0.5" opacity="0.05"/></pattern></defs><rect width="100%" height="100%" fill="url(%23tech-pattern)"/></svg>');
        font-family: 'Inter', sans-serif;
    }}
    
    * {{
        color: {colors['text_primary']};
    }}
    
    /* Hide Streamlit Branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {colors['bg_secondary']};
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(45deg, {colors['neon_cyan']}, {colors['neon_purple']});
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(45deg, {colors['neon_blue']}, {colors['neon_pink']});
    }}
    
    /* Card Styles */
    .tech-card {{
        background: {colors['bg_card']};
        border: 2px solid {colors['border_color']};
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        box-shadow: {colors['shadow_glow']};
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }}
    
    .tech-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 0 30px rgba(0, 246, 255, 0.6);
        border-color: {colors['neon_cyan']};
    }}
    
    /* Neon Button */
    .neon-button {{
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 32px;
        font-weight: 600;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(0, 246, 255, 0.5);
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }}
    
    .neon-button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(0, 246, 255, 0.8);
    }}
    
    /* Pill/Badge Styles */
    .skill-pill {{
        background: linear-gradient(135deg, {colors['neon_cyan']}22, {colors['neon_purple']}22);
        border: 1px solid {colors['neon_cyan']};
        border-radius: 20px;
        padding: 6px 16px;
        margin: 4px;
        display: inline-block;
        font-size: 13px;
        font-weight: 500;
        transition: all 0.2s ease;
    }}
    
    .skill-pill:hover {{
        background: linear-gradient(135deg, {colors['neon_cyan']}44, {colors['neon_purple']}44);
        transform: scale(1.05);
    }}
    
    /* Headings */
    h1, h2, h3 {{
        font-weight: 700;
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    /* Input Fields */
    .stTextInput input {{
        background-color: {colors['bg_card']} !important;
        border: 2px solid {colors['border_color']} !important;
        border-radius: 12px !important;
        color: {colors['text_primary']} !important;
        padding: 12px !important;
        transition: all 0.3s ease !important;
    }}
    
    .stTextInput input:focus {{
        border-color: {colors['neon_cyan']} !important;
        box-shadow: 0 0 15px rgba(0, 246, 255, 0.3) !important;
    }}
    
    /* Multiselect */
    .stMultiSelect {{
        background-color: {colors['bg_card']};
        border-radius: 12px;
    }}
    
    /* Selectbox */
    .stSelectbox select {{
        background-color: {colors['bg_card']} !important;
        border: 2px solid {colors['border_color']} !important;
        border-radius: 12px !important;
        color: {colors['text_primary']} !important;
    }}
    
    /* Expander */
    .streamlit-expanderHeader {{
        background-color: {colors['bg_card']};
        border: 2px solid {colors['border_color']};
        border-radius: 12px;
        font-weight: 600;
    }}
    
    .streamlit-expanderHeader:hover {{
        border-color: {colors['neon_cyan']};
    }}
    
    /* Links */
    a {{
        color: {colors['neon_cyan']};
        text-decoration: none;
        transition: all 0.2s ease;
    }}
    
    a:hover {{
        color: {colors['neon_pink']};
        text-shadow: 0 0 10px {colors['neon_pink']};
    }}
    
    /* Status Badge */
    .status-badge {{
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        text-transform: uppercase;
    }}
    
    .status-published {{
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
    }}
    
    .status-draft {{
        background: linear-gradient(135deg, #f59e0b, #d97706);
        color: white;
    }}
    
    .status-progress {{
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_blue']});
        color: white;
    }}
    
    /* Timeline (for News page) */
    .timeline-item {{
        border-left: 3px solid {colors['neon_cyan']};
        padding-left: 24px;
        margin-bottom: 32px;
        position: relative;
    }}
    
    .timeline-item::before {{
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: {colors['neon_cyan']};
        box-shadow: 0 0 10px {colors['neon_cyan']};
    }}
    
    /* Experience Timeline */
    .experience-timeline {{
        position: relative;
        padding: 0;
        margin: 32px 0;
        min-height: 400px;
        display: flex;
        flex-direction: column;
    }}
    
    .experience-timeline::before {{
        content: '';
        position: absolute;
        left: 32px;
        top: 0;
        height: 100%;
        min-height: 400px;
        width: 4px;
        background: linear-gradient(180deg, {colors['neon_cyan']}, {colors['neon_purple']});
        box-shadow: 0 0 15px {colors['neon_cyan']};
    }}
    
    .experience-entry {{
        position: relative;
        padding-left: 96px;
        margin-bottom: 48px;
        flex: 0 0 auto;
    }}
    
    .experience-entry::before {{
        content: '';
        position: absolute;
        left: 32px;
        transform: translateX(-50%) translateY(-50%);
        top: 24px;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: {colors['neon_cyan']};
        box-shadow: 0 0 15px {colors['neon_cyan']};
    }}
    
    /* Grid Layout */
    .project-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 24px;
        margin: 24px 0;
    }}
    
    /* Code/Mono Font */
    code, pre {{
        font-family: 'JetBrains Mono', monospace !important;
        background: {colors['bg_card']};
        border: 1px solid {colors['border_color']};
        border-radius: 8px;
        padding: 4px 8px;
    }}
    
    /* Image Styles */
    img {{
        border-radius: 12px;
        border: 2px solid {colors['border_color']};
    }}
    
    /* Button override */
    .stButton button {{
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 32px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(0, 246, 255, 0.5);
    }}
    
    .stButton button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(0, 246, 255, 0.8);
    }}
    
    /* Download Button */
    .stDownloadButton button {{
        background: linear-gradient(135deg, {colors['neon_pink']}, {colors['neon_purple']});
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 32px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(255, 0, 255, 0.5);
    }}
    
    .stDownloadButton button:hover {{
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.8);
    }}
    
    /* Markdown overrides */
    .stMarkdown {{
        color: {colors['text_primary']};
    }}
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {{
        background-color: {colors['bg_secondary']};
        border-right: 2px solid {colors['border_color']};
    }}
    
    /* Animated Tech Background */
    @keyframes pulse-grid {{
        0%, 100% {{ opacity: 0.05; }}
        50% {{ opacity: 0.15; }}
    }}
    
    .stApp::after {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background: 
            linear-gradient(90deg, {colors['neon_cyan']}05 1px, transparent 1px),
            linear-gradient(180deg, {colors['neon_purple']}05 1px, transparent 1px);
        background-size: 60px 60px;
        animation: pulse-grid 4s ease-in-out infinite;
        z-index: 0;
    }}
    
    /* Subtle Parallax Scroll Effect */
    .tech-card {{
        will-change: transform;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    /* Mouse-Tracking Glow */
    @keyframes glow-follow {{
        0%, 100% {{ transform: scale(1); opacity: 0.3; }}
        50% {{ transform: scale(1.2); opacity: 0.5; }}
    }}
    
    /* Neon Pulse Animation */
    @keyframes neon-pulse {{
        0%, 100% {{
            box-shadow: 0 0 20px {colors['neon_cyan']},
                        0 0 40px {colors['neon_cyan']},
                        0 0 60px {colors['neon_cyan']};
        }}
        50% {{
            box-shadow: 0 0 30px {colors['neon_purple']},
                        0 0 60px {colors['neon_purple']},
                        0 0 90px {colors['neon_purple']};
        }}
    }}
    
    /* Floating Animation */
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    .tech-card:hover {{
        animation: float 3s ease-in-out infinite;
    }}
    
    /* Glass-morphism Effect */
    .glass-bg {{
        background: rgba(26, 35, 71, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 246, 255, 0.2);
    }}
    
    /* Gradient Text */
    .gradient-text {{
        background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    /* Hover Glow Effect */
    .hover-glow {{
        transition: all 0.3s ease;
    }}
    
    .hover-glow:hover {{
        box-shadow: 0 0 25px {colors['neon_cyan']},
                    0 0 50px {colors['neon_cyan']},
                    inset 0 0 25px rgba(0, 246, 255, 0.1);
    }}
    </style>
    
    <script>
    // Mouse-tracking glow effect
    document.addEventListener('mousemove', (e) => {{
        const x = e.clientX;
        const y = e.clientY;
        document.documentElement.style.setProperty('--mouse-x', x + 'px');
        document.documentElement.style.setProperty('--mouse-y', y + 'px');
    }});
    
    // Parallax effect on scroll
    window.addEventListener('scroll', () => {{
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.tech-card');
        parallaxElements.forEach((el, index) => {{
            const speed = 0.05 + (index % 3) * 0.02;
            el.style.transform = `translateY(${{scrolled * speed}}px)`;
        }});
    }});
    </script>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# Theme toggling function
def toggle_theme():
    if st.session_state.theme == "dark":
        st.session_state.theme = "light"
    else:
        st.session_state.theme = "dark"

# Alias for applying theme
def apply_theme():
    """Alias for inject_custom_css for simpler API"""
    inject_custom_css()

# Load CSS function
def load_css():
    """Load CSS from external styles.css file"""
    try:
        with open("assets/styles.css") as f:
            css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError:
        inject_custom_css()

# Manual color palette access
def get_colors():
    """Get color palette for manual usage"""
    return {
        "neon_cyan": "#00f6ff",
        "neon_purple": "#9d4bff",
        "neon_pink": "#ff00ff",
        "text_primary": "#ffffff",
        "text_secondary": "#c7c7c7"
    }
