import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from string import ascii_uppercase
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    terms = list(mongo.db.terms.find().sort("created_on", -1))
    popular_terms = list(mongo.db.terms.find({"score": {"$gt": 4}}).sort("score", -1))
    users = mongo.db.users.find()
    return render_template("index.html", terms=terms, popular_terms=popular_terms, users=users)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
    if len(terms) == 0:
        flash("No results found")
        return render_template("not_found.html")
    return render_template("dictionary.html", terms=terms)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        existing_email = mongo.db.users.find_one({"email_address": request.form.get("email").lower()})
        is_superuser = True if request.form.get("username").lower == "admin" else False

        # check whether user already exists
        if existing_user:
            flash("User already exists")
            return redirect(url_for("register"))
        
        # check whether e-mail address was already used to sign up
        if existing_email:
            flash("An account already exists for this e-mail address!")
            return redirect(url_for("register"))
        
        create_account = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email_address": request.form.get("email").lower(),
            "is_superuser": is_superuser
        }
        mongo.db.users.insert_one(create_account)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("home_page", username=session["user"]))

    return render_template("register.html")


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
                    return redirect(url_for(
                        "home_page", username=session["user"]))

            else:
                # invalid password match
                flash("Invalid login credentials!")
                return redirect(url_for("login"))

        else: 
            # username doesn't exist
            flash("Invalid login credentials!")
            return redirect(url_for("login"))

    return render_template("login.html")  


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home_page"))


@app.route("/profile/<username>")
def profile(username):
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        if username != session["user"]:
            flash("You do not have permission to view other users' profiles")
            return redirect(url_for("home_page"), username=username)
        
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        return render_template("profile.html", username=username, terms=terms)
    else:
        flash("Please log in to view your profile")
        return redirect(url_for("login"))


@app.route("/view_dictionary")
def view_dictionary():
    terms = list(mongo.db.terms.find().sort("term_name", 1))
    return render_template("dictionary.html", terms=terms)


@app.route("/add_definition", methods=["GET", "POST"])
def add_definition():
    if "user" in session:
        if request.method == "POST":
            existing_term = mongo.db.terms.find_one({"term_name": request.form.get("term_name").capitalize()})
            if existing_term:
                flash("This term already exists in the dictionary. Please add another term.")
                return redirect(url_for("add_definition"))

            new_term = {
                "term_name": request.form.get("term_name").capitalize(),
                "term_definition": request.form.get("term_definition").capitalize(),
                "created_by": session["user"],
                "created_on": datetime.datetime.today().strftime("%m/%d/%y %H:%M:%S"),
                "contribution_value": 1,
                "score": 0
            }
            mongo.db.terms.insert_one(new_term)
            flash("Term successfully created. You will now be redirected to the dictionary page where you can see your contribution!")
            return redirect(url_for("view_dictionary"))
        
        terms = mongo.db.terms.find()
        users = mongo.db.users.find()
        return render_template("add_definition.html", terms=terms, users=users)
    else:
        flash("Please log in to view this page.")
        return redirect(url_for("login"))


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    if "user" in session:
        if request.method == "POST":
            updated_term = {
                "term_name": request.form.get("term_name").capitalize(),
                "term_definition": request.form.get("term_definition").capitalize(),
                "created_by": session["user"],
                "created_on": datetime.datetime.today().strftime("%m/%d/%y %H:%M:%S"),
                "contribution_value": 1,
                "score": 0
            }
            mongo.db.terms.update({"_id": ObjectId(term_id)}, updated_term)
            flash("Dictionary information successfully updated")
            return redirect(url_for("view_dictionary"))
        
        term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
        terms = mongo.db.terms.find().sort("term_name", 1)
        return render_template("edit_term.html", terms=terms, term=term)
    
    else:
        flash("Please log in to view this page")
        return redirect(url_for("login"))


@app.route("/upvote/<term_id>")
def upvote(term_id):
    if "user" in session:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        term = mongo.db.terms.find_one_and_update({"_id": ObjectId(term_id)}, {"$inc": {"score": 1}})

        return render_template("dictionary.html", term=term, terms=terms)
    else:
        flash("Please log in to perform this action")
        return redirect(url_for("login"))


@app.route("/downvote/<term_id>")
def downvote(term_id):
    if "user" in session:
        terms = list(mongo.db.terms.find().sort("term_name", 1))
        term = mongo.db.terms.find_one_and_update({"_id": ObjectId(term_id)}, {"$inc": {"score": -1}})
        
        return render_template("dictionary.html", term=term, terms=terms)
    else:
        flash("Please log in to perform this action")
        return redirect(url_for("login"))


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    if request.method == "POST":
        is_superuser = True if mongo.db.users.find_one(
            {"username": username, "is_superuser": True}) else False
        updated_account = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email_address": request.form.get("email").lower(),
            "is_superuser": is_superuser
        }
        mongo.db.users.update({"username": username}, updated_account)

        session["user"] = request.form.get("username").lower()
        flash("Your profile was successfully updated")
        return redirect(url_for("profile", username=username))

    return render_template("update_profile.html", username=username)


@app.route("/manage_users")
def manage_users():
    if session["user"] == "admin":
        users = mongo.db.users.find().sort("username", 1)
        return render_template("manage_users.html", users=users)
    else:
        flash("You are not authorised to view this page")
        return redirect(url_for("home_page"))      


@app.route("/add_new_user", methods=["GET", "POST"])
def add_new_user():
    if session["user"] == "admin":
        if request.method == "POST":
            existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
            existing_email = mongo.db.users.find_one({"email_address": request.form.get("email").lower()})
            is_superuser = True if request.form.get("username").lower == "admin" else False

            # check whether user already exists
            if existing_user:
                flash("User already exists")
                return redirect(url_for("register"))
            
            # check whether e-mail address was already used to sign up
            if existing_email:
                flash("An account already exists for this e-mail address!")
                return redirect(url_for("register"))
            
            new_user = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "email_address": request.form.get("email").lower(),
                "is_superuser": is_superuser
            }
            mongo.db.users.insert_one(new_user)
            flash("The user was successfully added to the database.")
            return redirect(url_for("manage_users"))

        users = mongo.db.users.find()
        return render_template("add_new_user.html")
    
    else:
        flash("You are not authorised to view this page")
        return redirect(url_for("home_page"))


@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    if "user" in session:
        terms = mongo.db.terms.find()
        mongo.db.terms.remove({"_id": ObjectId(term_id)})
        flash("Term deleted from dictionary")
        return redirect(url_for("view_dictionary", terms=terms))
    else:
        flash("You must log in to perform this action")
        return redirect(url_for("login"))


@app.route("/delete_account/<username>")
def delete_account(username):
    users = mongo.db.users.find()
    session.pop("user")
    mongo.db.users.remove({"username": username})
    flash("Your account was deleted. You will now be redirected to the home page.")
    return redirect(url_for("home_page", username=username, users=users))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    if session["user"] == "admin":
        users = mongo.db.users.find()
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        flash("The user was successfully deleted from the database.")
        return redirect(url_for("manage_users"))
    else:
        flash("You are not authorised to view this page")
        return redirect(url_for("home_page"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
    port=int(os.environ.get("PORT")), 
    debug=True)