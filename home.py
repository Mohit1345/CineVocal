
import streamlit as st

import os

def main():
    # Add a description section to explain what the website does
    st.title("Movie AudioBook Generator")
    st.markdown(
        """
        Welcome to the Movie AudioBook Generator! This tool allows you to generate an audio explanation or plot summary 
        of your favorite movies. Simply enter the name of the movie, and click the "Generate Audio" button. The tool will
        fetch movie details, generate a script based on the information, and create an audio file that you can listen to.

        Additionally, you can listen to some already generated movie explanations below. Enjoy!
        """
    )

    header_image = "header_image.png"
    st.image(header_image, use_column_width=True)


    st.write()
    audio_files = os.listdir("audio_generated")
    st.header("Listen to some already generated movie explanations: ")
    # Display each audio file in a loop
    for audio_file in audio_files:
        if audio_file.endswith(".mp3"):
            audio_name = os.path.splitext(audio_file)[0]
            movie_poster = f"posters/{audio_name}.jpg"
            st.image(movie_poster, width=200)
            st.write(f"**{audio_name}**")
            st.audio(open(os.path.join("audio_generated", audio_file), 'rb').read(), format='audio/mp3')

if __name__ == "__main__":
    main()
