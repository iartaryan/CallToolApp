from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request

app = Flask(__name__)

app.config.update(SECRET_KEY='super_secret_key')

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'OK'
    return render_template('test.html', form=form)

app.run(port = 5010, debug = True)