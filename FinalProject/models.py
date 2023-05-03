"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "players"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    
