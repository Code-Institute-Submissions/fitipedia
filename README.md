# **[Fitipedia!](https://fitipedia.herokuapp.com)**

## The free online fitness dictionary

![](libraries/readme_images/site_responsiveness.png)

This application was inspired by one of the [Code Institute](https://codeinstitute.net/)'s project ideas: 
**Create a jargon glossary/dictionary for a particular domain**. Fitness is not only a passion of mine but also
an area in which a great deal of jargon exists that many members of the community struggle to understand.
This website is an online dictionary that explains fitness terminology in a way that is suitable for both
beginners and more advanced practitioners. It serves two main purposes:

1. Users can read and browse the dictionary to find definitions of terminology that has confused them.
1. Fitness experts can use the site to contribute definitions of terminology to help educate the wider community

Registered users are able to add their own entries to the dictionary, as well as modify and delete them if they wish.
Users are encouraged to engage with the community and can vote on each others' entries (each entry has a score based 
on the number of up/down votes) to ensure terminology definitions are as accurate as possible. Users will also receive
feedback on the accuracy of their own entries as fellow users will be able to vote on them.

This app would be of interest for:

* anyone who wants to design a training plan but is put off by the amount of jargon they come across online
* anyone who wants to educate themselves about fitness and better understand the science behind training
* anyone knowledgeable about fitness who enjoys educating others on the subject and sharing their opinion
* fitness professionals who struggle to break down complex concepts to layman clients and need a way to explain themselves
more clearly

