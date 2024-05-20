from langchain.prompts import PromptTemplate
from langchain_community.llms import Together

from decouple import config
import time
import os

import Prompt_Template
import QuestionAnswerGen

# Load environment variables
together_api_key = config("together_api_key")
os.environ["together_api_key"] = together_api_key


def generate_questions_answers(file_path, file_type, num_questions, language):

    start_time = time.time()

    llm = Together(
        model="meta-llama/Llama-3-70b-chat-hf",
        temperature=0.7,
        max_tokens=128,
        top_k=1,
        together_api_key=together_api_key
    )

    quesitons = QuestionAnswerGen.Question_Answer(file_path, file_type, num_questions, language)

    QUESTION_PROMPT_TEMPLATE = PromptTemplate(template=Prompt_Template.format_question_template, input_variables=["text", "language"])
    question_prompt = QUESTION_PROMPT_TEMPLATE.format(text=quesitons, language=language)
    results_question = llm(question_prompt)

    ANSWER_PROMPT_TEMPLATE = PromptTemplate(template=Prompt_Template.format_answer_template, input_variables=["text", "language"])   
    answer_prompt = ANSWER_PROMPT_TEMPLATE.format(text=quesitons, language=language)
    results_answer = llm(answer_prompt)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    # print(f"Processing time: {elapsed_time} seconds")
    
    return results_question, results_answer



# # make sur to uncomment this lines to test if this function works well

# PATH_FILE = "D:\HAMZA M2\Lettre_Recommandation.pdf"
# TYPE_FILE = "Normal File" # File type (normal or scanned)
# NUM_QUESTION = 5  # Example number of questions
# LANGUAGE = "Frensh" # Example of LANGUAGE question

# results_question, results_answer = generate_questions_answers(PATH_FILE, TYPE_FILE, NUM_QUESTION, LANGUAGE)
# print(results_question)
# print("------------------------------------------------------------")
# print(results_answer)