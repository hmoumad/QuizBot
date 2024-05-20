from decouple import config
from langchain_together import Together
import os


# Load environment variables
together_api_key = config("together_api_key")
os.environ["together_api_key"] = together_api_key

def Load_LLM():
    llm = Together(
        model="meta-llama/Llama-3-70b-chat-hf", 
        temperature=0.7,
        max_tokens=128,
        top_k=1,
        together_api_key=together_api_key
    )
    return llm


