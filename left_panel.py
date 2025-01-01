# left_panel.py

import streamlit as st
from ai_102_topics import ai_102_topics  # Import the dictionary from the external file

def render_left_panel():
    # Set up the layout for the sidebar panel
    st.sidebar.markdown('<h1 style="color: #4CAF50; font-size: 24px;">Azure AI-102</h1>', unsafe_allow_html=True)
    # st.sidebar.markdown('<p class="panel-title">Select a Topic</p>', unsafe_allow_html=True)

    # Prepare the subtopics dictionary from the imported ai_102_topics
    subtopics_dict = get_subtopics_dict()

    # Dropdown for topics in the sidebar
    selected_topic = st.sidebar.selectbox("Choose a Topic", list(subtopics_dict.keys()))

    # Dropdown for subtopics based on selected topic in the sidebar
    subtopics = subtopics_dict[selected_topic]
    selected_subtopic = st.sidebar.selectbox("Choose a Subtopic", list(subtopics.keys()))

    # Dropdown for sub-subtopics based on selected subtopic in the sidebar
    sub_subtopics = subtopics[selected_subtopic]
    selected_sub_subtopic = st.sidebar.selectbox("Choose a Sub-Subtopic", sub_subtopics)

    return selected_topic, selected_subtopic, selected_sub_subtopic


def get_subtopics_dict():
    subtopics_dict = {}
    for topic, subtopics in ai_102_topics.items():
        subtopics_dict[topic] = {subtopic[0]: subtopic[2] for subtopic in subtopics}
    return subtopics_dict
