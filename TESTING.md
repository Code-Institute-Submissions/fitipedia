# **[Fitipedia!](https://fitipedia.herokuapp.com)**

# Testing

This file documents the testing process of the project.

## Table of contents

* [Validation](#validation)
* [Responsiveness](#responsiveness)
* [Browser Compatibility](#browser-compatibility)
* [Testing User Stories](#testing-user-stories)
* [Issues and Bugs](#issues-and-bugs)

## [Back to README](README.md)

### Validation

#### Python

The code was passed through the [PEP8](http://pep8online.com/) validator. No errors were found.

![PEP8 validation](/libraries/code_validation/python_validation_pep8.png)

#### JavaScript

Each JavaScript file was passed through the [JSHint](https://jshint.com/) validator. No errors were found on either.

![JSHint validation script.js](/libraries/code_validation/js_validation_jshint_script.png)

![JSHint validation maps.js](/libraries/code_validation/js_validation_jshint_maps.png)

#### CSS

The code was passed through the [Jigsaw](https://jigsaw.w3.org/) validator. No errors were found.

![Jigsaw validation](/libraries/code_validation/css_validation_jigsaw.png)

#### HTML

The code was passed through the [W3C](https://validator.w3.org/) validator. A number of unavoidable errors were thrown relating to Jinja templating characters, but there were no errors in the HTML itself.

The errors mostly relate to bad values with curly brackets inside href attributes denoting a url_for Flask function, and missing HTML start tags on files extending from the base template. As this does not affect the app's functionality, and changing them would actually make performance impossible, no action was taken on these errors.

![W3C Validation](/libraries/code_validation/html_validation_w3c.png)

![W3C Validation base.html errors](/libraries/code_validation/html_validation_w3c_base_template.png)

[Back to TOC](#table-of-contents)

### Responsiveness

The website was tested in Google Chrome using the Viewport Resizer extension, Chrome DevTools and the Responsive Design Checker.

The website's layout was tested pixel by pixel and on all popular mobile and tablet devices. The design is consistently responsive at all screen sizes and there is no change in the appearance or performance of interactive features.

No issues, major or minor, were found.

[Back to TOC](#table-of-contents)

### Browser Compatibility

The application was tested in the following browsers:

* Google Chrome
* Mozilla Firefox
* Brave Browser
* Opera
* Safari

The application proved itself highly compatible with all browsers and performance was consistent across the board. Only one minor issue was noted:

* Smooth scroll behaviour is not supported on Safari, meaning the page jumps right back to the top when the return to top button is clicked as opposed to a smooth scrolling motion. This is due to Safari not supporting the `scroll-behavior: smooth` CSS property.
    * I tried various JavaScript solutions to remedy this, but none of them had any effect, and some even hindered the app's performance. As this is a relatively minor issue, I decided not to take any further action at this stage.

[Back to TOC](#table-of-contents)

### Testing User Stories

##### All Users

* As a user, I want to be able to search for fitness jargon and its meaning.
    * I click on the 'Search Dictionary' button and am taken to the search bar. I enter a keyword, click search and find the word I'm
    looking for in the results
* As a user, I want to read a list of many different fitness terminologies.
    * I click on the 'View Dictionary' tab in the navbar and can read the terms in alphabetical order
    * I am informed that if I want to contribute to the dictionary myself and engage with other users, I must create an account and am
    invited to do so before the dictionary begins
* As a user and fitness enthusiast, I want to follow the dictionary's work and potentially get in touch with them.
    * I scroll down to the page footer which typically contains such information, and can immediately see Fitipedia's social media handles
    * I also spot a 'Contact Us' link next to the copyright text. I open it and am taken to a separate page containing Fitipedia's contact
    details, opening hours and office address next to a Google Maps widget that I can navigate to get a clearer idea of the location
* As a user, I want to see some examples of words in the dictionary.
    * I scroll slightly down the home page and see the list of most popular entries, sorted by score from highest to lowest
    * If these look intriguing, I have the opportunity to view the full dictionary by clicking on the button below
* As a user who is knowledgeable about fitness or wants to thank other users for their content, I want to register for an account
    * I click on the Register tab in the navbar, fill out my details and my account is created in seconds
* As a returning user, I want to sign in and create some entries, edit one of my existing entries or upvote/downvote another user's entry
    * I click on theLogin tab in the navbar, enter my username and password and am logged in where I can now make use of the site's full
    functionality
* As a user, I mistakenly enter an invalid URL
    * I land on a 404 page with a button that redirects me to the homepage when clicked on
* As a user, I enter a URL that only registered and logged in users can access
    * I am redirected to the login page and see a flash message that tells me I need to be logged into access this page or perform this
    action
    * I can then log in and perform the action if I wish

##### Registered Users

* As a registered user, I want to add a new word to the dictionary
    * I click on the Add Definition tab in the navbar and enter the term and its definition in the fields provided
    * I click on the Add to Dictionary button and am redirected to the dictionary page to look at my entry
* As a registered user, I want to add a word to the dictionary that I don't realise already exists in there
    * I click on the Add Definition tab and enter the term and its definition
    * As the term name matches the name of a record already in the database, I receive a flash message that this term already exists in the
    dictionary and am redirected back to the form
* As a registered user, I want to update one of my entries as I think it can be improved
    * I search for the term in the dictionary, click the Edit Details button, amend the information in the requirement feelds and click
    the Update Term Information button below
    * I am redirected to the dictionary page where I can see my updated entry
* As a registered user, I want to show my appreciation for another user's informative entry
    * I go to the dictionary page, locate the user's entry and click on the green thumbs up button to upvote the term
    * I receive a green flash message that the term has been upvoted, and can see the score has increased by one on the page
* As a registered user, I don't like someone else's definition of a term, do not find it helpful or can see a user abusing the app
    * I locate the relevant entry and click on the red thumbs down button to downvote the term
    * I receive a red flash message that the term has been downvoted, and the score has decreased by one on the page
* As a registered user, I want to delete one of my entries as I'm not happy with it or don't think it's relevant
    * I click the My Profile tab and find the term within my history of contributions (N.B. if it's a very recent one, I can find it on the
    homepage under my last 5 entries)
    * I click the Delete Term button and confirm the deletion by clicking Delete again
* As a user, I don't want to delete an entry but accidentally clicked the delete button
    * A confirmation box pops up asking whether I'm sure I want to delete the term from the dictionary
    * I click cancel and am taken back to the page I was on before
* As a registered user, I want to see some information about my recent activity on the homepage
    * I log in and can see my last 5 entries, sorted by date from the most recent
    * I can edit and delete these entries here if I want to change them, which saves time as I don't have to navigate to the dictionary page
    * I can easily add another entry if I wish by clicking on the button below
* As a registered user, I want to look at my profile information
    * I click the My Profile tab in the navbar and can see information such as my username, total number of contributions and a list of each
    individual entry I have made
    * If I wish, I can edit my details, edit and delete my entries, or delete my account
* As a registered user, I've decided the app is no longer for me and wish to delete my account
    * I head over to my profile page, scroll down to the Delete Account section and click the button to delete my account
    * In the confirmation box, I confirm the deletion by clicking on Delete again
    * I am redirected to the homepage, no longer logged in
* As a registered user, I have accidentally clicked on Delete Account and wish to cancel this
    * In the confirmation box, I click on Cancel and am taken back to the my profile page

##### Administrators

* As an administrator, I want to remove a user from the database who has been behaving inappropriately
    * I click on the Manage Users tab in the navbar, locate the user by their username in the list of users and click on Delete User
    * In the confirmation box, I confirm the deletion by clicking on Delete
    * I am redirected back to the Manage Users page and the record no longer appears in the list of users
* As an administrator, I see an entry by another user that doesn't look quite right, and want to change it to maintain the site's reputation
    * I locate the term and click on Edit Details or Delete Term and make the necessary changes as if I were the creator of that entry
    * I am redirected to the Dictionary page and the term is either no longer there or showing with its updated definition
* As an administrator, a potential new user has contacted Fitipedia saying they are unable to sign up. I therefore want to add a new user
to the database
    * I go to the Manage Users page, scroll to the bottom of the list of registered users and select Add New User
    * I fill out the user's desired username and e-mail address and assign them a password, which I recommend them to change upon logging in
    * The user now appears in the list of users

[Back to TOC](#table-of-contents)

### Issues and Bugs

#### Bugs during testing

Here is a list of bugs I encountered during the testing phase followed by the solution applied to fix each one.

* **Bug**: a user could access forms to add, edit and delete entries when they were not even logged in due to the URLs not being protected.
* **Fix**: I added an `if "user" in session:` condition for pages that are not publicly viewable and a redirect to the login page in the else block. A user receives a flash message prompting them that they must log in to view certain pages or perform certain actions.

* **Bug**: a user could access sensitive data such as other user profiles by copying the username of another user into the URL, and even delete another user's account this way
* **Fix**: I added multi-layered if conditions to stop this happening. See the 'delete_user' view as an example below, that only administrators(superusers) are authorised to carry out:
    ```
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
    ```

* **Bug**: a user could enter an invalid URL and be taken to a standard 404 error page
* **Fix**: I designed a [custom 404 page](templates/404.html) that fits with the rest of the site's design with a button that takes the user back to the homepage, and built the following error handling function in the Python file:

    ```
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404
    ```

* **Bug**: For views that passed an ObjectId as an argument, an invalid ObjectId would render a 404 page, but an ObjectId that was valid but didn't exist threw a BSON type ObjectId error
* **Fix**: I used the None keyword to create an if condition that searches through each ObjectId in the relevant MongoDB collection and renders the same 404 page if it does not exist. Here is a snippet of the edit_term view as an example:

    ```
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
    ```

* **Bug**: When upvoting or downvoting, the user would receive visual feedback confirming their action, but the term's score would not change. It would only change after the page was refreshed. Worse still, if you kept refreshing the page, the score would keep increasing or decreasing without having to even click the button.
* **Fix**: I solved this by setting the function to return a redirect rather than render_template, keeping the term as an argument. See the code snippet for the upvote view below:

    ```
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
    ```

* **Bug**: After adding modal functionality to ask the user to confirm a delete action, the confirmation box would show the first term in any sorted list, regardless of the one clicked on. If I confirmed deletion, the first term would also be deleted and the term intended for deletion would remain in the database.
* **Fix**: The modal functionality was part of a Jinja for loop that was iterating through each term. Therefore the id of the modal <div> element was not unique. Each entry had the same id, so the first object found sharing that id was passed to the front end. I fixed this by giving each modal div the id of the ObjectId of its respective term using `id="{{ term._id }}"` and setting the href of the corresponding anchor tag accordingly. See the example below:

    ```
    {% for term in terms %}
        ...
        <a href="#{{ term._id }}" class="btn-small red modal-trigger">
            <i class="fas fa-trash-alt tooltipped" data-tooltip="DELETE TERM"></i>
        </a>
        <div id="{{ term._id }}" class="modal">
            <div class="modal-content center-align">
                <p>Are you sure you want to delete the term {{ term.term_name }}&#63;</p>
            </div>
            <div class="modal-footer">
                <div class="row center-align">
                    <div class="col s12 m6">
                        <a href="{{ url_for('home_page') }}" class="btn grey cancel">Cancel</a>
                    </div>
                    <div class="col s12 m6">
                        <a href="{{ url_for('delete_term', term_id=term._id) }}" class="btn red delete-record">Delete</a>
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
    ```

* **Bug**: Users were able to upvote their own entries after creating them.
* **Fix**: I added if conditions using Jinja that users could only vote on terms created by others unless they were an administrator.

    ```
    {% if session.user and session.user|lower != term.created_by|lower or session.user|lower == "admin"|lower %}
        <div class="col s3 m2 xl1">
            <a href="{{ url_for('upvote', term_id=term._id) }}" class="btn upvote green" onclick="confirmUpvote()" data-position="top">
                <i class="fas fa-thumbs-up tooltipped" data-tooltip="UPVOTE"></i>
            </a>
            <div class="upvote-container center-align"></div>
        </div>
        <div class="col s3 m2 xl1">
            <a href="{{ url_for('downvote', term_id=term._id) }}" class="btn downvote red" onclick="confirmDownvote()" data-position="top">
                <i class="fas fa-thumbs-down tooltipped" data-tooltip="DOWNVOTE"></i>
            </a>
            <div class="downvote-container center-align"></div>
        </div>
    {% endif %}
    ```

* **Bug**: Users were able to edit and delete content created by others.
* **Bug**: I added if conditions using Jinja that users could only edit and delete their own entries, with the exception of administrators who can access any user's entries.

    ```
    {% if session.user|lower == "admin" or session.user|lower == term.created_by|lower %}
        <div class="row">
            <div class="col s6">
                <a href="#{{ term._id }}" class="btn-small delete right red modal-trigger">
                    <span>Delete term</span><i class="fas fa-trash-alt tooltipped" data-tooltip="DELETE TERM"></i>
                </a>
                ...
            </div>
            <div class="col s6">
                <a href="{{ url_for('edit_term', term_id=term._id) }}" class="btn-small edit blue">
                    <span>Edit details</span><i class="fas fa-pen-square tooltipped" data-tooltip="EDIT DETAILS"></i>
                </a>
            </div>
        </div>
    {% endif %}
    ```

* **Bug**: Users were unable to sign up using an existing username or e-mail address, but could change these to existing values when submitting the form to update their profile.
* **Fix**: I retrieved user values from MongoDB to store in variables and created if conditions around these that would redirect the user to their profile page if attempting to change to an existing username or e-mail address. At the same time, I added exceptions that let the user keep their current username and e-mail address (as these are also existing values):

    ```
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
    ```

* **Bug**: Users could submit a string of white spaces as a term's name and definition, and have this appear in the dictionary.
* **Fix**: With the help of jQuery, I used the following JavaScript code to prevent the inputting of successive whitespace in textarea and input fields:

    ```
    $("#term_definition").on("keydown", function (e) {
        var inputValue = $("#term_definition").val();
        if (inputValue.length == 0 || inputValue.slice(-1) == " ") {
            return e.which !== 32;
        }
    });
    $("input").on("keydown", function (e) {
        var inputValue = $("input").val();
        if (inputValue.length == 0 || inputValue.slice(-1) == " ") {
            return e.which !== 32;
        }
    });
    ```

* **Bug**: When resetting the search form, the entire page would refresh and return to the top of the screen, which is quite annoying user experience.
* **Fix**: I used the form.reset() method in JavaScript:

    ```
    <form id="search_bar" method="POST" action="{{ url_for('search') }}">
        ...
        <a onclick="resetSearch()" class="red btn">Reset</a>
        <button type="submit" class="btn teal">Search</button>
        ...
    </form>

    function resetSearch() {
        document.getElementById("search_bar").reset();
    }
    ```

#### Bugs still to be fixed

A couple of minor issues remain which do not affect site performance or security. These are:

* When clicking on the search call to action button, the page scrolls too far so that the search bar disappears from the top of the page. This happens on mobile devices and when users are not logged in. This happened after I made the navbar fixed - the search bar remains at the top of the viewport, but it is actually hidden behind the navbar.
    * This is not an issue on tablet and desktop devices when the user is logged in, as the search form is pushed down by the welcome heading to the user. I wrapped these two elements in a div with the id of search, and set the href of the search button to #search. This makes no difference when the user is logged out, however, as the starting position of the outer div is the same as that of the form.

* The console throws the following JavaScript error when on any page other than the Contact page.

![JavaScript console error](/libraries/testing/js_console_error.png)

I was unable to find a reliable solution to this issue. Strangely, when on the Contact page that actually renders the map, no such error appears. As this has no impact on site performance or security, I have not resolved the error at this stage, but will aim to have the console free of errors when producing future versions of the application. I am reluctant to remove the Contact page as I feel this is potentially useful to the user and makes the app appear more professional.

* There are other minor improvements to be made to the site that time unfortunately did not allow to be made. For examples of these, see the Features left to implement section in the [README](README.md#features-left-to-implement) file.

[Back to TOC](#table-of-contents)

[Back to README.md](README.md)