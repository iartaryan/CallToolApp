from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///users.sqlite')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    login = Column(String(50), unique = True)
    password = Column(String(50))
    email = Column(String(120))
    telegram_id = Column(String(50), unique = True)
    groupe = Column(String(50))
    status = Column(String(50))

    def __init__(self, first_name = None, last_name = None, login = None, password = None,
        email = None, telegram_id = None, groupe = None, status = None):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.email = email
        self.telegram_id = telegram_id
        self.groupe = groupe
        self.status = status

    def __repr__(self):
        return "User(first_name='%s', last_name='%s', login='%s', password='%s', email='%s', telegram_id='%s', groupe='%s', status='%s')" % (self.first_name,
        self.last_name, self.login, self.password, self.email, self.telegram_id, self.groupe, self.status)
    
    def add_users(first_name, last_name, login, password, email, telegram_id, groupe, status):

        me = User(first_name, last_name, login, password, email, telegram_id, groupe, status)
        db_session.add(me)
        db_session.commit()


    def query_info_all():
        return User.query.all()

    def query_info(field_name, specific_info):
        return User.query.filter(getattr(User, field_name) == specific_info).all()


class Logggggs:
    __tablename__ = 'basiclogs'


class Action(Logggggs):
    __tablename__ = 'actionlogs'



if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)