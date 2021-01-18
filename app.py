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


'''
This function renders the site's home page. If the user is logged in, their
most recent contributions to the dictionary appear on the page.
'''


@app.route("/")
@app.route("/home_page/")
def home_page():
    # orders terms by date of creation, starting with the most recent
    terms = list(mongo.db.terms.find().sort("created_on", -1))
    # finds terms with a score of 5 or more and sorts highest to lowest
    popular_terms = list(mongo.db.terms.find(
        {"score": {"$gt": 4}}).sort("score", -1))
    users = mongo.db.users.find()
    return render_template("index.html", terms=terms,
                           popular_terms=popular_terms, users=users)


'''
This function renders the dictionary page, displaying the user's search results
by filtering any records that contain a matching query keyword.
'''


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    terms = list(mongo.db.terms.find(
        {"$text": {"$search": query}}).sort("term_name", 1))
    # renders a no results found page if no records match the user's query
    if len(terms) == 0:
        return render_template("not_found.html")
    return render_template("dictionary.html", terms=terms)


'''
This function adds a new user to the database in the 'users' collection as long
as the username and e-mail address are not already in use.
'''


@app.route("/register", methods=["GET", "POST"])
def register():
    # a user cannot access this page if already logged in, as this would
    # not make sense
    if "user" in session:
        flash("You are already logged in!")
        return redirect("home_page")
    # if no user is in session, the register page will be rendered
    else:
        if request.method == "POST":
            # checks whether unique pieces of user data already exist in the
            # database
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})
            existing_email = mongo.db.users.find_one(
                {"email_address": request.form.get("email").lower()})
            # the superuser field allows the site administrator to access
            # certain pages and take actions that standard users cannot
            is_superuser = True if request.form.get(
                            "username").lower() == "admin" else False

            # prevents multiple users sharing one username
            if existing_user:
                flash("User already exists")
                return redirect(url_for("register"))

            # prevents multiple accounts being linked to the same e-mail
            # address
            if existing_email:
                flash("An account already exists for this e-mail address!")
                return redirect(url_for("register"))

            # creates the new user and adds them to the database
            create_account = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                            request.form.get("password")),
                "email_address": request.form.get("email").lower(),
                "is_superuser": is_superuser
            }
            mongo.db.users.insert_one(create_account)

            # adds the user to the session cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration successful!")
            return redirect(url_for("home_page", username=session["user"]))
        return render_template("register.html")


'''
This function puts an existing user in session if their details are entered
correctly
'''


@app.route("/login", methods=["GET", "POST"])
def login():
    # a user cannot access this page if already logged in, as this would
    # not make sense
    if "user" in session:
        flash("You are already logged in!")
        return redirect("home_page")
    # if no user is in session, the login page will be rendered
    else:
        if request.method == "POST":
            # checks if the username exists in the database
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ensures the hashed password for that username matches user
                # input
                if check_password_hash(existing_user["password"],
                   request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for(
                            "home_page", username=session["user"]))

                else:
                    # rejects login attempt if password does not match
                    flash("Invalid login credentials!")
                    return redirect(url_for("login"))

            else:
                # rejects login attempt if username does not exist
                flash("Invalid login credentials!")
                return redirect(url_for("login"))
        return render_template("login.html")


'''
This function signs the user out of the application.
'''


@app.route("/logout")
def logout():
    # removes the user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home_page"))


'''
This function displays the user's individual profile. By taking the username
argument, the content on the page is unique to each individual user.
'''


@app.route("/profile/<username>")
def profile(username):
    # renders a custom 404 page if the value of the username argument does
    # not exist
    if mongo.db.users.find_one({"username": username}) is None:
        return render_template("404.html"), 404

    # checks that the user is logged in to access the page
    if "user" in session:
        # ensures the value of the username argument matches the username of
        # the user in session
        if username == mongo.db.users.find_one(
                       {"username": session["user"]})["username"]:
                terms = list(mongo.db.terms.find().sort("term_name", 1))
                return render_template("profile.html",
                                       username=username, terms=terms)
        # the user is redirected if attempting to access another user's profile
        else:
            flash("You do not have permission to view other users' profiles")
            return redirect(url_for("home_page"))

    # the page is only available to users in session. If the user is not
    # logged in, they are redirected to the login page
    else:
        flash("Please log in to view your profile")
        return redirect(url_for("login"))


