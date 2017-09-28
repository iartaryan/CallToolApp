from flask import Flask, render_template

app = Flask(__name__, static_url_path='/Users/igorartaran/Documents/LearnPython/CallToolProject/static/')

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/login')
def login_page():
    return render_template('/login.html')


@app.route('/main')
def main_page():
    return render_template('/main.html')


@app.route('/working')
def working():
    return render_template('/working.html')


@app.route('/free')
def free_page():
    return render_template('/free.html')


@app.route('/analytics')
def analytics_and_metrika():
    return render_template('/analytics.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error.html')
    

if __name__ == "__main__":
    app.run(port = 5010, debug = True)