The nature of the website is clearly explained in the name Fitipedia, which is a fitness-related play on 
[Wikipedia](https://wikipedia.org), the world's largest encyclopaedia.

The deployed website is available [here](https://fitipedia.herokuapp.com)

## Table of contents

* [UX](#ux)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Data Structure](#data-structure)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits and Acknowledgements](#credits-and-acknowledgements)

### UX

#### Design

A clear and professional design using muted colours that are not dull. Each database entry is in a card panel to make it stand out.
Most of the layout comes from functionality provided by [Materialize CSS](https://materializecss.com). The jumbotron image on the home
page gives the site some character and makes it crystal clear to the user that this is a fitness-related website. The user is invited to
click on the 'Click Here' text before browsing where they can read about the site's purpose and how to use it effectively. 

Once registered, the user can intuitively perform all CRUD actions. Each button that performs an action is assigned a corresponding colour
depending on which CRUD function it represents:

* **Create (C)** all buttons that add data to the website are **<span style="color:green">green</span>**
* **Read (R)** all buttons that locate and read data on the website are **<span style="color:teal">teal</span>**
* **Update (U)** all buttons that edit and update data on the website are **<span style="color:aqua">blue</span>**
* **Delete (D)** all buttons that remove data from the website are **<span style="color:red">red</span>**

The exception is the gold 'Search Dictionary' button on the home page, which serves as the app's main call to action button.

The upvote and downvote buttons and the icons that they display also make their purpose clear to the user, as the colour green is
associated with approval, while red is associated with disapproval. Each term's score is shown in larger text so that the user is left in 
no doubt.

All delete actions initiated by the user bring up a confirmation box asking the user if they're sure they want to delete something in the
event they clicked the button mistakenly. The user can select cancel, which has the more neutral colour of grey, if they do not wish to
delete a piece of data.

The following fonts are used:

* **Commissioner** for main body of content, which gives the site a more informal but still informative feel
* **Big Shoulders Inline Text** for the jumbotron header, which gives a robust look, more associated with fitness
* **Bodoni Moda** for the Fitipedia brand logo
* **Yusei Magic** for the site information modal trigger, as it clearly stands out from the other text and is more likely to prompt a click
from the user

The navbar is fixed because content on certain pages, particularly the dictionary page, can be very long.

#### User Stories

##### All Users

* As a user, I want to be able to search for fitness jargon and its meaning.
* As a user, I want to read a list of many different fitness terminologies.
* As a user and fitness enthusiast, I want to follow the dictionary's work and potentially get in touch with them.
* As a user, I want to see some examples of words in the dictionary.
* As a user who is knowledgeable about fitness or wants to thank other users for their content, I want to register for an account
* As a returning user, I want to sign in and create some entries, edit one of my existing entries or upvote/downvote another user's entry
* As a user, I mistakenly enter an invalid URL
* As a user, I enter a URL that only registered and logged in users can access

##### Registered Users

* As a registered user, I want to add a new word to the dictionary
* As a registered user, I want to add a word to the dictionary that I don't realise already exists in there
* As a registered user, I want to update one of my entries as I think it can be improved
* As a registered user, I want to show my appreciation for another user's informative entry
* As a registered user, I don't like someone else's definition of a term, do not find it helpful or can see a user abusing the app
* As a registered user, I want to delete one of my entries as I'm not happy with it or don't think it's relevant anymore
* As a user, I don't want to delete an entry but accidentally clicked the delete button
* As a registered user, I want to see some information about my recent activity on the homepage
* As a registered user, I want to look at my profile information
* As a registered user, I've decided the app is no longer for me and wish to delete my account
* As a registered user, I have accidentally clicked on Delete Account and wish to cancel this

##### Administrators

* As an administrator, I want to remove a user from the database who has been behaving inappropriately
* As an administrator, I see an entry by another user that doesn't look quite right, and want to change it to maintain the site's reputation
* As an administrator, a potential new user has contacted Fitipedia saying they are unable to sign up. I therefore want to add a new user
to the database

#### Wireframes

I used [Wireframe.cc](https://wireframe.cc) to design wireframes for desktop/laptop and mobile devices. They can be viewed [here](libraries/wireframes/).

[Back to TOC](#table-of-contents)

### Features

#### Existing features

##### For all users 

* A responsive fixed navbar displaying the brand logo and the ability to navigate to the main dictionary page, log into your account or register
    * The navbar is accessible via a hamburger menu in the top left of the viewport on mobile and tablet devices
* A button that users can click to generate a pop-up displaying the information about the app and how to use it effectively
* A search bar in which users can input text and find results containing words matching one of the search terms instead of the whole
dictionary
    * A not found page that renders if no data matches the user's search query with a button to take the user directly back to the homepage
* A call to action button on the home page that takes the user directly to the search bar
* A reset button beside the search bar that enables users to clear any text they have entered in case of typing errors
* A snapshot of the most popular dictionary entries at any time, sorted by their score, starting with the highest
    * An entry must have a score of at least 5 to qualify as a popular term
    * If there are fewer than 3 terms with a qualifying score, the list disappears entirely
    * No more than 5 entries can appear in this section. If there are more than 5 entries that meet the qualifying score, those with the
    lowest scores will disappear from the list
* The full dictionary that lists each entry in alphabetical order by term name
* A score associated with each entry based on the number of upvotes and downvotes it has received
    * If a term's score reaches 20, the number is shown in green, indicating an especially strong score
    * If a term's score falls below 0, the number is shown in red, indicating a weak score
    * If a term's score falls below -5, the entry is hidden due to concerns the information is not reliable or accurate. Only administrators
    can continue to see entries whose score are below -5
* A responsive footer containing Fitipedia's logo, contact information and social media links
* A contact page displaying Fitipedia's contact details and a Google Maps widget using the Google Maps API to show the user the company's physical location
* A return to top button consisting of a Font Awesome icon of a finger pointing upwards that appears when the user scrolls down
    * When the user clicks this button, a scroll behaviour style rule implemented using CSS makes the page scroll smoothly back to the top (N.B. this does not happen on Safari, see the [Browser Compatibility](TESTING.md#browser-compatibility) section of the TESTING.md file for more information.
* A 404 page that is rendered if the user enters an invalid URL
* An automatic redirect to the login page if the user attempts to access a URL that only logged in users can access, with a flash message indicating that they must log in first

##### For registered users

* A responsive, fixed navbar that enables users to view their profile, add a new entry to the dictionary or log out
* A section on the homepage that shows the last 5 entries of the user logged in, sorted by date from most recent
    * The user can edit or delete entries in this section instead of having to navigate to the dictionary page
    * Entries that are hidden due to having a low score still appear in this section, as they are unique to the user and cannot be seen by anybody else
    * Each entry shows the date and time of its last update. If the entry hasn't been updated since its creation, the time of its creation will show. If the user updates an entry, this will count as the most recent entry and move to the top of the section
    * If a user deletes an entry from their most recent 5 entries, it will disappear from the section and the previously 6th most recent entry appears at the bottom of the section in its place
    * If a user has made fewer than 5 entries, the section is shortened to reflect the number of user entries
    * If the user has not yet made any entries, text will appear informing the user that they haven't yet made any contributions, with a call to action button below inviting the user to add their first
    * If the user hsa made entries, the text will state how many contributions the user has made. The number changes depending on the user adding further entries or deleting entries. The text on the button below also changes to 'Add Another'
* A dictionary in full where the user can view terms created by themselves and others
    * The user will see edit and delete buttons below their entries, and upvote and downvote buttons below those of other users
* Responsive forms for users to add new entries and edit existing entries
    * Each form has minlength and pattern attributes so that users must input genuine text
    * A JavaScript function exists to prevent the user typing consecutive spaces so that a string of whitespace cannot be submitted
* An automatic redirect to the respective form if users attempt to add or change an entry to a word that already exists in the dictionary
* A modal pop-up box that asks the user to confirm whether they wish to delete a term with a cancel button in case the user mistakenly selected this option
* A profile page containing the user's username, total number of contributions and all entries contributed by the user in alphabetical order
    * If the user has made 20 or more contributions, they will see the following text: "Congratulations! You have reached legend status!"
    * If the user has made fewer than 20 contributions, the text will tell them how manw more they need to make to achieve legend status
* A delete account function that enables the user to delete their account if they wish
* A resonsive form for users to update their profile details with an automatic redirect back to it if the user submits inputted usernames or e-mail addresses that are already occupied by another user
* An automatic redirect to the homepage if the user attempts to access a URL that is unique to another user, or that only an administrator can access, with a flash message indicating that the user is not authorised to perform such an action

##### For administrators (superusers)

* A responsive, fixed navbar where administrators can perform any standard user actions and access a manage users page to see a list of existing users
* The ability to edit or delete any entry in the dictionary, even if created by another user
* The ability to see entries with a score of -5 (that are therefore hidden to other users) in the dictionary as normal
* A list of existing users, sorted by username in alphabetical order, with each user's username, e-mail address and a button to delete their account
    * An administrator should only delete another user's account in exceptional circumstances, such as in appropriate use of the site or a user's request to have their account deleted
* A button to add a new user to the databse and a responsive form for the administrator to input the new user's data
    * An administrator should only add a new user in exceptional circumstances, such as multiple failed attempts by a user to register an account and an inability to identify the cause of this problem
    * It is recommended that a user registered in these circumstances changes their password immediately after first logging in
    * Like with other forms, the administrator is redirected back to it if they submit a username or e-mail address already occupied by an existing user
* A modal pop-up box that asks the administrator to confirm whether they wish to delete a user's account with a cancel button in case they mistakenly selected this option

#### Features left to implement

As the database expands, I would like to implement the following features:

* Filtering dictionary terms by first letter (0-9 + A-Z)
    * Each letter would be a clickable link that calls a backend function to limit the users query to data whose value string starts with that particular character (unfortunately there was not sufficient time remaining to implement this to an acceptable standard at this stage of the project)
* Limiting users to just one upvote or downvote for each term
* Pagination of search results, limiting the results to a certain number per page (e.g. 20) and the option for the user to navigate to a certain page number
    * If the database is especially large, the user could have the option to choose between how many search results they would like to have per page (e.g. 20, 50, 100)
* A dropdown of search suggestions based on the user's input (e.g. if the user inputted 'car' the word 'cardio' would be suggested)
* If the site gains a large number of users, the ability for the administrator to filter results on the Manage Users page by the first letter of the user's username
* The ability to publicly view other user's profiles and their contribution history
    * Other users may wish to hide potentially sensitive data such as e-mail addresses from other users, so they could have the option to not allow this to be seen by others
* A private messaging function that would enable users to communicate with each other on the app itself
* A tiered user status system based on user engagement i.e. number of entries made
    * Currently a user needs 20 entries to reach legend status, they could reach another milestone after 50 entries
* A user points system based on the number of upvotes their entries have received to indicate reliability and trustworthiness
* E-mail confirmation for new users when creating an account, including an activation link
* A reset password function that enables a user to reset their password via e-mail in the event they forget their password
* For security reasons, accounts created by admins for other users are forced to change their password when logging in for the first time
* Administrators are notified if a term's score drops below -5 and are forced to review it, removing it from the dictionary if necessary

[Back to TOC](#table-of-contents)

### Technologies Used

The application uses the following core programming languages:

**Backend**
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

**Frontend**
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

The following frameworks, libraries and packages were also used:

**Databases**
* [MongoDB Atlas](https://mongodb.com): the app's database, to store, retrieve and query data

**Python dependencies**
* [PyMongo](https://pymongo.readthedocs.io/en/stable/): a Python distribution with tools for interaction with MongoDB
* [dnspython](https://www.dnspython.org/): a DNS toolkit for Python
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/): a WSGI web application library that handles HTTP requests
* [Flask](https://flask.palletsprojects.com/en/1.1.x/): a Python web app framework
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/): a templating engine for Python
* [Datetime](https://docs.python.org/3/library/datetime.html): to record the exact date and time of a record being created or updated

**Frontend libraries and frameworks**
* [jQuery](https://jquery.com): to simplify DOM manipulation and event-handling
* [Materialize CSS](https://materializecss.com): for site responsiveness and clean, intuitive layout
* [Google Fonts](https://fonts.google.com/): to import font families to be used for the application's front end
* [Font Awesome](https://fontawesome.com/): for responsive icons that let users initiate actions 
* [Favicon](https://favicon.io/): to include a favicon within the browser tab
* [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview): to render a Google Maps widget on the website
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools): to test responsiveness, inspect the role of each element and 
class and experiment in real time with new style rules and their effect on the site's layout and structure

**Software hosting and cloud platforms**
* [Heroku](https://www.heroku.com/): for the project's live deployment
* [GitHub](https://github.com/lbacon17/fitipedia): to create a repository for the project and link it to Heroku to be deployed
* [Gitpod](https://gitpod.io): to manage the project's necessary files and write the code for the project

**Design tools**
* [Am I responsive](http://ami.responsivedesign.is/): for testing and screenshots of the website's responsive design

**Validators**
* [PEP8](http://pep8online.com/): Python
* [JSHint](https://jshint.com/): JavaScript
* [Jigsaw](https://jigsaw.w3.org/): CSS
* [W3C](https://validator.w3.org/): HTML

[Back to TOC](#table-of-contents)

### Data Structure

The project uses MongoDB Atlas as its database to store data. This project uses two collections:

1. Terms: records of the words that appear in the dictionary. It consists of the following keys:
    * _id (ObjectId)
    * term_name
    * term_definition
    * created_by
    * created_on
    * contribution_value (this number is always 1 so that each term created by a user adds 1 to their total number of entries made)
    * score (calculated by subtracting the number of downvotes from the number of upvotes. An upvote adds 1 to the score, a downvote takes
    1 off the score)

1. Users: records of the users that have registered on the website. It consists of the following keys:
    * _id (ObjectId)
    * username
    * password (which is hashed into a random string of letters and numbers for added security)
    * email_address
    * is_superuser (a boolean field that can be used to grant administrators certain site privileges by being set to 'True')

[Back to TOC](#table-of-contents)

### Testing

To read about the testing process, please see the separate [TESTING.md](TESTING.md) file.

[Back to TOC](#table-of-contents)

### Deployment

#### To deploy the app to Heroku using Gitpod

1. Install Flask via the Gitpod terminal with the command: ```pip3 install flask```

1. Import Flask in the app.py file: ```from flask import Flask```

1. Install the Heroku toolbelt via the terminal with the command: ```npm install -g heroku```

1. Once installed, log in with your heroku login details using the command: ```heroku login -i```

1. We then need to tell Heroku which libraries and frameworks (dependencies) are needed for the application to run. A list of these are stored in the requirements.txt file. Redirect the dependencies lists to the requirements file with the command: ```pip3 freeze --local > requirements.txt```

1. Next, we need to create a Procfile that Heroku looks for to know that the app runs on Python. Create the Procfile with the command:
```echo web: python app.py > Procfile```
    * There may be a blank line at the end of the Procfile. Delete this line as it can cause Heroku problems in locating the file.

1. Log into your Heroku account and select 'Create a new app' from the dashboard. Make sure the app's name is all in lowercase and has no spaces (use dashes ('-') to link words instead). Select 'United States' or 'Europe', depending on the region in which you are based.
    * **You may have created the app in Heroku before starting the deployment, in which case you can skip this step and go straight to the step below.**

1. From your Heroku dashboard, select the app to be deployed. Click the 'Deploy' tab and select 'GitHub' as the deployment method.

1. Connect the GitHub account that has created this app's repository and search for the repository's name. Click 'Connect' once this is found.
    * Your GitHub username should already be displayed as you should be prompted to configure GitHub integration if you have not yet done so when opting to deploy using GitHub.

1. Go to the Settings tab, scroll down and click on the 'Reveal Config Vars' button. Add the environment key-value pairs from the env.py file, ensuring to remove quotation marks when pasting them into Heroku.
    * When using MongoDB, the environment variables should be as follows:
        ```
        IP: 0.0.0.0
        PORT: 5000
        SECRET_KEY: [secret_key]
        MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>.ckdkb.mongodb.net/<database_name>?retryWrites=true&w=majority
        MONGO_DBNAME: [database_name]
        ```
    * A secret key is a randomly generated string of letters and numbers. You can obtain one from [randomkeygen.com](https://randomkeygen.com/).
    * In the MONGO_URI variable, the data in angle brackets (<>), including the brackets themselves, will need to be replaced with your unique MongoDB username, password, cluster name and database name
        * To find your Mongo URI, log into your MongoDB account, select 'Clusters' and click the 'Connect' button in the sandbox. From there, select the 'Connect your appliation' option, select 'Python' as the driver and '3.6 or later' as the version. Your MongoDB URI should be displaying in the box below.
        * You should not use any non-alphanumeric characters in your MongoDB password as you will not then be able to connect the database using Python.

1. After all Config Vars have been added, go back to the Gitpod terminal and add the requirements.txt and Procfiles: ```git add requirements.txt Procfile```

1. Commit these files and push the changes to Github.

1. If you haven't done so already, create a .gitignore file in Gitpod with ```touch .gitignore``` and add ```env.py``` and ```__pycache__/``` so that these are not included in any commits. **Do not push the `env.py` file to GitHub as your secret key and MongoDB login information will be publicly available.**

1. The app is now ready to be deployed to Heroku. Go back to the Deploy tab, scroll down to the 'Automatic deploy' section and click 'Enable 
automatic deploys'. This updates the app on the Heroku platform whenever changes are pushed to Github and saves us from having to do it manually each time.

1. In the 'Manual deploy' section below, select the branch of the repository to be deployed. Once selected, click 'Deploy branch'.

1. The deployment may take a few minutes. Once complete, the message: "Your app was successfully deployed" will appear. Click on the 'View' 
button below the message to view the deployed app in a new browser tab and ensure everything is working as it should.

1. For the app to function properly, you will need to install certain dependencies via Gitpod. The exact dependencies can vary according to the nature of the app. To install them, use the command: ```pip3 install [name of dependency]```. For more information on dependencies, see the [Technologies Used](#technologies-used) section.

#### To run the app locally

1. At the top of the project's repository just below the menu, click on the 'Code' dropdown button.

1. In the 'Clone' section, make sure that the 'HTTPS' heading is underlined and copy the URL inside the box.

1. Open the Terminal on your device and type `pwd` to show your current working directory (this is where the project folder will be imported).

1. Type 'git clone' and paste the URL copied from GitHub (note there must be a space between 'clone' and the URL) and press enter.

1. Check the directory printed in step 3 to make sure the project folder exists there.

1. To run the app locally, you will need to install all the dependencies included in the [requirements.txt](requirements.txt) file. Type the command `pip3 install -r requirements.txt` and press enter.
    * You may need to add the filepath before the requirements.txt file if the repository was not cloned into your desktop. For example, if it were in your Documents folder, the command would be `pip3 install -r /Users/MyName/Documents/requirements.txt`

1. Create the `env.py` file with the command `touch (..filepath../)env.py` and add the following content:
        
    ```
    import os
    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "[secret_key]")
    os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>.ckdkb.mongodb.net/<database_name>?retryWrites=true&w=majority")
    os.environ.setdefault("MONGO_DBNAME", "[database_name]")
    ```
    
    You may also need to add:

        ```
        os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<cluster_name>.ckdkb.mongodb.net/<database_name>?retryWrites=true&w=majority"
        ```

1. To run locally, type the command `python3 (..filepath../)app.py` and press enter.
    * The Terminal may throw the following error: *TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'*. In this case, remove the int() method from the last code block of the `app.py` file so that it reads:
        ```
        if __name__ == "__main__":
            app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"), debug=False)
        ```
    * The Terminal should read "running on http://127.0.0.1:5000". Paste this URL into the browser to acccess the app.

[Back to TOC](#table-of-contents)

### Credits and Acknowledgements

#### Content

The website uses a number of components from Materialize CSS, including the navbar, card panels, buttons and colour classes. Much of the
Python views are based on material learned in the Data Centric Development module by the Code Institute, in particular the 
[Task Manager](https://github.com/Code-Institute-Solutions/TaskManagerAuth) mini-project delivered by
[Tim Nelson](https://github.com/TravelTimN).

Some ideas are based on recommendations by [Stack Overflow](https://stackoverflow.com/). I'd most like to highlight the solution
[to check the validity of an ObjectId](https://stackoverflow.com/questions/28774526/how-to-check-that-mongo-objectid-is-valid-in-python),
which helped with rendering a custom 404 page when an invalid ID was passed.

The dictionary entries and definitions are from a book that I wrote on fitness last year called 'Gym and Weight Training Basics A-Z'. This is
an e-book that gives a comprehensive breakdown of jargon in the fitness industry and provides the raw data for this project. The book can be
purchased and downloaded [here](https://gum.co/mzDyj).

#### Special thanks

I would like to give special thanks to my mentor [Precious Ijege](https://ng.linkedin.com/in/precious-ijege-908a00168) for highlighting
flaws with the app in the testing phase, giving clear, actionable advice on how to rectify them and his tireless support to help improve the project and make it realise its full potential. Thanks also to the Code Institute's Tutors and [Slack](https://slack.com) channel who dealt with my queries at short notice and helped me fix some mistifying bugs in the code.

Thank you for reading.

I hope you enjoy using Fitipedia.

[Back to TOC](#table-of-contents)