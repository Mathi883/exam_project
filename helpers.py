import streamlit as st


def display_music(audio_filepath):
    audio_file = open(audio_filepath, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)