import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/recipies.html")
def recipies():
    return render_template("recipies.html")


@app.route("/add_recipie.html", methods=["GET", "POST"])
def add_recipie():
    if request.method == "POST":
        new_recipie = {
            "food_name": request.form.get("food_name"),
            "difficulty": request.form.get("difficulty"),
            "cook_time": request.form.get("cook_time"),
            "img_url": request.form.get("img_url"),
            "ing_name": request.form.get("ing_name"),
            "ing_quantity": request.form.get("ing_quantity"),
            "step_1": request.form.get("step_1"),
            "step_2": request.form.get("step_2"),
            "step_3": request.form.get("step_3"),
            "step_4": request.form.get("step_4"),
            "step_5": request.form.get("step_5"),
            "step_6": request.form.get("step_6"),
        }
        mongo.db.recipies.insert_one(new_recipie)

    return render_template("add_recipie.html")


@app.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))
        # Used register method from Code Institute walkthrough project
        # but added name and email fields when registering
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "name": request.form.get("name"),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        # put new user into cookie
        session["user"] = request.form.get("username").lower()
        session["name"] = request.form.get("name").title()
        flash("Registration Successful")
        return redirect(url_for("user_profile", username=session["user"]))

    return render_template("register.html")


@app.route("/user_profile.html")
def user_profile():
    return render_template("user_profile.html")


# login method used from walkthrough project
#  in the Code Institute Backend module
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("user_profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# login method used from walkthrough project
#  in the Code Institute Backend module
@app.route("/logout")
def logout():
    flash("Successfully logged out, Goodbye!")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
