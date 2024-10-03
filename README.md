# Vocabulary Quiz Program

## Description

This Python program allows students to test their vocabulary skills by translating words between English and French. The program uses a CSV file to store vocabulary words, including the number of errors made during previous quizzes. Users can choose the direction of translation, select between all available words or a random sample, and keep track of their progress.

## Features

- **CSV Handling**: Read and write vocabulary words from/to a CSV file.
- **Multiple Modes**: Test yourself in different translation directions:
  - English to French
  - French to English
  - Mixed
- **Error Tracking**: Keep track of the number of errors made for each word to focus on areas needing improvement.
- **Random Selection**: Option to select a random subset of words for quizzes.

## Requirements

- Python 3.x
- Vocabulary Lists

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Clone or download this repository.
3. Save your vocabulary words in a CSV file named `filename.csv` or any name you prefer, ensuring it follows the format:
```csv
   English,French,Errors 
   word1,translation1,0 
   word2,translation2,0
```
## Usage

1. Run the program:
```bash
python vocabulary_quiz.py
```
2. Follow the prompts:
    - Enter the name of your CSV file (e.g., mots.csv).
    - Select the quiz mode:
        1: Translate from English to French
        2: Translate from French to English
        3: Mixed
    - Choose to answer all questions or a random selection.
    - Specify the number of words if selecting randomly.

3. Answer the quiz questions:
    - Type your translation and press Enter.
    - Receive feedback on your answer, including the option to accept minor errors.

4. At the end of the quiz, your score will be displayed, and the updated errors will be saved back to the CSV file.

# Contributing
Contributions are welcome! If you have suggestions for improvements or features, don't hesitate to reach me out at Corentin.BESQUEUT@etu.isima.fr

