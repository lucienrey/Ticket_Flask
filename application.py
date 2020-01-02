import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    ubsuser = db.execute("SELECT * FROM ubsuser").fetchall()
    return render_template("index.html", ubsuser=ubsuser)

@app.route("/newticket", methods=["POST"])
def newticket():
    """Create new ticket."""

    # Get form information.
    status = request.form.get("status")
    version = request.form.get("version")
    description = request.form.get("description")
    ubsuser_id = request.form.get("ubsuser")

    # Commit to DB
    db.execute("INSERT INTO tickets (status, version, description, ubsuser_id) VALUES (:status, :version, :description, :ubsuser_id)",
            {"status": status, "version": version,"description": description, "ubsuser_id": ubsuser_id})
    db.commit()
    return render_template("success.html")


@app.route("/allinctickets")
def allinctickets():
    """Lists all Inc Tickest."""
    opentickets = db.execute("SELECT * FROM tickets where status='Open'").fetchall()
    closedtickets = db.execute("SELECT * FROM tickets where NOT status='Open'").fetchall()
    return render_template("allinctickets.html", opentickets=opentickets, closedtickets=closedtickets)

@app.route("/allinctickets/<int:ticket_id>")
def ticket(ticket_id):
    """Lists details about Individual Ticket."""
    # Make sure ticket exists.
    ticket = db.execute("SELECT tickets.id, status, version, description, name, tnumber FROM tickets join ubsuser on tickets.ubsuser_id = ubsuser.id WHERE tickets.id = :id", {"id": ticket_id}).fetchone()
    if ticket_id is None:
        return render_template("error.html", message="No such Inc Tickets.")
    return render_template("ticket.html", ticket=ticket)
