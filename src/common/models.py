import uuid
from sqlalchemy import Text, Column, DateTime, Numeric, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.common.app import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Text(), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime(), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self) -> str:
        return str(self.to_dict())

    def to_dict(self) -> dict:
        return {
            column: getattr(self, column) for column in self.__table__.columns.keys()
        }


class Bank(Base):
    __tablename__ = 'bank'
    # the id is the name
    link = Column(Text(), nullable=False)

    exchanges = relationship('Exchange', back_populates="bank")


class Exchange(Base):
    __tablename__ = 'exchange'

    date = Column(Date(), nullable=False)
    dollar_buy = Column(Numeric(precision=5, scale=2), nullable=True)
    dollar_sell = Column(Numeric(precision=5, scale=2), nullable=True)
    euro_buy = Column(Numeric(precision=5, scale=2), nullable=True)
    euro_sell = Column(Numeric(precision=5, scale=2), nullable=True)
    bank_id = Column(Text(), ForeignKey("bank.id"), nullable=False)

    bank = relationship('Bank', back_populates="exchanges")
