from sqlalchemy import Column, Integer, String, Enum, Float
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.types import Date
from .schemas import OperatingSystem
from .database import Base


class PerformanceMetrics(Base):
    __tablename__ = "performance_metrics"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    channel = Column(String(255), index=True)
    country = Column(String(2), index=True)
    os = Column(Enum(OperatingSystem))
    impressions = Column(Integer)
    clicks = Column(Integer)
    installs = Column(Integer)
    spend = Column(Float)
    revenue = Column(Float)

    @hybrid_property
    def cpi(self):
        return self.spend / self.installs

    @cpi.expression
    def cpi(cls):
        return cls.spend / cls.installs

