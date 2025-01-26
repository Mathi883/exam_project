import streamlit as st
from page_definitions import lyrics_writing
from page_definitions import intro_page
from page_definitions import music_theory_page
from page_definitions import feedback_page
from page_definitions import music_ai
from registration_page import connect_to_mongo
from registration_page import register



connect_to_mongo()

placeholder = st.empty()

if 'count' not in st.session_state:
    st.session_state.count = 0

def skip_register():
    st.session_state.count = 2
    placeholder.empty()

if st.session_state.count == 0:

    register()
    skip_register_button = st.button('Dive in!', on_click=skip_register)


elif st.session_state.count == 2:
    placeholder.empty()
    options = ['Introduction', '✏️ Lyrics', '🔎 Music Theory & Quiz','🎸 Music AI Tool', '📝 Feedback']
    page_selection = st.sidebar.selectbox("Menu", options)

    if page_selection == "Introduction":
        intro_page()
    elif page_selection == "✏️ Lyrics":
        lyrics_writing()
    elif page_selection == "🔎 Music Theory & Quiz":
        music_theory_page()
    elif page_selection == "🎸 Music AI Tool":
        music_ai()
    elif page_selection == "📝 Feedback":
        feedback_page()


#TODO: Maybe add Tabs in the pages (Music Theory page, Projects)
#TODO: Submit Button muss zweimal gedrückt werden
#TODO: Die App so gestalten, dass sie tatsächlich Spaß macht und nicht nur random Funktionen hat
