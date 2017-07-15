import db
import datetime

Session = db.setup_db('sqlite:///test_fpl_db.db')
session = Session()
session.add(db.HourlyUsageDataDB(time=datetime.datetime.now(),
                                 kwh = 12.2,
                                 approx_cost = 1.2,
                                 top_temp = 99))

session.commit()
