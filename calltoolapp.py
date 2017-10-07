from flask import Flask, render_template, request, redirect, url_for, redirect
from func import *

app = Flask(__name__, static_url_path='/Users/igorartaran/Documents/LearnPython/CallToolProject/static/')

@app.route('/')
def index():
    return render_template('/index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login_page():
#     name = None
#     error = None
#     if request.method == 'POST':
#         name = request.form.get('name')
#         error = len(name) < 10
#         if not error:
#             return redirect(url_for('index'))
#     return render_template('/login.html', name=name, error=error)

@app.route('/main')
def main_page():
    get_externaldb()
    return render_template('/main.html', call_table = return_info('waiting'))

@app.route('/take_in_hand/<login>', methods=['POST'])
def take_in_hand(login):
    work_taken(login, login)
    return redirect(url_for('main_page'))

@app.route('/working')
def working():
    get_externaldb()
    return render_template('/working.html', call_table = return_info('work_with'))

@app.route('/dobi_is_free/<login>', methods=['POST'])
def dobi_is_free(login):
    job_done(login, login)

    return redirect(url_for('working'))

@app.route('/return_to_queue/<login>', methods=['POST'])
def return_to_queue(login):
    return_to_queue(login, login)

    return redirect(url_for('working'))

@app.route('/free')
def free_page():
    get_externaldb()
    return render_template('/free.html', call_table = return_info('free'))

# @app.route('/take_in_hand/<login>', methods=['POST'])
# def take_in_hand(login):
#     work_taken(login, login)
#     print(login)
#     return redirect(url_for('free_page'))


@app.route('/analytics')
def analytics_and_metrika():
    return render_template('/analytics.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error.html')
    

if __name__ == "__main__":
    app.run(port = 5010, debug = True)



