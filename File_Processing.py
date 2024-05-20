from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

import ExtractDataOCR as ExtractDataOCR
import ExtractDataPyPDF2 as ExtractDataPyPDF2
import time

def File_processing(FILE_PATH, FILE_TYPE):

    start_time = time.time()  # Record the start time

    # If the File input is normal we will use PyPDF2 else we will use OCR
    if FILE_TYPE == "Scanned File":
        # Extract data from uploaded file using OCR
        # print("I used OCR")
        data = ExtractDataOCR.extract_text_from_pdf(FILE_PATH)
    elif FILE_TYPE == "Normal File":
        # Extract Data from PFD using PyPDF2
        # print("I used PyPDF2")
        data = ExtractDataPyPDF2.Extract_text_pypdf2(FILE_PATH)

    question_gen = ''
    for page in data:
        question_gen += page

    splitter_ques_gen = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks_ques_gen = splitter_ques_gen.split_text(question_gen)

    document_ques_gen = [Document(page_content=t) for t in chunks_ques_gen]

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    # print(f"Processing time: {elapsed_time} seconds")

    return document_ques_gen



# # make sur to uncomment this lines to test if this function works well

# PATH_FILE = "D:\HAMZA M2\LM_Hamza_Moumad.pdf"
# TYPE_FILE = "Scanned File"

# Chunks_que = File_processing(PATH_FILE, TYPE_FILE)
# print(Chunks_que)