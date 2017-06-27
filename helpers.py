import httplib2
import json

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


def get_fb_token(request_result=None):
    """ This function takes a request result to FB API to return the FB Token """
    if request_result is not None:
        return request_result.split(',')[0].split(':')[1].replace('"', '')


def request_to_url(url=None, method="GET", value=0, to_json=True):
    """ This method pretend to simulate the HTTP Request method in an easy way, taking an Url, Method and Value
        parameters and returning the request in JSON format.
    """
    h = httplib2.Http()
    if to_json:
        return json.loads(h.request(url, method)[value])
    return h.request(url, method)[value]
