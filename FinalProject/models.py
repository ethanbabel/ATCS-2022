"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, FLOAT
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "players"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    name = Column('name', TEXT)
    position = Column('position', TEXT)
    points = Column('points', FLOAT)
    passing_yards = Column('passing_yards', FLOAT)
    passing_tds = Column('passing_tds', FLOAT)
    interceptions = Column('interceptions', FLOAT)
    sacks = Column('sacks', FLOAT)
    rushing_yards = Column('rushing_yards', FLOAT)
    rushing_tds = Column('rushing_tds', FLOAT)
    receptions = Column('receptions', FLOAT)
    recieving_yards = Column('recieving_yards', FLOAT)
    recieving_tds = Column('recieving_tds', FLOAT)
    fumbles = Column('fumbles', FLOAT)

class User(Base):
    __tablename__ = "users"

    #Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)

    comparisons = relationship("Comparison", back_populates="user")

class Comparison(Base):
    __tablename__ = "comparisons"

    #Columns
    id = Column("id", INTEGER, primary_key=True)
    username = Column("username", TEXT, ForeignKey("users.username"))

    user = relationship("User", back_populates= "comparisons")


    
