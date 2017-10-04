# from application import db
# from application.models import *

# def init_db():
#     db.create_all()



# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


# def get_session(user, password, db, host='localhost', port=5432):
#     '''Returns a connection and a metadata object'''
#     # We connect with the help of the PostgreSQL URL
#     # postgresql://federer:grandestslam@localhost:5432/tennis
#     url = 'postgresql://{}:{}@{}:{}/{}'
#     url = url.format(user, password, host, port, db)

#     # The return value of create_engine() is our connection object
#     engine = create_engine(url, client_encoding='utf8')

#     db_session = scoped_session(sessionmaker(autocommit=False,
#                                              autoflush=False,
#                                              bind=engine))

#     return engine, db_session



# def init_db(user='admin', password='123qwe', db='dev', host='localhost', port=5432):
#     # import all modules here that might define models so that
#     # they will be registered properly on the metadata.  Otherwise
#     # you will have to import them first before calling init_db()
#     engine, _ = get_session(user, password, db, host, port)
#     import application.models as models
#     models.Base.metadata.create_all(bind=engine)
