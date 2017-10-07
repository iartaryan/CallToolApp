from func import *
from db_lib import User, Logggggs
import db_lib as db
#user_called('+79265416640')

#users_logs = Logggggs.query.filter(Logggggs.login.like('+79265416640')).order_by(Logggggs.T1).all()

#print('Last one:',users_logs[-1])
# def rt_info():
    # users_logs = Logggggs.query.filter(Logggggs.action.like(action_in_log)).order_by(Logggggs.T1).all()
    # call_table_dict = {}
    # try:
    #     for i in users_logs:
    #         call_table_dict.update({i.login:i.T0})
    #     return call_table_dict
    # except IndexError:
    #     print('empty')
    #     return None
# user_in_action = User.query.all()
# for i in user_in_action:
#     print(i.login, i.status)
#     job_done(i.login, i.login)
#     break

# def rt_info():
#     #last_Log = Logggggs.query.filter(Logggggs.action.like('%')).order_by(Logggggs.T0).frist()
#     last_Log = Logggggs.query.order_by(Logggggs.T0.desc()).first()
#     print(last_Log.T0)

# rt_info()
# asdasd = rt_info('job_done')
# for i in asdasd:
#     print(i,asdasd[i])
# print()


print(get_externaldb())




