# CineVocal - Your Audio Movie Summarizer

![CineVocal Logo](header_image.png)

## Overview

CineVocal is an innovative Python-based project that generates audio movie summaries, offering a delightful and convenient way to explore the world of cinema. This README provides a guide on how to set up CineVocal and use it to enjoy engaging movie insights.

## Table of Contents

1. [Installation](#installation)
2. [Getting API Keys](#getting-api-keys)
3. [Running CineVocal](#running-cinevocal)
4. [User Interaction](#user-interaction)
5. [Prospects and Applications](#prospects-and-applications)
7. [Contact](#contact)

## Installation

To get started with CineVocal, follow these steps:

1. Clone the CineVocal repository to your local machine.

```bash
git clone https://github.com/YourUsername/CineVocal.git
```

2.Install requirements
```bash
pip install -r requirements.txt
```

3.Obtain API keys for the following services and add them to a .env file in the project directory:
Cohere API: https://cohere.run/
Eleven Labs API: https://elevensight.com/
OMDB API: http://www.omdbapi.com/
Make sure to include the API keys in the .env file using the following format:
```bash
COHERE_API_KEY=your_cohere_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
OMDB_API_KEY=your_omdb_api_key
```

4.run streamlit app
```bash
streamlit run main.py
```

## Video tutorial
## Embedded Video
[Click here to watch the CineVocal Video](https://drive.google.com/file/d/1KBnkZPgF-sIxJq54zgcwFTytncsyRkEi/view?usp=sharing)

## checkout Presentation to look into details over its use cases and diffferent aspecs
[Click here to open the CineVocal presentation]
<iframe src="https://gamma.app/embed/ltbhor87qf4f9zh" style="width: 700px; max-width: 100%; height: 450px" allow="fullscreen" title="CineVocal - Audio Summaries of Your Favorite Movies"></iframe>
