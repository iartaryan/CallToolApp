from db_lib import User, Logggggs
import db_lib as db
from datetime import datetime

try:
    from settings_local import *
except ImportError:
    pass

def find_spec_user(user_login):
    spec_user = User.query.filter(User.login.like(user_login)).first()
    return spec_user

def check_user_status(user_login):
    try:
        user_in_action = User.query.filter(User.login.like(user_login)).first()
        return user_in_action.status
    except AttributeError:
        #Тут происходит заполение базы пользователей неизвестными позвонившими
        User.add_users('unknown', 'unknown', user_login, 'unknown', 'unknown', user_login, 'unknown')
        check_user_status(user_login)
        return 'free'

#Создать единую функцию изменения статусов
def change_status(user_login, new_user_status):
    try:
        user_in_action = User.query.filter(User.login.like(user_login)).first()
        user_in_action.status = new_user_status
        db.db_session.commit()
    except AttributeError:
        pass
#Обозначаем юзеров свободными в начале рабочего дня
def user_free(user_login):
    change_status(user_login, 'free')

def user_called(user_login):
    change_status(user_login, 'waiting')
    Logggggs.add_logs(T1 = datetime.now(), login = user_login, action = 'called')

def work_taken(user_login, user_login_c_ngn):
    change_status(user_login, 'work_with')
    change_status(user_login_c_ngn, 'work_with')
    Logggggs.add_logs(T2 = datetime.now(), login = user_login, action = 'job_start', companion = user_login_c_ngn)

def job_done(user_login, user_login_c_ngn):
    change_status(user_login, 'free')
    change_status(user_login_c_ngn, 'free')
    Logggggs.add_logs(T3 = datetime.now(), login = user_login, action = 'job_done', companion = user_login_c_ngn)

#возврат в очередь
def return_to_queue(user_login, user_login_c_ngn):
    change_status(user_login, 'ready_to_work')
    change_status(user_login_c_ngn, 'free')
    Logggggs.add_logs(T3 = datetime.now(), login = user_login, action = 'return_to_q', companion = user_login_c_ngn)

#Вычисление времени сессии
def timer_function(session_time):
    from datetime import datetime as dt, date, time, timedelta
    
    # last_Log = Logggggs.query.order_by(Logggggs.T0.desc()).first()
    # timer = '{:%Y-%m-%d %H:%M:%S}'.format(last_Log.T0)
    
    seychas = '{:%Y-%m-%d %H:%M:%S}'.format(dt.now())
    seychas = dt.strptime(seychas,'%Y-%m-%d %H:%M:%S')
    timer = seychas - timedelta(minutes=session_time)
    return str(timer)

def get_externaldb():
    import pymysql
    calls_dict = {}
    work_list, free_users, waiting_users, working_users, ready_to_work = [], [], [], [], []
    try:
        db = pymysql.connect(host = EXTENAL_DB['host'], user = EXTENAL_DB['user'], passwd = EXTENAL_DB['passwd'], db = EXTENAL_DB['db'], port = EXTENAL_DB['port'])
        cursor = db.cursor()
        #получить последнее значение SELECT calldate FROM cdr ORDER BY calldate DESC LIMIT 1
        cursor.execute('SELECT src,calldate FROM cdr WHERE calldate > ' + '"' +timer_function(60)+'" ORDER BY calldate DESC')
        phone_and_date = cursor.fetchall()

        return phone_and_date
    except pymysql.err.OperationalError:
        print('Some connection problems')

def return_info(info):
    all_users = User.query.filter(User.status.like(info)).all()
    users = {}
    for i in all_users:
        if i.status == 'free':
            users.update({i.login:i.status})
        elif i.status == 'waiting':
            users.update({i.login:i.status})
        elif i.status == 'work_with':
            users.update({i.login:i.status})
        elif i.status == 'work_with':
            users.update({i.login:i.status})

    return users





