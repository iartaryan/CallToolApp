from func import *
from db_lib import User, Logggggs
import db_lib as db

#Добавление пользователей работает!
# User.add_users('Igor1', 'Artaryan1', 'Login11', 'Pass11', 'a@a.ru', '2222222', 'c_ngn')
# User.add_users('Igor2', 'Artaryan2', 'Login12', 'Pass12', 'a@a.ru', '3333333', 'c_ngn')
# User.add_users('Igor3', 'Artaryan3', 'Login13', 'Pass13', 'a@a.ru', '4444444', 'c_ngn')
# User.add_users('Igor4', 'Artaryan4', 'Login14', 'Pass14', 'a@a.ru', '5555555', 'c_ngn')

# User.add_users('Igor1', 'Artaryan1', 'Login111', 'Pass11', 'a@a.ru', '6666666', 'i_ngn')
# User.add_users('Igor2', 'Artaryan2', 'Login121', 'Pass12', 'a@a.ru', '7777777', 'i_ngn')
# User.add_users('Igor3', 'Artaryan3', 'Login131', 'Pass13', 'a@a.ru', '8888888', 'i_ngn')
# User.add_users('Igor4', 'Artaryan4', 'Login141', 'Pass14', 'a@a.ru', '9999999', 'i_ngn')

user_called('6666666')
# work_taken('6666666', '2222222')
job_done('7777777', '2222222')

print('free:')
for user in query_info('status', 'free'):
    print(user)

print('waiting:')
for user in query_info('status', 'waiting'):
    print(user)

print('jobs done:')
for user in query_info('status', 'ready_to_work'):
    print(user)