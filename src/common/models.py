import uuid
from sqlalchemy import Text, Column, DateTime
from sqlalchemy.sql import func
from src.common.app import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Text(), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(), server_default=func.now(), onupdate=func.now(), nullable=False)


class Bank(Base):
    __tablename__ = 'bank'

    link = Column(Text(), nullable=False)
