from flask import Flask, render_template, url_for, flash, redirect
from form import XMLQuestionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/home/', methods=['GET', 'POST'])
def home():
    form = XMLQuestionForm()


    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)