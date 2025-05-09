from sqlalchemy import Column, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base= declarative_base()

class Embeddings(Base):
    __tablename__ = 'embeddings'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    vector = Column(Vector(1536), nullable=True)