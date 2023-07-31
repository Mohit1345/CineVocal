# CineVocal - Your Audio Movie Summarizer

![CineVocal Logo](header_image.png)

## Overview

CineVocal is an innovative Python-based project that generates audio movie summaries, offering a delightful and convenient way to explore the world of cinema. This README provides a guide on how to set up CineVocal and use it to enjoy engaging movie insights.

### Checkout some already generated movie explanation audios
https://cinevocal-home.streamlit.app/

## Installation

To get started with CineVocal, follow these steps:

1. Clone the CineVocal repository to your local machine.

```bash
git clone [https://github.com/YourUsername/CineVocal.git](https://github.com/mohit1345/cinevocal)
```

2.Install requirements
```bash
pip install -r requirements.txt
```

3.Obtain API keys for the following services and add them to a .env file in the project directory:
Cohere API: https://cohere-ai.readme.io/ <br>
Eleven Labs API: https://elevenlabs.io/ <br>
OMDB API: https://www.omdbapi.com/apikey.aspx<br>
Make sure to include the API keys in the .env file using the following format:
```bash
COHERE_API_KEY=your_cohere_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
OMDB_API_KEY=your_omdb_api_key
```

4.Run streamlit app
```bash
streamlit run main.py
```

5.To look all created audios in gallery formate 
```bash
streamlit run home.py
```

## Video tutorial
[Click here to watch the CineVocal Video](https://drive.google.com/file/d/1KBnkZPgF-sIxJq54zgcwFTytncsyRkEi/view?usp=sharing)

## checkout Presentation to look into details over its use cases and diffferent aspecs
[Click here to open the CineVocal presentation](https://gamma.app/docs/CineVocal-Audio-Summaries-of-Your-Favorite-Movies-ltbhor87qf4f9zh)