'''
This function retrieves all the terms from the database and renders them onto
the dictionary page, sorting in alphabetical order.
'''


@app.route("/view_dictionary")
def view_dictionary():
    terms = list(mongo.db.terms.find().sort("term_name", 1))
    return render_template("dictionary.html", terms=terms)


'''
This function enables a user to add an entry to the dictionary, provided the
word they are adding does not already exist, and renders the new data onto
the dictionary page.
'''


@app.route("/add_definition", methods=["GET", "POST"])
def add_definition():
    # checks that the user is logged in
    if "user" in session:
        # submits the form to the database
        if request.method == "POST":
            # searches the database to check if the term name entered by the
            # user already exists in the database
            existing_term = mongo.db.terms.find_one(
                {"term_name": request.form.get("term_name").capitalize()})
            # prevents the user from adding a word that already exists
            if existing_term:
                flash("This term already exists in the dictionary."
                      " Please add another term.")
                return redirect(url_for("add_definition"))

            # creates the new term and adds it to the database
            new_term = {
                "term_name": request.form.get(
                    "term_name").capitalize().strip(),
                "term_definition": request.form.get(
                    "term_definition").capitalize().strip(),
                "created_by": session["user"],
                "created_on": datetime.datetime.
                today().strftime("%m/%d/%y %H:%M:%S"),
                "contribution_value": 1,
                "score": 0,
                "first_letter": str(request.form.get("term_name").
                                    capitalize().strip())[0]
            }
            mongo.db.terms.insert_one(new_term)
            flash("Term successfully created. You will now be redirected to"
                  "the dictionary page where you can see your contribution!")
            return redirect(url_for("view_dictionary"))
        terms = mongo.db.terms.find()
        users = mongo.db.users.find()
        return render_template("add_definition.html", terms=terms, users=users)
    # prevents users who are not logged in from accessing this page
    else:
        flash("Please log in to perform this action.")
        return redirect(url_for("login"))


'''
This function allows the user to edit entries that they have created, and
renders the updated data onto the dictionary page.
'''


@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    # checks that the user is logged in
    if "user" in session:
        # ensures the ObjectId is a valid BSON type
        if ObjectId.is_valid(term_id):
            # renders a 404 page if the ObjectId does not exist in the database
            # even if it is valid
            if mongo.db.terms.find_one({"_id": ObjectId(term_id)}) is None:
                return render_template("404.html"), 404

            # retrieves the username of the user that created the entry
            term_creator = mongo.db.terms.find_one(
                {"_id": ObjectId(term_id)})["created_by"]
            # finds any superusers in the database
            is_superuser = mongo.db.users.find_one(
                {"is_superuser": True})["username"]
            # searches the database for term names that match the user's input
            existing_term = mongo.db.terms.find_one(
                {"term_name": request.form.get("term_name")})
            # submits the updated form to the database
            if request.method == "POST":
                updated_term = {
                    "term_name": request.form.get(
                        "term_name").capitalize().strip(),
                    "term_definition": request.form.get(
                        "term_definition").capitalize().strip(),
                    "created_by": term_creator,
                    "created_on": datetime.datetime.
                    today().strftime("%m/%d/%y %H:%M:%S"),
                    "contribution_value": 1,
                    "score": 0
                }

                # prevents the user from changing the term name to one
                # that already exists elsewhere in the dictionary
                if existing_term:
                    # lets the user update the entry if the term name has
                    # not been changed and renders the updated data
                    # on the dictionary page
                    current_term = mongo.db.terms.find_one(
                        {"_id": ObjectId(term_id)})["term_name"]
                    if request.form.get("term_name").capitalize().strip() == current_term:
                        mongo.db.terms.update(
                            {"_id": ObjectId(term_id)}, updated_term)
                        flash(
                             "Dictionary information successfully updated")
                        return redirect(url_for("view_dictionary"))
                    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
                    flash("This term already exists in the dictionary."
                          " Please add another term.")
                    return render_template("edit_term.html", term=term)

                # grants the user editing permissions for an entry if they
                # are its creator or if the user in session is a site
                # administrator
                if session["user"] == term_creator or session["user"] == is_superuser:
                    mongo.db.terms.update(
                        {"_id": ObjectId(term_id)}, updated_term)
                    flash("Dictionary information successfully updated")
                    return redirect(url_for("view_dictionary"))
                # prevents users who are not administrators changing other
                # users' entries
                else:
                    flash("You cannot edit terms created by other users.")
                    return redirect(url_for("view_dictionary"))

                flash("Dictionary information successfully updated")
                return redirect(url_for("view_dictionary"))
        # renders a custom 404 page if the ObjectId passed is not a valid
        # BSON type
        else:
            return render_template("404.html"), 404

        term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
        terms = mongo.db.terms.find().sort("term_name", 1)
        return render_template("edit_term.html", term=term, terms=terms)
    # prevents users who are not logged in from accessing this page
    else:
        flash("You must log in to perform this action.")
        return redirect(url_for("login"))


