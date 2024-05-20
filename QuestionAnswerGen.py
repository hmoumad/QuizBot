from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import Prompt_Template
import File_Processing
import Model_final
import time


def Question_Answer(file_path, file_type, num_questions, language):

    # Extract document text from PDF
    document_que_gen = File_Processing.File_processing(file_path, file_type)

    # load our Model LLM Llama-2
    llm_generation = Model_final.Load_LLM()

    # Update input variables to include placeholders for number and target of questions
    PROMPT_TEMPLATE = PromptTemplate(template=Prompt_Template.Prompt_Template, input_variables=["text", "num_questions", "language"])
    REFINE_PROMPT_TEMPLATE = PromptTemplate(template=Prompt_Template.Refine_Template, input_variables=["text", "existing_answer", "language", "num_questions"])

    ques_gen_chain = load_summarize_chain(
        llm=llm_generation, 
        chain_type="refine", 
        verbose=True, 
        question_prompt=PROMPT_TEMPLATE, 
        refine_prompt=REFINE_PROMPT_TEMPLATE,
        input_key="input_documents",
        output_key="output_text",
    )

    QuestionsAnswer = ques_gen_chain({"input_documents": document_que_gen, "num_questions": num_questions, "language": language}, return_only_outputs=True)


    return QuestionsAnswer


# # make sur to uncomment this lines to test if this function works well

# PATH_FILE = "D:\HAMZA M2\LM_Hamza_Moumad.pdf"
# TYPE_FILE = "Scanned File" # File type (normal or scanned)
# num_questions = 5  # Example number of questions
# language = "Frensh" # Example of language question

# questions = Question_Answer(PATH_FILE, TYPE_FILE, num_questions, language)
# print(questions)