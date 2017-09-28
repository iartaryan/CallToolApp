from db_lib import *

User.add_users('Igor2', 'Artaryan2', 'archi2', 'pass1', 'a@a.ru', '12312312312', 'config_engin', 'frees2')

print(User.query_info('last_name', 'Artaryan1'))
print('*********************')
print('ALL:', '\n', User.query_info_all())