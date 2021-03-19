import os
from datetime import date
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
    recipies = list(mongo.db.recipies.find())
    return render_template(
                           "recipies.html", recipies=recipies,)


@app.route("/add_recipe.html", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        steps = request.form.getlist("steps")
        step_list = []
        for step in steps:
            step_list.append(step)
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        ingredients = request.form.getlist("ing_name")
        ingredients_list = []
        for ingredient in ingredients:
            ingredients_list.append(ingredient)

        new_recipe = {
            "created_by": session.get("user"),
            "date_created": d1,
            "food_name": request.form.get("food_name"),
            "difficulty": request.form.get("difficulty"),
            "cook_time": request.form.get("cook_time"),
            "img_url": request.form.get("img_url"),
            "ing_name": ingredients_list,
            "steps": step_list
        }
        mongo.db.recipies.insert_one(new_recipe)
        flash("Thank you for submitting your recipe!")

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        steps = request.form.getlist("steps")
        step_list = []
        for step in steps:
            step_list.append(step)
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        ingredients = request.form.getlist("ing_name")
        ingredients_list = []
        for ingredient in ingredients:
            ingredients_list.append(ingredient)
        submit = {
            "created_by": session.get("user"),
            "date_created": d1,
            "food_name": request.form.get("food_name"),
            "difficulty": request.form.get("difficulty"),
            "cook_time": request.form.get("cook_time"),
            "img_url": request.form.get("img_url"),
            "ing_name": ingredients_list,
            "steps": step_list
        }
        mongo.db.recipies.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated!")
        return redirect(url_for("user_profile"))

    recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipies.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("user_profile"))


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
    user = session.get("user")
    if user is not None:
        recipies = list(mongo.db.recipies.find())
        return render_template("user_profile.html", recipies=recipies)
    else:
        return render_template("403.html")


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
                    session["name"] = existing_user["name"]
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


# Search function, takes the string used to search
#  and returns all matches from the db. Code from
# walkthrough task project and modified to suit this project
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    recipies = list(mongo.db.recipies.find({"$text": {"$search": query}}))
    return render_template("recipies.html",
                           recipies=recipies)


# Error handlers from flask documentation
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def access_denied(e):
    return render_template('403.html'), 403


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
