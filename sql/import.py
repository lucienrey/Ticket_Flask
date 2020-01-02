import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine(os.getenv("DATABASE_URL")) \\ needs to be added to environment of termianl as follow
# export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/ubsform"

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("INCTickets.csv")
    reader = csv.reader(f)
    for status, version, description, ubsuser_id in reader:
        db.execute("INSERT INTO tickets (status, version, description, ubsuser_id) VALUES (:status, :version, :description, :ubsuser_id)",
                    {"status": status, "version": version, "description": description, "ubsuser_id": ubsuser_id})
        print(f"Added New Tickets  {status}, {version}, {description} ,{ubsuser_id}.")
    db.commit()

if __name__ == "__main__":
    main()