'''
This function removes a dictionary term from the database.
'''


@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    # checks that the user is logged in
    if "user" in session:
        # ensures the ObjectId is a valid BSON type
        if ObjectId.is_valid(term_id):
            # renders a 404 page if the ObjectId does not exist in the database
            # even if it is valid
            if mongo.db.terms.find_one({"_id": ObjectId(term_id)}) is None:
                return render_template("404.html"), 404
            # ensures that the entry can only be deleted by its creator
            # or an administrator
            else:
                term_creator = mongo.db.terms.find_one(
                    {"_id": ObjectId(term_id)})["created_by"]
                is_superuser = mongo.db.users.find_one(
                    {"is_superuser": True})["username"]
                # removes entry from the database provided the user is its
                # creator or an admin
                if session["user"] == term_creator or session["user"] == is_superuser:
                    mongo.db.terms.remove({"_id": ObjectId(term_id)})
                    flash("Term deleted from dictionary")
                    return redirect(url_for("view_dictionary"))
                # prevents users who are not administrators from deleting
                # other users' entries
                else:
                    flash("You cannot delete terms created by other users")
                    return redirect(url_for("view_dictionary"))
        # renders a custom 404 page if the ObjectId passed is not a valid
        # BSON type
        else:
            return render_template("404.html"), 404
    # prevents users who are not logged in from deleting database records
    else:
        flash("You must log in to perform this action.")
        return redirect(url_for("login"))


'''
This function increases the term's score by one with each click, updates the
record in the database and renders the updated score on the dictionary page.
'''


@app.route("/upvote/<term_id>", methods=["GET", "POST"])
def upvote(term_id):
    # checks that the user is logged in
    if "user" in session:
        # ensures the ObjectId is a valid BSON type
        if ObjectId.is_valid(term_id):
            # renders a 404 page if the ObjectId does not exist in the database
            # even if it is valid
            if mongo.db.terms.find_one({"_id": ObjectId(term_id)}) is None:
                return render_template("404.html"), 404

            # increases the term's score by one
            term = mongo.db.terms.find_one_and_update(
                {"_id": ObjectId(term_id)}, {"$inc": {"score": 1}})
            return redirect(url_for("view_dictionary", term=term))
        # renders a custom 404 page if the ObjectId passed is not a valid
        # BSON type
        else:
            return render_template("404.html"), 404
    # prevents users who are not logged in from upvoting entries
    else:
        flash("You must log in to perform this action")
        return redirect(url_for("login"))


'''
This function decreases the term's score by one with each click, updates the
record in the database and renders the updated score on the dictionary page.
'''


