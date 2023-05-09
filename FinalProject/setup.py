from database import init_db, db_session
from models import *
from csv import *
from pandas import *
import re
import math

init_db()

# Open file
with open("FinalProject_FantasyData/FantasyPros_Fantasy_Football_Statistics_QB.csv") as qb:

    # Create reader object by passing the file
    # object to reader method
    reader = read_csv(qb, delimiter=",")

    num_rows = len(reader["Rank"])

    # Iterate over each row in the csv file using reader object
    for row in range(num_rows):
        if not math.isnan(reader["G"][row]) and (reader["G"][row])>0:
            p = Player(name=str(reader["Player"][row]), 
            position="QB", points=float(reader["FPTS/G"][row]), 
            passing_yards=int(re.sub("[^\d\.]", "", reader["PYDS"][row]))/int(reader["G"][row]), 
            passing_tds=int(reader["PTD"][row])/int(reader["G"][row]), 
            interceptions=int(reader["INT"][row])/int(reader["G"][row]), 
            sacks=float(reader["SACKS"][row])/int(reader["G"][row]), 
            rushing_yards=int(re.sub("[^\d\.]", "", reader["RYDS"][row]))/int(reader["G"][row]), 
            rushing_tds=int(reader["RTD"][row])/int(reader["G"][row]), 
            fumbles=int(reader["FL"][row])/int(reader["G"][row]), 
            receptions=0.0, recieving_yards=0.0, recieving_tds=0.0)

        db_session.add(p)
        db_session.commit()
    

with open("FinalProject_FantasyData/FantasyPros_Fantasy_Football_Statistics_RB.csv") as rb:

    # Create reader object by passing the file
    # object to reader method
    reader = read_csv(rb, delimiter=",")

    num_rows = len(reader["Rank"])

    # Iterate over each row in the csv file using reader object
    for row in range(num_rows):
        if not math.isnan(reader["G"][row]) and (reader["G"][row])>0:
            p = Player(name=str(reader["Player"][row]), 
            position="RB", points=float(reader["FPTS/G"][row]), 
            rushing_yards=int(re.sub("[^\d\.]", "", reader["RuYDS"][row]))/int(reader["G"][row]), 
            rushing_tds=int(reader["RuTD"][row])/int(reader["G"][row]), 
            recieving_yards=int(reader["ReYDS"][row])/int(reader["G"][row]), 
            recieving_tds=int(reader["ReTD"][row])/int(reader["G"][row]), 
            fumbles=int(reader["FL"][row])/int(reader["G"][row]), 
            passing_yards=0.0, passing_tds=0.0, interceptions=0.0, sacks=0.0)

        db_session.add(p)
        db_session.commit()


with open("FinalProject_FantasyData/FantasyPros_Fantasy_Football_Statistics_WR.csv") as wr:

    # Create reader object by passing the file
    # object to reader method
    reader = read_csv(wr, delimiter=",")

    num_rows = len(reader["Rank"])

    # Iterate over each row in the csv file using reader object
    for row in range(num_rows):
        if not math.isnan(reader["G"][row]) and (reader["G"][row])>0:
            p = Player(name=str(reader["Player"][row]), 
            position="WR", points=float(reader["FPTS/G"][row]), 
            recieving_yards=float(re.sub("[^\d\.]", "", str(reader["ReYDS"][row])))/int(reader["G"][row]), 
            recieving_tds=int(reader["ReTD"][row])/int(reader["G"][row]), 
            receptions=int(reader["REC"][row])/int(reader["G"][row]), 
            rushing_tds=int(reader["RuTD"][row])/int(reader["G"][row]), 
            rushing_yards=int(reader["RuYDS"][row])/int(reader["G"][row]),            
            fumbles=int(reader["FL"][row])/int(reader["G"][row]), 
            passing_yards=0.0, passing_tds=0.0, interceptions=0.0, sacks=0.0)

        db_session.add(p)
        db_session.commit()


with open("FinalProject_FantasyData/FantasyPros_Fantasy_Football_Statistics_TE.csv") as te:

    # Create reader object by passing the file
    # object to reader method
    reader = read_csv(te, delimiter=",")

    num_rows = len(reader["Rank"])

    # Iterate over each row in the csv file using reader object
    for row in range(num_rows):
        if not math.isnan(reader["G"][row]) and (reader["G"][row])>0:
            p = Player(name=str(reader["Player"][row]), 
            position="TE", points=float(reader["FPTS/G"][row]), 
            recieving_yards=int(re.sub("[^\d\.]", "", reader["ReYDS"][row]))/int(reader["G"][row]), 
            recieving_tds=int(reader["ReTD"][row])/int(reader["G"][row]), 
            receptions=int(reader["REC"][row])/int(reader["G"][row]), 
            rushing_tds=int(reader["RuTD"][row])/int(reader["G"][row]), 
            rushing_yards=int(reader["RuYDS"][row])/int(reader["G"][row]),            
            fumbles=int(reader["FL"][row])/int(reader["G"][row]), 
            passing_yards=0.0, passing_tds=0.0, interceptions=0.0, sacks=0.0)

        db_session.add(p)
        db_session.commit()