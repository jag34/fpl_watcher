from models import HourlyUsageDataDB, DailyUsageDataDB

def setup_db(db_path='sqlite:///fpl_db.db'):
    from models import Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(db_path)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    return Session

Session = setup_db()