@app.route("/downvote/<term_id>", methods=["GET", "POST"])
def downvote(term_id):
    # checks that the user is logged in
    if "user" in session:
        if ObjectId.is_valid(term_id):
            # renders a 404 page if the ObjectId does not exist in the database
            # even if it is valid
            if mongo.db.terms.find_one({"_id": ObjectId(term_id)}) is None:
                return render_template("404.html"), 404

            # decreases the term's score by one
            term = mongo.db.terms.find_one_and_update(
                {"_id": ObjectId(term_id)}, {"$inc": {"score": -1}})
            return redirect(url_for("view_dictionary", term=term))
        # renders a custom 404 page if the ObjectId passed is not a valid
        # BSON type
        else:
            return render_template("404.html"), 404
    # prevents users who are not logged in from downvoting entries
    else:
        flash("You must log in to perform this action")
        return redirect(url_for("login"))


'''
This function lets the user update their login details and stores the updated
details in the database.
'''


@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    # checks the user is logged in
    if "user" in session:
        if request.method == "POST":
            # maintains an administrator's superuser status should they update
            # their login information
            is_superuser = True if mongo.db.users.find_one(
                {"username": username, "is_superuser": True}) else False
            updated_account = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "email_address": request.form.get("email").lower(),
                "is_superuser": is_superuser
            }
            # searches the database for usernames and email addresses that
            # match the user's input
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})
            existing_email = mongo.db.users.find_one(
                {"email_address": request.form.get("email").lower()})
            # retrieves the user's existing e-mail address from the database
            email_address = mongo.db.users.find_one(
                {"username": username})["email_address"]

            if existing_user:
                if username == request.form.get("username").lower():
                    if existing_email:
                        # if the user enters the same username and e-mail
                        # address their profile is updated
                        if email_address == request.form.get("email").lower():
                            mongo.db.users.update(
                                {"username": username}, updated_account)
                            session["user"] = request.form.get(
                                "username").lower()
                            flash("Your profile was successfully updated")
                            return redirect(url_for(
                                "profile", username=username))

                        # prevents the user from using an e-mail address
                        # already linked to another user
                        flash(
                         "An account already exists for this e-mail address!")
                        return render_template(
                            "update_profile.html", username=username)

                    # updates the user's details if the user has kept their
                    # username and entered a new e-mail address that was not
                    # previously in the database
                    mongo.db.users.update(
                        {"username": username}, updated_account)
                    session["user"] = request.form.get("username").lower()
                    flash("Your profile was successfully updated")
                    return redirect(url_for("profile", username=username))

                # prevents the user from using a username already owned by
                # another user
                else:
                    flash("Username already exists!")
                    return render_template(
                        "update_profile.html", username=username)

            else:
                if existing_email:
                    # lets the user update their profile when they keep the
                    # same e-mail address and enter a new username that was not
                    # previously in the database
                    if email_address == request.form.get("email").lower():
                        mongo.db.users.update(
                            {"username": username}, updated_account)
                        session["user"] = request.form.get("username").lower()
                        flash("Your profile was successfully updated")
                        return redirect(url_for(
                            "profile", username=session["user"]))

                    # prevents the user from using an e-mail address already
                    # linked to another user
                    flash("An account already exists for this e-mail address!")
                    return render_template(
                        "update_profile.html", username=username)

            # updates the user in the database and stores the updated user
            # information in the session cookie
            mongo.db.users.update({"username": username}, updated_account)
            session["user"] = request.form.get("username").lower()
            flash("Your profile was successfully updated")
            return redirect(url_for("profile", username=session["user"]))

        return render_template("update_profile.html", username=username)
    # prevents users who are not logged in from updating profiles
    else:
        flash("Please log in to update your profile")
        return redirect(url_for("login"))


'''
This function logs the user out before deleting their account and removing
their record from the database.
'''


@app.route("/delete_account/<username>")
def delete_account(username):
    # checks that the user is logged in
    if "user" in session:
        # ensures the username of the account to be deleted matches the
        # username argument
        deleted_user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # removes the user from the session cookie and the database and
        # redirects them to the home page
        if username == deleted_user:
            users = mongo.db.users.find()
            session.pop("user")
            mongo.db.users.remove({"username": username})
            flash("Your account was deleted."
                  "You will now be redirected to the home page.")
            return redirect(url_for(
                            "home_page", username=username, users=users))
        # prevents users from deleting somebody else's account if somebody
        # else's username is passed in
        else:
            flash("You are not authorised to perform this action.")
            return redirect(url_for("home_page"))
    # prevents users who are not logged in from deleting accounts
    else:
        flash("You are not authorised to perform this action.")
        return redirect(url_for("home_page"))


