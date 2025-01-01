# main.py

import streamlit as st
from left_panel import render_left_panel
from right_panel import render_right_panel

def main():
    # Load custom CSS
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    # Set up the layout for the main content area
    col1, col2 = st.columns([1, 2])

    # Left panel (Sidebar)
    with st.sidebar:
        selected_topic, selected_subtopic, selected_sub_subtopic = render_left_panel()

    # Right panel (Main content area)
    with col2:
        render_right_panel(selected_topic, selected_subtopic, selected_sub_subtopic)

if __name__ == "__main__":
    main()
