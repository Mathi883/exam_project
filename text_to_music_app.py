# Reference: https://github.com/AIAnytime/Text-to-Music-Generation-App/blob/main/app.py
import os
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy
import streamlit as st
import datetime  # for timestamp
from helpers import display_music

# libraries we need to install
# 1. torch: https://pypi.org/project/torch/
# 2. transformers: https://pypi.org/project/transformers/
# 3. scipy: https://scipy.org/

def text_to_music_AI():
    # create an expander
    with st.expander("See explanation"):
        st.write("Music Generator app using Meta's Music Gen Small model."
                 "More information on the model can be found [here](https://huggingface.co/facebook/musicgen-small)."
                 "Credit for inspiring this work and the streamlit app code goes to [AIAnytime](https://github.com/AIAnytime/Text-to-Music-Generation-App/tree/main).")

    # create a box for user
    prompt = st.text_area("What are you in the mood to listen to.......")
    time_slider = st.slider("Select time duration (In seconds)", 0, 20, 10)
    duration = round(time_slider * (256 / 5))

    if prompt and time_slider:
        # use processor + generate code to create audio files
        model_name = "facebook/musicgen-small"
        processor = AutoProcessor.from_pretrained(model_name)
        model = MusicgenForConditionalGeneration.from_pretrained(model_name)

        inputs = processor(
            text=prompt,
            # we need to add these arguments, otherwise the text can not be converted to music
            padding=True,
            return_tensors="pt"
        )

        # to adjust the duration, play with the max new tokens
        audio_values = model.generate(**inputs, max_new_tokens=duration)

        # you could potentially adjust this, the number of samples per second
        sampling_rate = model.config.audio_encoder.sampling_rate

        # create a timestamp
        current_datetime = datetime.datetime.now()
        current_timestamp = current_datetime.timestamp()

        # write the generated music to the folder
        # create folder if necessary
        directory = "music"
        if not os.path.exists(directory):
            os.makedirs(directory)

        scipy.io.wavfile.write(f"music/musicgen_out_{current_timestamp}.wav",
                               rate=sampling_rate,
                               data=audio_values[0, 0].numpy())
        # read the file
        audio_filepath = f"music/musicgen_out_{current_timestamp}.wav"
        # play in the app
        display_music(audio_filepath)

