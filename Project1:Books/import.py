import csv
import psycopg2
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://tzxyempokotnfe:e38e00f7e54ef1b0665e895ada1146fc4624b158aee42845243e91490426d38f@ec2-54-163-246-159.compute-1.amazonaws.com:5432/d444jseosr52v2')
   # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))
f = open("books.csv")
reader = csv.reader(f)
for no,title,author,yr in reader: # loop gives each column a name
      db.execute("INSERT INTO \"book\" (isbn,title,author,year) VALUES (:isbn,:title,:author,:year)",
                  {"isbn":no, "title": title, "author":author,"year":yr}) # substitute values from CSV line into SQL command, as per this dict
      print("Added book details")
db.commit() 
