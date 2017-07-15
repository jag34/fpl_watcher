from sqlalchemy import Column, Float, Integer, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DailyUsageDataDB(Base):
    __tablename__ = 'DailyUsageData'

    date = Column(Date, primary_key=True)
    kwh = Column(Float)
    approx_cost = Column(Float)
    top_temp = Column(Integer)


    def __repr__(self):
        return ' '.join([self.date,
                         self.kwh+"kwh",
                         '$'+ self.approx_cost,
                         self.top_temp+"F"])

class HourlyUsageDataDB(Base):
    __tablename__ = 'HourlyUsageData'

    time = Column(DateTime, primary_key=True)
    kwh = Column(Float)
    approx_cost = Column(Float)
    top_temp = Column(Integer)

    def __repr__(self):
        return ' '.join([self.time,
                         self.kwh+"kwh",
                         '$'+ self.approx_cost,
                         self.top_temp+"F"])
