import tornado.ioloop
import tornado.web

try:
    from settings_local import *
    from func import *
except ImportError:
    pass

class check_DB_info(tornado.web.Application):
    def user_in_db(self):
        processing_info(get_externaldb())

if __name__ == "__main__":
    timer_app = check_DB_info([])
    tornado.ioloop.PeriodicCallback(timer_app.user_in_db, 1000*60*PERIOD).start()
    tornado.ioloop.IOLoop.current().start()