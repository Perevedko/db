# -*- coding: utf-8 -*-
from unittest import main
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application.views import *
from application import create_app, init_db, db
from application.models import Datapoint

import json

# <http://nidkil.me/2017/02/07/flask-application-factory-pattern/>
# <https://pythonhosted.org/Flask-Testing/#testing-with-sqlalchemy>

class TestCase(TestCase):
    
    def create_app(self):
        return create_app(config_name='testing')

    def setUp(self):
        db.init_app(app)
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_user(self):
        with self.app.app_context():
            d = Datapoint(date="2014-03-31", freq='q', name="CPI_rog", value=102.3)
            db.session.add(d)
            db.session.commit()
            
# 'The sqlalchemy extension was not registered to the current ' \
# AssertionError: The sqlalchemy extension was not registered to the current application.  Please make sure to call init_app() first.     
           
#
#app = create_app(config_filename='testing')
#
#class TestClientDB(TestCase):
#    def setUp(self):
#        self.app = create_app('testing')
#        self.app_context = self.app.app_context()
#        self.app_context.push()
#        db.init_app(self.app)
#        db.create_all()
#        self.client = self.app.test_client(use_cookies=True)
#
#    def tearDown(self):
#        db.session.remove()
#        db.drop_all()
#        # self.app_context.pop()
#
#    def test_get_datapoints_without_token(self):
#        resust = self.client.get('/api/datapoints?name=QWE&freq=d')
#        self.assertEqual(resust.status_code, 401)
#
#    def test_get_non_existent_data(self):
#        resust = self.client.get('/api/datapoints?name=QWE&freq=d&token=123qwe')
#        self.assertEqual(resust.data, [])
#
#    def test_successful_get_data(self):
#        d = Datapoint(date="2014-03-31", freq='e', name="CPI_rog", value=102.3)
#        db.session.add(d)
#        # self.session.flush()
#        raw_result = self.app.get('/api/datapoints?name=CPI_rog&freq=q&token=123qwe')
#
#        expected = dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=102.3)
#        print(raw_result.data)
#        actual = json.loads(raw_result.data.decode("utf-8"))
#
#        del actual['id']
#        assert actual in expected
#
#    def test_succesful_post_get_data(self):
#
#        data = json.dumps(dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=102.3))
#
#        raw_result = self.app.post('/api/datapoints?name=CPI_rog&freq=q&token=123qwe', json=data, headers={'content-type': 'application/json'})
#
#        expected = '[]'
#        actual = json.loads(raw_result.data.decode("utf-8"))
#
#        self.assertEqual(actual, expected)
#
#    def test_succesful_update_get_data(self):
#
#        d = Datapoint(date="2014-03-31", freq='e', name="CPI_rog", value=102.3)
#        db.session.add(d)
#
#        data = json.dumps(dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=1002.3))
#
#        raw_result = self.app.post('/api/datapoints?name=CPI_rog&freq=q&token=123qwe', json=data, headers={'content-type': 'application/json'})
#
#        expected = dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=1002.3)
#
#        actual = json.loads(raw_result.data.decode("utf-8"))
#
#        assert actual in expected



if __name__ == '__main__':
    main()