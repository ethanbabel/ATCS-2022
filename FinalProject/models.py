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
    name = Column('name', TEXT, nullable=False)
    position = Column('position', TEXT, nullable=False)
    points = Column('points', FLOAT, nullable=False)
    passing_yards = Column('passing_yards', FLOAT, nullable=False)
    passing_tds = Column('passing_tds', FLOAT, nullable=False)
    interceptions = Column('interceptions', FLOAT, nullable=False)
    sacks = Column('sacks', FLOAT, nullable=False)
    rushing_yards = Column('rushing_yards', FLOAT, nullable=False)
    rushing_tds = Column('rushing_tds', FLOAT, nullable=False)
    receptions = Column('receptions', FLOAT, nullable=False)
    recieving_yards = Column('recieving_yards', FLOAT, nullable=False)
    recieving_tds = Column('recieving_tds', FLOAT, nullable=False)
    fumbles = Column('fumbles', FLOAT, nullable=False)

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
    player1_id = Column("player1_id", INTEGER)
    player2_id = Column("player2_id", INTEGER)
    username = Column("username", TEXT, ForeignKey("users.username"))

    user = relationship("User", back_populates= "comparisons")
    


    
