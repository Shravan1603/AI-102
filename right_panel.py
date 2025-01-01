# right_panel.py

import streamlit as st

def render_right_panel(selected_topic, selected_subtopic, selected_sub_subtopic):
    st.markdown('<p class="panel-title">Selected Values</p>', unsafe_allow_html=True)
    st.markdown(f"**<span style='color:#4CAF50'>Topic:</span>** {selected_topic}", unsafe_allow_html=True)
    st.markdown(f"**<span style='color:#4CAF50'>Subtopic:</span>** {selected_subtopic}", unsafe_allow_html=True)
    st.markdown(f"**<span style='color:#4CAF50'>Sub-Subtopic:</span>** {selected_sub_subtopic}", unsafe_allow_html=True)
