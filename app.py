import os
from datetime import date
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/recipes")
def recipes():
    """
    App route for recipes page, returns all recipes paginated
    with 3 results per page
    """
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = (page - 1) * 3  # My formula for getting the right offset
    total = mongo.db.recipies.find().count()
    recipe = list(mongo.db.recipies.find())
    recipe_paginated = recipe[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template('recipes.html',
                           recipes=recipe_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/range")
def range():
    """
    App route for product range, returns all products paginated
    """
    products = list(mongo.db.products.find())
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = offset = (page - 1) * 3  # My formula for getting the right offset
    total = mongo.db.products.find().count()
    product_paginated = products[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template('range.html',
                           products=product_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Function to add recipie from the provided form
    """
    if request.method == "POST":
        steps = request.form.getlist("steps")
        step_list = []
        for step in steps:
            step_list.append(step)
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        ingredients = request.form.getlist("ing_name")
        ingredients_list = []
        for ingredient in ingredients:
            ingredients_list.append(ingredient)
        new_recipe = {
            "created_by": session.get("user"),
            "date_created": d1,
            "food_name": request.form.get("food_name"),
            "difficulty": request.form.get("difficulty"),
            "cook_time": int(request.form.get("cook_time")),
            "img_url": request.form.get("img_url"),
            "ing_name": ingredients_list,
            "steps": step_list,
            "nationality": request.form.get("nationality")
        }
        mongo.db.recipies.insert_one(new_recipe)
        flash("Thank you for submitting your recipe!")
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Function to edit a recipe via the provided form
    """
    if request.method == "POST":
        steps = request.form.getlist("steps")
        step_list = []
        for step in steps:
            step_list.append(step)
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        ingredients = request.form.getlist("ing_name")
        ingredients_list = []
        for ingredient in ingredients:
            ingredients_list.append(ingredient)
        submit = {
            "created_by": session.get("user"),
            "date_created": d1,
            "food_name": request.form.get("food_name"),
            "difficulty": request.form.get("difficulty"),
            "cook_time": int(request.form.get("cook_time")),
            "img_url": request.form.get("img_url"),
            "ing_name": ingredients_list,
            "steps": step_list,
            "nationality": request.form.get("nationality")
        }
        mongo.db.recipies.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated!")
        return redirect(url_for("user_profile"))
    recipe = mongo.db.recipies.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Function to delete a recipe
    """
    mongo.db.recipies.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("user_profile"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function to register a new user via the registration page
    """
    if request.method == "POST":  # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))
        register = {  # Register method from Code Institute walkthrough project
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "name": request.form.get("name"),  # added name and email
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()  # add cookie
        session["name"] = request.form.get("name").title()
        flash("Registration Successful")
        return redirect(url_for("user_profile", username=session["user"]))
    return render_template("register.html")


@app.route("/user_profile")
def user_profile():
    """
    Function to show all recipes created by logged in user
    """
    user = session.get("user").lower()
    if user is not None:
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page',
            offset_parameter='offset')
        per_page = 3
        offset = (page - 1) * 3  # My formula for getting the right offset
        total = mongo.db.recipies.find({'created_by': user}).count()
        recipe = list(mongo.db.recipies.find({'created_by': user}))
        recipe_paginated = recipe[offset: offset + per_page]
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='materializecss')
        return render_template('user_profile.html',
                               recipes=recipe_paginated,
                               page=page,
                               per_page=per_page,
                               pagination=pagination)
    else:
        return render_template("403.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function to handle logins used and customized from walkthrough project
    in the Code Institute Backend module
    """
    if request.method == "POST":  # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            if check_password_hash(  # ensure hash matches user input
                                    existing_user["password"],
                                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["name"] = existing_user["name"]
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(url_for("user_profile",
                                        username=session["user"]))
            else:  # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:  # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    logout method used from CI walkthrough project
    """
    flash("Successfully logged out, Goodbye!")
    session.pop("user")  # Removes user from cookie
    return redirect(url_for("login"))


@app.route("/search", methods=["GET"])
def search():
    """
    Search function, takes the string used to search
    and returns all matches from the db.
    modified from CI walkthrough project.
    """
    query = request.args.get("query")
    recipes = list(mongo.db.recipies.find({"$text": {"$search": query}}))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = (page - 1) * 3  # My formula for getting the right offset
    recipe_paginated = recipes[offset: offset + per_page]
    total = mongo.db.recipies.find({"$text": {"$search": query}}).count()
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    if len(recipes) == 0:
        flash(f"We're sorry but no recipes with {query} were found!")
    else:
        flash(f"Your search for {query} returned {len(recipes)} result(s)!")
    return render_template('recipes.html',
                           recipes=recipe_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/cook_time", methods=["GET"])
def by_cook_time():
    """
    Sort all products by cooking time ascending
    """
    recipes = list(mongo.db.recipies.find().sort("cook_time", 1))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = (page - 1) * 3  # My formula for getting the right offset
    recipe_paginated = recipes[offset: offset + per_page]
    total = mongo.db.recipies.find().sort("cook_time", 1).count()
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    flash("Showing results by cooking time ascending!")
    return render_template('recipes.html',
                           recipes=recipe_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route('/nationality_filter/<id>')
def nationality_filter(id):
    """
    Function to take the id variable and return
    paginated recipes which included that id
    """
    recipes = list(mongo.db.recipies.find({"nationality": id}))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = (page - 1) * 3  # My formula for getting the right offset
    recipe_paginated = recipes[offset: offset + per_page]
    total = len(recipes)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    flash(f"Showing results for {id.title()}")
    return render_template('recipes.html',
                           recipes=recipe_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route('/utensil_filter/<id>')
def utensil_filter(id):
    """
    Function to take the id variable and return
    paginated products which included that id
    """
    products = list(mongo.db.products.find({"type": id}))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = (page - 1) * 3  # My formula for getting the right offset
    total = mongo.db.products.find({"type": "pot"}).count()
    product_paginated = products[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template('range.html',
                           products=product_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route("/rating", methods=["GET"])
def by_rating():
    """
    Function to filter by product rating in descending order
    """
    products = list(mongo.db.products.find().sort("rating", -1))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 3
    offset = (page - 1) * 3  # My formula for getting the right offset
    total = mongo.db.products.find().count()
    product_paginated = products[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='materializecss')
    return render_template('range.html',
                           products=product_paginated,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.errorhandler(404)
def page_not_found(e):
    """
    Error handler 404 from flask documentation
    """
    return render_template('404.html'), 404


@app.errorhandler(403)
def access_denied(e):
    """
    Error handler 403 from flask documentation
    """
    return render_template('403.html'), 403


@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handler 500 from flask documentation
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
