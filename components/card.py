import streamlit as st
from components.theme import get_theme_colors

def ProjectCard(project, theme="dark"):
    colors = get_theme_colors(theme)
    
    st.markdown(f"""
    <div class="tech-card">
        <h3 style="margin-top: 0;">{project['title']}</h3>
        <p style="color: {colors['text_secondary']};">{project['description']}</p>
        
        <div style="margin: 16px 0;">
            <strong style="font-size: 13px; color: {colors['neon_cyan']};">Technical Skills:</strong><br/>
            {''.join([f'<span class="skill-pill">{skill}</span>' for skill in project.get('technical_skills', [])])}
        </div>
        
        {f'''<div style="margin: 16px 0;">
            <strong style="font-size: 13px; color: {colors['neon_purple']};">Techniques:</strong><br/>
            {''.join([f'<span class="skill-pill">{tech}</span>' for tech in project.get('techniques', [])])}
        </div>''' if project.get('techniques') else ''}
        
        <div style="margin: 16px 0;">
            {''.join([f'<span style="background: linear-gradient(135deg, {colors["neon_pink"]}, {colors["neon_purple"]}); color: white; padding: 4px 12px; border-radius: 12px; font-size: 11px; margin-right: 8px; display: inline-block;">#{tag}</span>' for tag in project.get('tags', [])])}
        </div>
        
        <div style="margin-top: 16px; display: flex; gap: 12px; flex-wrap: wrap;">
            {f'<a href="{project.get("github", "#")}" target="_blank" class="neon-button" style="font-size: 14px; padding: 8px 20px;">🔗 GitHub</a>' if project.get('github') else ''}
            {f'<a href="{project.get("demo", "#")}" target="_blank" class="neon-button" style="font-size: 14px; padding: 8px 20px;">🚀 Demo</a>' if project.get('demo') else ''}
        </div>
    </div>
    """, unsafe_allow_html=True)

def ExperienceCard(experience, theme="dark"):
    colors = get_theme_colors(theme)
    
    with st.expander(f"**{experience['role']}** at {experience['company']} ({experience['duration']})"):
        st.markdown(f"""
        <div style="color: {colors['text_primary']};">
            <p style="color: {colors['text_secondary']};">{experience['description']}</p>
            
            <div style="margin: 16px 0;">
                <strong style="font-size: 14px; color: {colors['neon_cyan']};">Skills:</strong><br/>
                {''.join([f'<span class="skill-pill">{skill}</span>' for skill in experience.get('skills', [])])}
            </div>
            
            <div style="margin: 16px 0;">
                {''.join([f'<span style="background: linear-gradient(135deg, {colors["neon_cyan"]}, {colors["neon_blue"]}); color: white; padding: 4px 12px; border-radius: 12px; font-size: 11px; margin-right: 8px; display: inline-block;">#{tag}</span>' for tag in experience.get('tags', [])])}
            </div>
        </div>
        """, unsafe_allow_html=True)

def ResearchCard(research, theme="dark"):
    colors = get_theme_colors(theme)
    
    status_class = {
        "published": "status-published",
        "draft": "status-draft",
        "in progress": "status-progress"
    }.get(research.get('status', '').lower(), "status-draft")
    
    st.markdown(f"""
    <div class="tech-card">
        <h3 style="margin-top: 0;">{research['title']}</h3>
        <span class="status-badge {status_class}">{research.get('status', 'Draft')}</span>
        
        <p style="color: {colors['text_secondary']}; margin-top: 16px;">
            {research.get('abstract', '')[:200]}{'...' if len(research.get('abstract', '')) > 200 else ''}
        </p>
        
        <div style="margin: 16px 0;">
            {''.join([f'<span class="skill-pill">{tag}</span>' for tag in research.get('tags', [])])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if research.get('links'):
        links = research['links']
        cols = st.columns(len(links))
        for i, (link_type, link_url) in enumerate(links.items()):
            if link_url:
                with cols[i]:
                    st.markdown(f"[📄 {link_type.upper()}]({link_url})")
    
    with st.expander("Read Full Abstract"):
        st.write(research.get('abstract', ''))

def NewsCard(news, theme="dark"):
    colors = get_theme_colors(theme)
    
    st.markdown(f"""
    <div class="timeline-item">
        <div style="background: linear-gradient(135deg, {colors['neon_cyan']}, {colors['neon_purple']}); color: white; padding: 6px 16px; border-radius: 20px; display: inline-block; font-size: 12px; font-weight: 600; margin-bottom: 12px;">
            {news.get('date', '')}
        </div>
        <h3 style="margin: 8px 0;">{news.get('title', '')}</h3>
        <p style="color: {colors['text_secondary']};">{news.get('content', '')}</p>
        <div style="margin-top: 12px;">
            {''.join([f'<span style="background: {colors["bg_secondary"]}; border: 1px solid {colors["neon_cyan"]}; padding: 4px 12px; border-radius: 12px; font-size: 11px; margin-right: 8px; display: inline-block;">#{tag}</span>' for tag in news.get('tags', [])])}
        </div>
    </div>
    """, unsafe_allow_html=True)

def SkillCard(title, skills, icon, theme="dark", animate=False):
    colors = get_theme_colors(theme)
    
    # Use skill-animate class if animate=True, otherwise use skill-pill
    skill_class = "skill-animate" if animate else "skill-pill"
    
    st.markdown(f"""
    <div class="tech-card">
        <h3 style="margin-top: 0;">{icon} {title}</h3>
        <div style="margin-top: 16px;">
            {''.join([f'<span class="{skill_class}">{skill}</span>' for skill in skills])}
        </div>
    </div>
    """, unsafe_allow_html=True)
