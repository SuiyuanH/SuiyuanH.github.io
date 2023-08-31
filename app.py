from flask import Flask, render_template, request
from gltr_utils import gen_input

app = Flask(__name__)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    data = gen_input ()
    options = ["human", "machine"]
    user_answer = None

    if request.method == 'POST':
        user_answer = request.form.get('answer')

    return render_template('quiz.html', data=data, options=options)

if __name__ == '__main__':
    app.run(debug=True)