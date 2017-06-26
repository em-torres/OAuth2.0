from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Users

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_user(login_session):
    new_user = Users(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    return get_user_id(login_session['email'])


def get_user_id(email):
    try:
        user = session.query(Users).filter_by(email=email).one()
        return user.id
    except:
        return None


def get_user_info(user_id):
    if user_id:
        user = session.query(Users).filter_by(id=user_id).one()
        return user
