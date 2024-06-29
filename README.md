# Sentiment Analysis

The project focuses on sentiment analysis of product reviews using natural language processing techniques. It aims to provide insights into the sentiment polarity (positive, negative, or neutral) of customer reviews to help businesses understand customer opinions about their products more effectively.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](screenshots)
- [Credits](#credits)
 
Table of Contents:

1- Installation

2- Usage


## Installation

1- Clone the repository to your local machine:

```bash
git clone https://github.com/Jbass95/codingTasks 
```

2 - Navigate to the project directory:
```bash
cd project_name
```

3 - Install the required dependencies using pip:

Pandas: 

```bash
$ pip Install pandas
```

spaCy:

```bash
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download en_core_web_sm
```

TextBlob:

```bash
$ pip install -U textblob
$ python -m textblob.download_corpora
```

4- Download the dataset and place it in the appropriate directory.

5- Run the project:

```bash
$ python sentiment_analysis.py
```


## Usage
1-Open the Python script (sentiment_analysis.py) in your preferred code editor.

2- Modify the script as needed to specify the input data source (e.g., CSV file path).

3- Run the script:
```bash
python sentiment_analysis.py
```

4- The script will preprocess the text data, analyze the sentiment of the reviews, and display the results.

5- You can customize the script to save or visualize the sentiment analysis results according to your requirements.

```bash
review1 = df['reviews.text'][0]
review2 = df['reviews.text'][1]
```

## Screenshots

![App Screenshot](https://github.com/Jbass95/codingTasks/blob/main/Screenshot1.png)

## Credits

