from db_lib import User, Logggggs
import db_lib as db
from datetime import datetime

try:
    from settings_local import *
except ImportError:
    pass

def find_spec_user(user_login):
    spec_user = User.query.filter(User.login == user_login).first()
    return spec_user

def check_user_status(user_login):
     try:
         user_in_action = User.query.filter(User.login == user_login).first()
         return user_in_action.status
     except AttributeError:
         #Тут происходит заполение базы пользователей неизвестными позвонившими
         User.add_users('unknown', 'unknown', user_login, 'unknown', 'unknown', user_login, 'unknown')
         check_user_status(user_login)

#Создать единую функцию изменения статусов
def change_status(user_login, new_user_status):
    try:
        user_in_action = User.query.filter(User.login == user_login).first()
        user_in_action.status = new_user_status
        db.db_session.commit()
    except AttributeError:
        pass

#Обозначаем юзеров свободными в начале рабочего дня
def user_free(user_login):
    change_status(user_login, STATUS_FREE)

def user_called(user_login):
    change_status(user_login, STATUS_WAITING)
    Logggggs.add_logs(T1=datetime.now(), login=user_login, action=ACTION_CALL)

def work_taken(user_login, user_login_c_ngn):
    change_status(user_login, STATUS_WORK_W)
    change_status(user_login_c_ngn, STATUS_WORK_W)
    Logggggs.add_logs(T2=datetime.now(), login=user_login, action=ACTION_J_START, companion=user_login_c_ngn)

def job_done(user_login, user_login_c_ngn):
    change_status(user_login, STATUS_FREE)
    change_status(user_login_c_ngn, STATUS_FREE)
    Logggggs.add_logs(T3=datetime.now(), login=user_login, action=ACTION_DONE, companion=user_login_c_ngn)

#возврат в очередь
def return_to_queue(user_login, user_login_c_ngn):
    change_status(user_login, STATUS_READY)
    change_status(user_login_c_ngn, STATUS_FREE)
    Logggggs.add_logs(T3=datetime.now(), login=user_login, action=ACTION_RETURN_TO_Q, companion=user_login_c_ngn)

#Вычисление времени сессии
def timer_function(session_time):
    from datetime import datetime as dt, date, time, timedelta
    
    last_Log = Logggggs.query.order_by(Logggggs.T0.desc()).first()
    timer = '{:%Y-%m-%d %H:%M:%S}'.format(last_Log.T0)
    
    # seychas = '{:%Y-%m-%d %H:%M:%S}'.format(dt.now())
    # seychas = dt.strptime(seychas,'%Y-%m-%d %H:%M:%S')
    # timer = seychas - timedelta(minutes=session_time)
    print(str(timer))
    return str(timer)

def get_externaldb():
    import pymysql
    calls_dict = {}
    work_list, free_users, waiting_users, working_users, ready_to_work = [], [], [], [], []
    
    try:
        db = pymysql.connect(host = EXTENAL_DB['host'], user = EXTENAL_DB['user'], passwd = EXTENAL_DB['passwd'], db = EXTENAL_DB['db'], port = EXTENAL_DB['port'])
        cursor = db.cursor()
        #получить последнее значение SELECT calldate FROM cdr ORDER BY calldate DESC LIMIT 1
        cursor.execute('SELECT src,calldate FROM cdr WHERE calldate > ' + '"' +timer_function(600)+'" ORDER BY calldate DESC')
        phone_and_date = cursor.fetchall()

        return phone_and_date
    except pymysql.err.OperationalError:
        print('Some connection problems')

def return_info(info):
    all_users = User.query.filter(User.status == info).all()
    users = {}
    
    try: 
        for user_info in all_users:
            log_query = Logggggs.query.filter(Logggggs.login == user_info.login)

            if user_info.status == STATUS_FREE:
                last_Log = log_query.order_by(Logggggs.T3.desc()).first()
                users.update({user_info.login: last_Log.T3})
                #users[user_info.login] = last_Log.T3
            elif user_info.status == STATUS_WAITING:
                last_Log = log_query.order_by(Logggggs.T1.desc()).first()
                users.update({user_info.login:last_Log.T1})
            elif user_info.status == STATUS_WORK_W:
                last_Log = log_query.order_by(Logggggs.T2.desc()).first()
                users.update({user_info.login:last_Log.T2})
            elif user_info.status == STATUS_READY:
                last_Log = log_query.order_by(Logggggs.T3.desc()).first()
                users.update({user_info.login:last_Log.T3})
        
        return users
    except AttributeError:
        return 'NoLogs'

def processing_info(call_work_list):
    for user_info in call_work_list:
        user_info_status = check_user_status(user_info[0])
        if user_info_status == STATUS_FREE:
            user_called(user_info[0])










