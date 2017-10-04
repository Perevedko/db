from application.models import Datapoint
from application import db


def load_data(bulk):
    try:
        print('!!!!!!!!!!!!!')
        for chunk in bulk:
            exists = db.session.query(Datapoint).filter_by(name=chunk['name'], freq=chunk['freq'], date=chunk['date']).first()
            if exists:
                exists.value = chunk['value']
                db.session.add(exists)
            else:
                db.session.add(Datapoint(**chunk))
        db.session.commit()
        return
    except Exception as e:
        db.session.rollback()
        return e


def get_data(name, freq, start_date=None, end_date=None):
    try:
        data = db.session.query(Datapoint).filter_by(name=name, freq=freq)
        if start_date and end_date:
            data.filter(Datapoint.date.between(start_date, end_date))

        result = [obj.__dict__ for obj in data.all()]
        for d in result:
            del d['_sa_instance_state']
        print('#############', result)
        return result
    except Exception as e:
        return e
