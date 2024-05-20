import json
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # Process the uploaded file (generate quiz)

        # Example: Save the file to a folder
        file.save('uploads/' + file.filename)

        # get the path of file
        FILE_PATH = 'uploads/' + file.filename

        # generate questions and answers
        # question_list, answer_list, incorrect_answers_list = FilePiplines.llm_piplines(FILE_PATH)
        question_list = ["who are you", "how olde are you", "where did you study"]
        answer_list = ["im hamza", "im 23 years old", "i study @ INSEA"]
        incorrect_answers_list = ["im hamza", "im 23 years old", "i study @ INSEA"]

        # Convert lists to JSON format
        questions_json = json.dumps(question_list)
        answers_json = json.dumps(answer_list)
        Incorrect_answers_json = json.dumps(incorrect_answers_list)

        # Pass JSON data to the template
        return render_template('TableResults.html', Questions=questions_json, Answers=answers_json, Incorrect_answers=Incorrect_answers_json)

if __name__ == '__main__':
    app.run(debug=False)
