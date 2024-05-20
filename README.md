# PDF Text Extraction and Quiz Generation

This repository contains scripts for extracting text from PDF files and generating quizzes. Below is a description of each file included in this repository:

## Files and Descriptions

1. **ExtractDataOCR.py**:
    - This script extracts text from scanned PDF files using Optical Character Recognition (OCR).

2. **ExtractDataPyPDF2.py**:
    - This script extracts text from normal (non-scanned) PDF files using the PyPDF2 library.

3. **FileProcessing.py**:
    - This script processes the extracted text from PDF files and splits it into manageable chunks.

4. **QuestionAnswerGen.py**:
    - This script generates questions and answers for the quiz from the processed text.

5. **FormatQuestionGen.py**:
    - This script formats the output of the `QuestionAnswerGen.py` file to extract questions and answers.

6. **IncorrectQuestionGen.py**:
    - This script generates an incorrect answer for each question to create multiple-choice quiz options.

7. **AllQuiz.py**:
    - This script calls all the functions from the above files and compiles them to generate the final quiz.

## Usage

1. **Extracting Text**:
    - Use `ExtractDataOCR.py` for scanned PDFs.
    - Use `ExtractDataPyPDF2.py` for normal PDFs.

2. **Processing Text**:
    - Run `FileProcessing.py` to split the extracted text into chunks.

3. **Generating Questions and Answers**:
    - Run `QuestionAnswerGen.py` to create quiz questions and answers.

4. **Formatting Questions and Answers**:
    - Use `FormatQuestionGen.py` to format the generated questions and answers.

5. **Generating Incorrect Answers**:
    - Run `IncorrectQuestionGen.py` to create incorrect answer options for the quiz.

6. **Generating the Final Quiz**:
    - Run `AllQuiz.py` to call all the functions and generate the complete quiz.

## Requirements

- Python 3.x
- PyPDF2
- OCR library (e.g., Tesseract)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/hmoumad/QuizBot
    ```
2. Install the required libraries:
    ```
    pip install -r requirements.txt
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.
