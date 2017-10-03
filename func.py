from db_lib import User, Logggggs
import db_lib as db
from datetime import datetime

def query_info(field_name, specific_info):
    return User.query.filter(getattr(User, field_name) == specific_info).all()

#Создать единую функцию изменения статусов и логирования
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

def check_user_status(user_login):
    try:
        user_in_action = User.query.filter(User.login.like(user_login)).first()
        return user_in_action.status
    except AttributeError:
        #Тут происходит заполение базы пользователей неизвестными позвонившими
        User.add_users('unknown', 'unknown', user_login, 'unknown', 'unknown', user_login, 'unknown')
        check_user_status(user_login)
    



