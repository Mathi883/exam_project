from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
import time

@st.cache_resource
def connect_to_mongo():
    user = st.secrets['username']
    db_password = st.secrets['password']

    uri = f"mongodb+srv://{user}:{db_password}@tb-2.nti3a.mongodb.net/?retryWrites=true&w=majority&appName=tb-2"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    return client

placeholder = st.empty()


def register():
    with placeholder.form("registration_form"):
        st.subheader("Please tell us something about you")
        age = st.number_input("Enter Age", min_value=12, step=1)
        level = st.selectbox("How advanced are you in music production?", ("Beginner", "Intermediate", "Advanced"),)
        reason_for_using_app = st.selectbox("Why do you use this app", ("Just for fun", "I want to be a succesful music producer", "I want to learn music theory"), )
        profession = st.selectbox("What is your profession", ("Student", "Teacher", "Singer/Songwriter", "Other Professions"),)
        prior_knowledge = st.selectbox("Prior Knowledge in Music Theory", ("None", "Only from school", "I know much about music theory"),)
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        try:
            client = connect_to_mongo()
            db = client["streamlit"]
            collection = db["user_infos"]

            document = {
                    "age": age,
                    "user level": level,
                    "reason for using app": reason_for_using_app,
                    "profession": profession,
                    "prior_knowledge": prior_knowledge,
                }
            collection.insert_one(document)
            st.success("Thank you! Enjoy my application🫶!")
            time.sleep(3)
            st.session_state.count = 2
        except Exception as e:
            st.error(f"An error occurred: {e}")

