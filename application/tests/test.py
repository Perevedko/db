# -*- coding: utf-8 -*-
from unittest import TestCase, main
from flask_sqlalchemy import SQLAlchemy
from application.views import *
from application import create_app, init_db
from application.models import Datapoint, db

import os, json


class TestClientDB(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
        self.client = app.test_client(use_cookies=True)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_datapoints_without_token(self):
        resust = self.client.get('/api/datapoints?name=QWE&freq=d')
        self.assertEqual(resust.status_code, 401)

    def test_get_non_existent_data(self):
        resust = self.client.get('/api/datapoints?name=QWE&freq=d&token=123qwe')
        self.assertEqual(resust.data.decode("utf-8"), '[]')

    def test_successful_get_data(self):
        d = Datapoint(date="2014-03-31", freq='e', name="CPI_rog", value=102.3)
        w = Datapoint(date="2015-03-31", freq='e', name="CPI_rog", value=102.3)
        db.session.add(d)
        db.session.add(w)

        raw_result = self.client.get('/api/datapoints?name=CPI_rog&freq=e&token=123qwe')

        expected = dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=102.3)

        actual = json.loads(raw_result.data.decode("utf-8"))
        for item in actual:
            del item['id']
        assert expected in actual

    def test_succesful_post_data(self):

        data = json.dumps(dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=102.3))

        raw_result = self.client.post('/api/incoming?name=CPI_rog&freq=q&token=123qwe', data=data, headers={'content-type': 'application/json'})

        expected = []
        actual = json.loads(raw_result.data.decode("utf-8"))

        self.assertEqual(actual, expected)

    def test_succesful_update_post_data(self):

        d = Datapoint(date="2014-03-31", freq='e', name="CPI_rog", value=102.3)
        db.session.add(d)

        data = json.dumps([dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=1002.3)])

        raw_result = self.client.post('/api/incoming?token=123qwe', data=data, headers={'content-type': 'application/json'})

        expected = []
        actual = json.loads(raw_result.data.decode("utf-8"))

        self.assertEqual(actual, expected)

        expected = dict(date="2014-03-31", freq='e', name=u"CPI_rog", value=1002.3)

        actual = db.session.query(Datapoint).filter_by(date="2014-03-31", freq='e', name=u"CPI_rog", value=1002.3).first().__dict__
        del actual['_sa_instance_state']
        del actual['id']

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()