from langchain_community.llms import Together
from decouple import config
import time
import os

# Load environment variables
together_api_key = config("together_api_key")
os.environ["together_api_key"] = together_api_key

def generate_incorrect_response(question, answer):

    start_time = time.time()

    llm = Together(
        model="meta-llama/Llama-3-70b-chat-hf",
        temperature=0.7,
        max_tokens=128,
        top_k=1,
        together_api_key=together_api_key
    )

    Prompt = f"""You are an expert in generating incorrect answers. Please provide two other incorrect responses generate just 2 that are plausible but not correct to the following question:\
        
    Question: '{question}' 
    \nCorrect Answer: '{answer}' 

    Generate two incorrect responses to the question '{question}' 
    based on the correct answer '{answer}' 
    In order to make a MCQ generate big differents answers that are not correct.\
    please make sure  to Do not include any supplementary informations like the correct answer or explanation of modefications.
    Answer 1 : 
    Answer 2 :
    """

    response = llm(Prompt)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    # print(f"Processing time: {elapsed_time} seconds")
    
    return response



# question = "Who are you ?"
# answer = "i'm a human and i i'm 23 years old."

# incorrect_answer = generate_incorrect_response(question, answer)
# print(incorrect_answer)