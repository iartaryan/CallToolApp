import pymysql
from datetime import datetime as dt, date, time, timedelta

try:
    from settings_local import *
except ImportError:
    pass

day_min = 1440
day_count = 2

calls_dict = {}
#Вычисление времени сессии
def timer_function(session_time):

    seychas = '{:%Y-%m-%d %H:%M:%S}'.format(dt.now())
    seychas = dt.strptime(seychas,'%Y-%m-%d %H:%M:%S')
    timer = seychas - timedelta(minutes=session_time)
    return timer

def get_externaldb():

    try:
        db = pymysql.connect(host = EXTENAL_DB['host'], user = EXTENAL_DB['user'], passwd = EXTENAL_DB['passwd'], db = EXTENAL_DB['db'], port = EXTENAL_DB['port'])
        cursor = db.cursor()
        #получить последнее значение SELECT calldate FROM cdr ORDER BY calldate DESC LIMIT 1
        cursor.execute('SELECT src,calldate FROM cdr WHERE calldate > ' + '"' +str(timer_function(day_min))+'" ORDER BY calldate DESC')

        for i in cursor.fetchall():
            calls_dict.update({i[0]:i[1]})
        return calls_dict

    except pymysql.err.OperationalError:
        return 'Some connection problems'

print(get_externaldb())