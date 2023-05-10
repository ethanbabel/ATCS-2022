from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "q1?ruYe!Puf3kOsetrOt"

# TODO: Fill in methods and routes

@app.route("/", methods=["GET", "POST"])
@app.route("/login",  methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        u = request.form["username"]
        p = request.form["password"]

        user = db_session.query(User).where(User.username==u).first()
        if user is None:
            flash('Incorrect Username/Password', 'error')
            return render_template("login.html")
        elif user.password != p:
            flash('Incorrect Username/Password', 'error')
            return render_template("login.html")

        session["username"] = u

        return redirect(url_for("search"))

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    else:
        u = request.form["username"]
        p = request.form["password"]

        usernames = db_session.query(User.username).all()
        usernames = [r for (r,) in usernames]
        if u in usernames:
            flash("Username Already Taken, Please Choose Another", "error")
            return render_template("signin.html")

        user = User(username=u, password=p)
        db_session.add(user)
        db_session.commit()
        session["username"] = u

        return redirect(url_for("search"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        if "username" in session:
            return render_template("search.html")
        else:
            return redirect(url_for("login"))
    else:
        p1 = request.form["player1"] + "%"
        p2 = request.form["player2"] + "%"

        dbp1 = db_session.query(Player).filter(Player.name.like(p1)).all()
        dbp2 = db_session.query(Player).filter(Player.name.like(p2)).all()

        if dbp1 is None or len(dbp1) < 1:
            flash("Player 1 Not Found", "error")
            return render_template("search.html")
        elif len(dbp1) > 1:
            flash("Multiple Players Found for Player 1", "error")
            return render_template("search.html")
        else:
            player1 = dbp1[0]

        if dbp2 is None or len(dbp2) < 1:
            flash("Player 2 Not Found", "error")
            return render_template("search.html")
        elif len(dbp2) > 1:
            flash("Multiple Players Found for Player 2", "error")
            return render_template("search.html")
        else:
            player2 = dbp2[0]
        
        c = Comparison(username=session["username"], player1_id=player1.id, player2_id=player2.id)
        db_session.add(c)
        db_session.commit()

        session["player1"] = player1.id
        session["player2"] = player2.id

        return redirect(url_for("comparison"))



@app.route("/comparison", methods=["GET", "POST"])
def comparison():
    if "username" in session:
        player1 = db_session.query(Player).where(Player.id == session["player1"]).first()
        p1 = {"name":str(player1.name), "position":str(player1.position), "points":round(player1.points, 2), "passing_yards":round(player1.passing_yards, 2), 
                "passing_tds":round(player1.passing_tds, 2), "interceptions":round(player1.interceptions, 2), "sacks":round(player1.sacks, 2), 
                "rushing_yards":round(player1.rushing_yards, 2), "rushing_tds":round(player1.rushing_tds, 2), "receptions":round(player1.receptions, 2), 
                "recieving_yards":round(player1.recieving_yards, 2), "recieving_tds":round(player1.recieving_tds, 2), "fumbles":round(player1.fumbles, 2)}
        player2 = db_session.query(Player).where(Player.id == session["player2"]).first()
        p2 = {"name":str(player2.name), "position":str(player2.position), "points":round(player2.points, 2), "passing_yards":round(player2.passing_yards, 2), 
                "passing_tds":round(player2.passing_tds, 2), "interceptions":round(player2.interceptions, 2), "sacks":round(player2.sacks, 2), 
                "rushing_yards":round(player2.rushing_yards, 2), "rushing_tds":round(player2.rushing_tds, 2), "receptions":round(player2.receptions, 2), 
                "recieving_yards":round(player2.recieving_yards, 2), "recieving_tds":round(player2.recieving_tds, 2), "fumbles":round(player2.fumbles, 2)}
        return render_template("comparison.html", p1_dict = p1, p2_dict = p2)
    else:
        return redirect(url_for("login"))

@app.route("/history", methods=["GET", "POST"])
def history():
    if "username" in session:
        comparison = db_session.query(Comparison).where(Comparison.username==session["username"]).all()
        h = []
        for c in comparison:
            p1_name = db_session.query(Player.name).where(Player.id == c.player1_id).first()
            p2_name = db_session.query(Player.name).where(Player.id == c.player2_id).first()
            print(p1_name)
            print(p2_name)
            p1_name, = p1_name
            p2_name, = p2_name
            comp = [p1_name, p2_name]
            h.append(comp)
        h.reverse()
        return render_template("history.html", history = h)
    else:
        return redirect(url_for("login"))

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if "username" in session:
        session.pop("username")
        flash("You've been logged out", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    
