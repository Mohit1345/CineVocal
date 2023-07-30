# import streamlit as st
# from movie_info import fetch_movie_data
# from movie_wiki import extract_movie_plot
# from movie_info2 import plot
# from script_cohere import scripter
# from voice import voiceover
# from poster import get_poster
# import time
# import os
# from dotenv import load_dotenv
# load_dotenv()





# def main():
#     header_image = "header_image.jpg"
#     st.image(header_image, use_column_width=True)
#     st.title("Movie AudioBook Generator")
#     name = st.text_input("Enter the name of the movie:")
#     if st.button("Generate Audio"):
#         movie_data = fetch_movie_data(name)
#         movie_plot = plot(name)
#         if extract_movie_plot(name) is not None:
#             movie_plot = movie_plot + extract_movie_plot(name)
#         # st.write(movie_plot)
#         # with st.spinner("Generating audio..."):
#         get_poster(movie_data['Title'])
#         progress_bar = st.progress(0)
#         script = scripter(movie_data['Title'], movie_data['Year'], movie_data['Genre'], movie_plot)

#         # st.write(script)
#         # st.write(movie_data['Genre'])
#         voiceover(script, movie_data['Title'], movie_data['Genre'])

#         for i in range(100):
#             time.sleep(0.1)
#             progress_bar.progress(i + 1)
#         st.success("Audio generated successfully!")
#         audio_file = open(f'audio_generated/{movie_data["Title"]}.mp3', 'rb')
#         audio_bytes = audio_file.read()

#         st.audio(audio_bytes, format='audio/mp3')
#     st.write()
#     audio_files = os.listdir("audio_generated")
#     st.header("Listen to some already generated movie explanations: ")
#         # Display each audio file in a loop
#     for audio_file in audio_files:
#         if audio_file.endswith(".mp3"):

#             audio_name = os.path.splitext(audio_file)[0]


#             movie_poster = f"posters/{audio_name}.jpg"
#             st.image(movie_poster, width=200)
#             st.write(f"**{audio_name}**")
#             st.audio(open(os.path.join("audio_generated", audio_file), 'rb').read(), format='audio/mp3')




# if __name__ == "__main__":
#     main()

import streamlit as st
from movie_info import fetch_movie_data
from movie_wiki import extract_movie_plot
from movie_info2 import plot
from script_cohere import scripter
from voice import voiceover
from poster import get_poster
import time
import os
from dotenv import load_dotenv
load_dotenv()

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

    header_image = "header_image.jpg"
    st.image(header_image, use_column_width=True)

    name = st.text_input("Enter the name of the movie:")
    if st.button("Generate Audio"):
        movie_data = fetch_movie_data(name)
        movie_plot = plot(name)
        if extract_movie_plot(name) is not None:
            movie_plot = movie_plot + extract_movie_plot(name)
        get_poster(movie_data['Title'])
        progress_bar = st.progress(0)
        script = scripter(movie_data['Title'], movie_data['Year'], movie_data['Genre'], movie_plot)

        voiceover(script, movie_data['Title'], movie_data['Genre'])

        for i in range(100):
            time.sleep(0.1)
            progress_bar.progress(i + 1)
        st.success("Audio generated successfully!")
        audio_file = open(f'audio_generated/{movie_data["Title"]}.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/mp3')

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
