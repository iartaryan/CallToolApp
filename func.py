from db_lib import User, Logggggs
import db_lib as db
from datetime import datetime

def query_info(field_name, specific_info):
    return User.query.filter(getattr(User, field_name) == specific_info).all()

#Создать единую функцию изменения статусов и логирования
def change_status(id_from_telegram, new_user_status):
    user_in_action = User.query.filter(User.telegram_id.like(id_from_telegram)).first()
    user_in_action.status = new_user_status
    db.db_session.commit()

#Обозначаем юзеров свободными в начале рабочего дня
def user_free(id_from_telegram):
    change_status(id_from_telegram, 'free')

def user_called(id_from_telegram):
    change_status(id_from_telegram, 'waiting')

    Logggggs.add_logs(T1 = datetime.now(), telegram_id = id_from_telegram, action = 'called')

def work_taken(id_from_telegram, id_from_telegram_c_ngn):
    change_status(id_from_telegram, 'work_taken')
    change_status(id_from_telegram_c_ngn, 'work_with')

    Logggggs.add_logs(T2 = datetime.now(), telegram_id = id_from_telegram, action = 'work_with', companion = id_from_telegram_c_ngn)

def job_done(id_from_telegram, id_from_telegram_c_ngn):

    change_status(id_from_telegram, 'ready_to_work')
    change_status(id_from_telegram_c_ngn, 'ready_to_work')

    Logggggs.add_logs(T3 = datetime.now(), telegram_id = id_from_telegram, action = 'job_done', companion = id_from_telegram_c_ngn)

#возврат в очередь
# def return_to_queue(id_from_telegram, id_from_telegram_c_ngn):

#     change_status(id_from_telegram, 'ready_to_work')
#     change_status(id_from_telegram_c_ngn, 'ready_to_work')

#     Logggggs.add_logs(T3 = datetime.now(), telegram_id = id_from_telegram, action = 'job_done', companion = id_from_telegram_c_ngn)

