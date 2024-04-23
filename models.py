from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    id_user = Column(Integer,
                     unique=True)
    tg_username = Column(String,
                         nullable=True,
                         default=None)
    tg_fullname = Column(String,
                         nullable=True,
                         default=None)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    telegram_user_id = Column(Integer,
                              unique=True,
                              nullable=False)
    full_name = Column(String,
                       nullable=False)
    phone_number = Column(String,
                          nullable=False)
    request = Column(String)
    email = Column(String,
                   nullable=False)
    instagram = Column(String,
                       nullable=False)
