import FormatQuestionAnswer
import IncorrectAnswerGen
import time


def QuizGeneration(file_path, file_type, num_question, language):

    start_time = time.time()

    # generate question and Answer
    QuestionList, AnswerList = FormatQuestionAnswer.generate_questions_answers(file_path, file_type, num_question, language)

    # generate incorrect Answer
    IncorrectAnswers = IncorrectAnswerGen.generate_incorrect_response(QuestionList, AnswerList)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"Processing time: {elapsed_time} seconds")

    return QuestionList, AnswerList, IncorrectAnswers


# make sur to uncomment this lines to test if this function works well

PATH_FILE = "D:\HAMZA M2\LM_Hamza_Moumad.pdf"
TYPE_FILE = "Normal File" # File type (normal or scanned)
NUM_QUESTION = 5  # Example number of questions
LANGUAGE = "Frensh" # Example of LANGUAGE question

questions, AnswerList, IncorrectAnswers = QuizGeneration(PATH_FILE, TYPE_FILE, NUM_QUESTION, LANGUAGE)
print(questions)
print("------------------------------------------------------------")
print(AnswerList)
print("------------------------------------------------------------")
print(IncorrectAnswers)