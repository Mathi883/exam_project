import streamlit as st
from registration_page import connect_to_mongo
from text_to_music_app import text_to_music_AI
import pronouncing
import random


placeholder = st.empty()


def long_hyphen():
    st.write("--------------------------------------------------------------------------------------")
def lyrics_writing():
    # List of inspirational prompts, created with CHATGPT
    prompts = {
        "Love": [
            "Write about a lost love in the rain.",
            "Describe a moment when you realized you were in love.",
            "Write lyrics about unspoken words between two lovers.",
            "Create a song about love that never came to be.",
            "Write about the bittersweet feeling of saying goodbye to someone you love."
        ],
        "Self-Discovery": [
            "Describe a journey to self-discovery.",
            "Write a song about the person you are becoming.",
            "Create lyrics about finding strength within yourself.",
            "Write about overcoming your biggest personal obstacle.",
            "Describe a moment of clarity in your life."
        ],
        "Adventure": [
            "Write about a road trip with your best friend.",
            "Create lyrics about an unexpected encounter during travel.",
            "Write a song about the thrill of exploring unknown places.",
            "Describe a time you took a risk and it paid off.",
            "Create a song about a journey that changed you forever."
        ],
        "Memories": [
            "Write a song about your favorite childhood memory.",
            "Describe a dream you had last night.",
            "Write lyrics about a nostalgic moment in time.",
            "Create a song about a memory you’ll never forget.",
            "Write about a place that feels like home to you."
        ],
        "Empowerment": [
            "Write about overcoming a challenge.",
            "Create lyrics about breaking free from limitations.",
            "Write a song about empowerment after a difficult experience.",
            "Describe the feeling of rising above negativity.",
            "Write about taking control of your own destiny."
        ]
    }

    st.title("Lyrics Writing")

    long_hyphen()

    st.subheader("Lyric Inspiration Prompts")
    category = st.selectbox("Choose a category for your prompt:", list(prompts.keys()))

    if st.button("Get Inspiration Prompt"):
        prompt = random.choice(prompts[category])
        st.write(f"Your {category} inspiration prompt: {prompt}")

    long_hyphen()

    # Using "Pronouncing" to find rhymes
    st.subheader("Rhyme Finder for Lyrics Production")

    word = st.text_input("Enter a word to find rhymes:")

    if word:
        rhymes = pronouncing.rhymes(word)
        if rhymes:
            st.write("Rhymes for:", word)
            st.markdown(rhymes)
        else:
            st.write("No rhymes found for this word.")

def intro_page():
    st.title("ZongWr!ter")
    long_hyphen()
    st.write("Welcome to Zongwr!ter, the beginner-friendly music production"
             " app. On this app you can learn something about the theory of music, how you write simple melodies"
             " and it helps getting inspiration when writing lyrics. HAVE FUN!")
    long_hyphen()

    with st.expander("More about the developer"):
        st.write("This app was developed by Mathis Schräder, a Digital Media student from Leuphana University"
                 " in Lüneburg. Since his childhood he is interested in music and producing his own songs."
                 " Currently he's working on a few songs. His goal is to publish them some day. Mathis created"
                 " this app for people who are also curious and eager to create their own music and learn something about production.")


        c1,c2, c3 = st.columns(3, vertical_alignment="center")

        with c2:
            st.image("images/mathis.JPEG")

