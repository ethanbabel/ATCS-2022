from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "q1?ruYe!Puf3kOsetrOt"

# TODO: Fill in methods and routes

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/history")
def history():
    return render_template("history.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    