'''
This function allows site administrators to view a list of registered users
and certain data such as their usernames and e-mail addresses.
'''


@app.route("/manage_users")
def manage_users():
    # checks that the user is logged in
    if "user" in session:
        # ensures that the user in session has superuser status
        is_superuser = mongo.db.users.find_one(
            {"is_superuser": True})["username"]
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # renders the page if the user is a superuser
        if username == is_superuser:
            users = mongo.db.users.find().sort("username", 1)
            return render_template("manage_users.html", users=users)
        # prevents non-superusers from accessing the page
        else:
            flash("You are not authorised to view this page")
            return redirect(url_for("home_page"))
    # prevents users who are not logged in from accessing the page
    else:
        flash("You are not authorised to view this page")
        return redirect(url_for("home_page"))


'''
This function enables administrators to add a new user to the database if a
user is having difficulty signing up.
'''


@app.route("/add_new_user", methods=["GET", "POST"])
def add_new_user():
    # checks that the user is logged in
    if "user" in session:
        # ensures that the user in session has superuser status
        is_superuser = mongo.db.users.find_one(
            {"is_superuser": True})["username"]
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # renders the page if the user is a superuser
        if username == is_superuser:
            if request.method == "POST":
                # checks whether the username and e-mail address already exist
                # in the database
                existing_user = mongo.db.users.find_one(
                    {"username": request.form.get("username").lower()})
                existing_email = mongo.db.users.find_one(
                    {"email_address": request.form.get("email").lower()})
                is_superuser = True if request.form.get(
                    "username").lower == "admin" else False

                # prevents an account being added with username already in use
                if existing_user:
                    flash("User already exists")
                    return redirect(url_for("add_new_user"))

                # prevents an account being added with an e-mail already in use
                if existing_email:
                    flash("An account already exists for this e-mail address!")
                    return redirect(url_for("add_new_user"))

                # adds the new user to the database
                new_user = {
                    "username": request.form.get("username").lower(),
                    "password": generate_password_hash(
                        request.form.get("password")),
                    "email_address": request.form.get("email").lower(),
                    "is_superuser": is_superuser
                }
                mongo.db.users.insert_one(new_user)
                flash("The user was successfully added to the database.")
                return redirect(url_for("manage_users"))

            users = mongo.db.users.find()
            return render_template("add_new_user.html")

        # prevents non-superusers from accessing the page
        else:
            flash("You are not authorised to view this page.")
            return redirect(url_for("home_page"))

    # prevents users who are not logged in from accessing the page
    else:
        flash("You are not authorised to view this page.")
        return redirect(url_for("home_page"))


'''
This function allows administrators to delete a user from the database if
they have not been using the application appropriately.
'''


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    # checks that the user is logged in
    if "user" in session:
        # ensures that the user in session has superuser status
        is_superuser = mongo.db.users.find_one(
                {"is_superuser": True})["username"]
        username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
        # removes the selected account from the database if the user is a
        # superuser
        if username == is_superuser:
            users = mongo.db.users.find()
            user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            mongo.db.users.remove({"_id": ObjectId(user_id)})
            flash("The user was successfully deleted from the database.")
            return redirect(url_for("manage_users"))
        # prevents non-superusers from accessing performing this action
        else:
            flash("You are not authorised to perform this action.")
            return redirect(url_for("home_page"))
    # prevents users who are not logged in from performing this action
    else:
        flash("You are not authorised to perform this action.")
        return redirect(url_for("home_page"))


'''
This function renders the site's address and contact information. There are
no restrictions on who can view this page and no user-specific actions.
'''


@app.route("/contact")
def contact():
    return render_template("contact.html")


'''
This function handles invalid URLs by rendering a custom 404 page. Credit
to the Flask documentation for this solution.
'''


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
