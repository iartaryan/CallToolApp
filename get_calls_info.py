import pymysql
from datetime import datetime as dt, date, time, timedelta

try:
    from settings_local import *
except ImportError:
    pass

#Вычисление времени сессии
def timer_function(session_time):

    seychas = '{:%Y-%m-%d %H:%M:%S}'.format(dt.now())
    seychas = dt.strptime(seychas,'%Y-%m-%d %H:%M:%S')
    timer = seychas - timedelta(minutes=session_time)
    return str(timer)

def get_externaldb():
    calls_dict = {}
    work_list = []
    phone_list = []

    try:
        db = pymysql.connect(host = EXTENAL_DB['host'], user = EXTENAL_DB['user'], passwd = EXTENAL_DB['passwd'], db = EXTENAL_DB['db'], port = EXTENAL_DB['port'])
        cursor = db.cursor()
        #получить последнее значение SELECT calldate FROM cdr ORDER BY calldate DESC LIMIT 1
        cursor.execute('SELECT src,calldate FROM cdr WHERE calldate > ' + '"' +timer_function(43000)+'" ORDER BY calldate DESC')
        phone_and_date = cursor.fetchall()

        for phone_info in phone_and_date:
            if phone_info[0] not in work_list:
                calls_dict.update({phone_info[0]:phone_info[1]})
                work_list.append(phone_info[0])

        return calls_dict
    except pymysql.err.OperationalError:
        return 'Some connection problems'

