"""
This page contains language management functions.
"""

# Import libraries
import json
import streamlit as st

def load_translations():
    """Load translations from JSON file"""
    with open('data/translations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_text(key):
    """Get translated text for current language"""
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    translations = load_translations()
    return translations.get(st.session_state.language, {}).get(key, key)

def toggle_language():
    """Toggle between English and French"""
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    st.session_state.language = 'fr' if st.session_state.language == 'en' else 'en'