def music_theory_page():
    st.title("Music Theory & Quiz")
    long_hyphen()
    st.write("Here you can learn something about music theory and test your knowledge"
             " with a quiz. First, watch the videos below and afterwards press on one"
             " of the quiz's")

    long_hyphen()

    c1, c2 = st.columns(2, vertical_alignment="top")

    with c1:
        harmonies = st.button("Video: Harmonies")
        container = st.container(border=True, height=300)

        if harmonies:
            with container:
                st. write("Harmonies")
                url = "https://www.youtube.com/watch?v=D2ltRa2BosE"
                st.video(url, autoplay=True, muted=True)

    with c2:
        melodies = st.button("Video: Melodies")
        container = st.container(border=True, height=300)

        if melodies:
            with container:
                st.write("Melodies")
                url = "https://www.youtube.com/watch?v=hPVR_EKp6Xs"
                st.video(url, autoplay=True, muted=True)

    c1, c2 = st.columns(2, vertical_alignment="top")

    with c1:
        rhythms = st.button("Rhythms")
        container = st.container(border=True, height=500)

        if rhythms:
            with container:
                st. write("Rhythms")
                url = "https://www.youtube.com/watch?v=6zyv0O7kfcc&list=PL5j5H06QkhxE0RK-Ormp3zgf5SGJ28zsj&index=1"
                st.video(url, autoplay=True, muted=True)

                st.write("Simple & Compound Time Signatures")
                url2 = "https://www.youtube.com/watch?v=qi6uuhU1unk&list=PL5j5H06QkhxE0RK-Ormp3zgf5SGJ28zsj&index=3"
                st.video(url2, autoplay=True, muted=True)
    with c2:
        circle_of_fifths = st.button("Video: Circle of Fifths")
        container = st.container(border=True, height=500)

        if circle_of_fifths:
            with container:
                st.write("Circle of Fifths")
                url = "https://www.youtube.com/watch?v=_LHv5WN4SiU&list=PL5j5H06QkhxE0RK-Ormp3zgf5SGJ28zsj&index=10"
                st.video(url, autoplay=True, muted=True)

                st.write("Write Songs with the Circle of Fifths")
                url2 = "https://www.youtube.com/watch?v=XNwlybb-j_M"
                st.video(url2, autoplay=True, muted=True)
    long_hyphen()

    st.write("Do you wanna test your knowledge? Choose a quiz!")

    tabs1, tabs2, tabs3, tabs4 = st.tabs(['Harmonies', 'Melodies', 'Rhythms', 'Circle of Fifths'])

    with tabs1:
        st.subheader("Harmonies Quiz")
        st.image("https://www.piano-lessons-info.com/images/xCScale-notes.jpg.pagespeed.ic.OXGK8v1VeU.jpg")
        st.write("Which is/are the Dominant Chord(s) in Major Keys")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer1 = st.button("The second and third")
        with c2:
            answer2 = st.button("The first chord")
        with c3:
            answer3 = st.button("The fifth and the seventh")

        if answer1 or answer2:
            st.write("Wrong X")
        if answer3:
            st.write("Correct! V and Vii are the dominant chords")

        long_hyphen()

        st.write("What is the main, most common cadence?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer4 = st.button("III to I")
        with c2:
            answer5 = st.button("V to I")
        with c3:
            answer6 = st.button("V to IV")

        if answer4 or answer6:
            st.write("Wrong X")
        if answer5:
            st.write("Correct! The most common cadence in music is V to I (Dominant to Tonic)")

        long_hyphen()

        st.write("What is a deceptive cadence?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer7 = st.button("I to V")
        with c2:
            answer8 = st.button("V to ii")
        with c3:
            answer9 = st.button("V to vi")

        if answer7 or answer8:
            st.write("Wrong X")
        if answer9:
            st.write("Correct! V to vi is called a deceptive cadence")

    with tabs2:
        st.subheader("Melodies Quiz")

        # Question 1
        st.write("What is an important characteristic of a memorable melody?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer10 = st.button("Use of dissonance")
        with c2:
            answer11 = st.button("Repetition and variation")
        with c3:
            answer12 = st.button("Rapid key changes")

        if answer10 or answer12:
            st.write("Wrong X")
        if answer11:
            st.write("Correct! A memorable melody often uses repetition and variation.")

        long_hyphen()

        # Question 2
        st.write("Which type of scale is most commonly associated with creating happy or uplifting melodies?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer14 = st.button("Major scale")
        with c2:
            answer13 = st.button("Minor scale")
        with c3:
            answer15 = st.button("Chromatic scale")

        if answer13 or answer15:
            st.write("Wrong X")
        if answer14:
            st.write("Correct! The major scale is often used to create happy and uplifting melodies.")

        long_hyphen()

        # Question 3
        st.write("What technique is used to make melodies more expressive?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer17 = st.button("Dynamic variation (e.g., loudness)")
        with c2:
            answer16 = st.button("Strict adherence to rhythm")
        with c3:
            answer18 = st.button("Playing all notes staccato")

        if answer16 or answer18:
            st.write("Wrong X")
        if answer17:
            st.write("Correct! Dynamic variation makes melodies more expressive.")

        long_hyphen()

        # Question 4
        st.write("What is the role of a melody in a piece of music?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer19 = st.button("To provide the harmonic foundation")
        with c2:
            answer21 = st.button("To maintain the tempo")
        with c3:
            answer20 = st.button("To create a singable and recognizable tune")

        if answer19 or answer21:
            st.write("Wrong X")
        if answer20:
            st.write("Correct! Melodies create singable and recognizable tunes.")

        long_hyphen()

    with tabs3:
        st.subheader("Rhythms Quiz")

        # Question 1
        st.write("What is rhythm in music?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer19 = st.button("The speed of the melody")
        with c2:
            answer20 = st.button("The pattern of beats and silences")
        with c3:
            answer21 = st.button("The sequence of chords")

        if answer19 or answer21:
            st.write("Wrong X")
        if answer20:
            st.write("Correct! Rhythm is the pattern of beats and silences.")

        long_hyphen()

        # Question 2
        st.write("Which of the following is an example of a compound time signature?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer22 = st.button("4/4")
        with c2:
            answer23 = st.button("6/8")
        with c3:
            answer24 = st.button("3/4")

        if answer22 or answer24:
            st.write("Wrong X")
        if answer23:
            st.write("Correct! 6/8 is a compound time signature")

        long_hyphen()

        # Question 3
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c2:
            st.image(
                "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKMAAAE2CAMAAAA6btL2AAAAeFBMVEX///8AAABBQUGRkZEqKiru7u76+vqlpaXX19eJiYno6OiBgYE9PT28vLygoKCwsLDLy8uZmZkkJCRRUVHExMQ2NjZWVlbi4uJoaGjq6upgYGC2trZbW1svLy9ubm4JCQlGRkYfHx93d3fT09MYGBhLS0uEhIRzc3OWrTqQAAAES0lEQVR4nO3bbWPhQBhG4bYEpYhSLFVFX/7/P9wKq0JmJuQ8Yz/c5+N2sq7N62R07+6sG3zU9z0PzT/symr3hx5ubXElI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDIyycgkI5OMTDKWq5H8aU/aScP181saJ6Ne53Vxf9Ri9tjfnFlvZGzPO0/3rp473ZzzBsZGd+3k/WKayc2MSfMzDNw1HN3C2Og/lAVmfcxjG1vfFwF3ylFM43zhlvgaJrGMzeuAWfNeDGPPDSjT0t7YrybMZWNMVyDRxJiMSaGJseKJGMHYfqGJuLHK/SaSET4TDYwtCyFrJO+JRsaOERE0vloROaP7LeB/MTaunIRxxqSVbibeEc+GxBLG7nQ/9GXwxzXGci+GjfnnxqxdOOiyFxbY2D47hoOCUSYPl7LGUcEGw7NRZvfFMsZu4RZPJ6Osni6ljK6n7yw3amJO9Bmd2/RLjYphfHRvdLR4NHWPsjc2PBvVDqOKT1m40yvgkPetpMw/JILR++hI94PeohjPb3e7Eu9W+4NtNO8+beowpt6t9rcf/hWwsEeH0X9nXmRjih5DFvUdxsCLfDamHod437rKuAyfDmAOYuBYv2yHvEcivruMG+9m2ystwoN6V9F0MMt/d95u5nlWsrlOx8CR3G4Wi+g8HQMnZMwrpuY2+vZTM+ahLn6F2uVZpdv+2PRt9aixh+h50m1nFHFmPD9tvEbXtCJ7fMY6HZ3zsn3F05q30JmA5t+Nd8W36c7uR19xiK8h4s9Zd7Zg9++r21kco3P15rg0t07ye68yXj45+7zAAR8Ms/GrdffoT6PcelYliVmNJDn5k2X4E6rnX08MFsPonPCUbGVP/KxIjHHNOH89qWz2956KJ+NdhGlPN2wIZb3q2KtOtF6icL32X5YpcY0QTRceIaLlymMHIhoe7LITiRJZzSCbHDGwQnl1o/AnX5DJjqz+dMnHCz8rP6NPwy/tqpOxoth75NK9+FQl8o2Buyvm467tus1O3NaGiORN0QbZwS/nfMmqqvDt9J3ToGq/fPRdaimichXm5F8R9uGuZHgV8KNpfB7mSy//zmuahv9auNFFX3C+96PuwkOtEv/7JGvcj3YWFtQNfule/2IniFfV6rmWMJbTQXqbI1xUo9Xtfb2NHxb1en3x9Dlb1/ojevIa7i/9Y0BIT36cnAAAAABJRU5ErkJggg==",
                width=70)
        st.write("What is the total value of a dotted crotchet?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer25 = st.button("One and a half beats")
        with c2:
            answer26 = st.button("Two beats")
        with c3:
            answer27 = st.button("A half beat")

        if answer26 or answer27:
            st.write("Wrong X")
        if answer25:
            st.write("Correct! A dotted crotchet has a value of 1 1/2 beats")

        long_hyphen()

        # Question 4
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c2:
            st.image("https://www.liveabout.com/thmb/yLPSBBMyZU9FDIiNKSuqlWdRMyQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/800px-Music-halfres-5baa986ac9e77c002c352acf.jpg", width=200)

        st.write("How many beats is the minim rest worth ?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer25 = st.button("Four beats long")
        with c2:
            answer26 = st.button("Two beats long")
        with c3:
            answer27 = st.button("A half beat long")

        if answer25 or answer27:
            st.write("Wrong X")
        if answer26:
            st.write("Correct! The minim rest is two beats long ")

        long_hyphen()

    with tabs4:
        st.subheader("Circle of Fifths Quiz")

        # Question 1
        st.write("What is the purpose of the Circle of Fifths?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer28 = st.button("To identify rhythms")
        with c2:
            answer29 = st.button("To visualize key relationships")
        with c3:
            answer30 = st.button("To determine melody structures")

        if answer28 or answer30:
            st.write("Wrong X")
        if answer29:
            st.write("Correct! The Circle of Fifths helps visualize key relationships.")

        long_hyphen()

        # Question 2
        st.write("Which key is directly opposite to C major on the Circle of Fifths?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer31 = st.button("F major")
        with c2:
            answer32 = st.button("G major")
        with c3:
            answer33 = st.button("A flat major")

        if answer31 or answer32:
            st.write("Wrong X")
        if answer33:
            st.write("Correct! A flat major is directly opposite to C major.")

        long_hyphen()

        # Question 3
        st.write("What is a relative minor key?")
        c1, c2, c3 = st.columns(3, vertical_alignment="top")
        with c1:
            answer34 = st.button("A key with a different tonic but the same key signature")
        with c2:
            answer35 = st.button("A key with the same tonic and different key signature")
        with c3:
            answer36 = st.button("A key with a lower pitch range")

        if answer35 or answer36:
            st.write("Wrong X")
        if answer34:
            st.write("Correct! Relative minor keys share the same key signature as their major counterparts.")

        long_hyphen()


def music_ai():
    st.title("Music AI-Tool")
    long_hyphen()
    st.write("Here you can play with a music AI. Type in some keywords and get inspiration for your own music! Press Shift + Enter to submit.")
    text_to_music_AI()

def feedback_page():

    with placeholder.form("feedback_form"):
        st.title("Feedback")
        long_hyphen()
        st.write("Please give some feedback! What would you like to see"
                 " in the next version of the app? What do you like/dislike?")
        feedback = st.text_input("Feedback", max_chars=200)
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        try:
            client = connect_to_mongo()
            db = client["streamlit"]
            collection = db["feedback"]

            document = {
                    "feedback": feedback,
                }
            collection.insert_one(document)
            st.success("Thank you!")
        except Exception as e:
            st.error(f"An error occurred: {e}")