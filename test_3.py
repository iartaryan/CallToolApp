from func import *

all_users = User.query.all()

# for i in all_users:
#     user_called(i.login)

# for i in all_users:
#     work_taken(i.login,i.login)

for i in all_users:
    job_done(i.login,i.login)