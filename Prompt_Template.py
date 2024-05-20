Prompt_Template = """
----------------------
Text: {text}
----------------------

You are an expert Question/Answer maker. Given the above text, it is your job to\
create a quiz of {num_questions} Questions with there Anwers in {language} language.

Make sure that questions are not repeated and check all the questions to be conforming to the text as well.
Make sure to format your response like the LIST_IMBRIQUE below and use it as a guide.\

Ensure to make the {num_questions} Couple of Qestion/Answer using {language} language.

### LIST_IMBRIQUE

lIST = [["Question": "Put the question here", "Answer": "Put the Answer here"]["Question": "Put the question here", "Answer": "Put the Answer here"]["Question": "Put the question here", "Answer': "Put the Answer here"]
"""

Refine_Template = """

You are an expert in creating practice Questions/Answers based on study material. Your goal is to help a student prepare for an exam.\

As an expert {language} grammarian and writer.\
We have received some practice questions/Answers to a certain extent, refine this:\
-------------------------
{existing_answer}.
-------------------------.

with {num_questions} questions/Answers in {language} language.\

If Questions/Answers above are not generated with {language} language and number of elements is more or less than {num_questions}, \
update the Questions/Answers above which need to be changed and change the number of questions to {num_questions} emelents and language to {language}.\

I want as an output just the quiz, please don't provide any explaination.\
please make sure to respect this format and don't provide any supplementary information :\

lIST = [["Question": "Put the question here", "Answer": "Put the Answer here"]["Question": "Put the question here", "Answer": "Put the Answer here"]["Question": "Put the question here", "Answer': "Put the Answer here"]
]
"""

format_question_template = """

You are an expert in formating {language} text and Enlarging text
Extract questions from the provided text.
------------------------------
{text}
------------------------------
if the question is not terminate just ignore it and don't retrun it.\
Make sure not to forget any question i want just the questions as output.\
QUESTIONS:
"""

format_answer_template = """

the text provide is in this format:\
-----------------------------------
lIST = [["Question": "Put the question here", "Answer": "Put the Answer here"]["Question": "Put the question here", "Answer": "Put the Answer here"]["Question": "Put the question here", "Answer': "Put the Answer here"]
-----------------------------------

You are an expert in formating {language} text and Enlarging text
Based on the Format above, extract Answer from the provided text.
------------------------------
{text}
------------------------------

Can you please after extracting all the answers change them to a good sentancences in {language} to exprime this answer.\
And make sure not to provide any explaination.\

Please provide only one sentance for each question, and make sure not to return any question i want just the ansers.\

SENTENCES_ANSWER:
"""