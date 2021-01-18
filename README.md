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
* [Credits](#credits)

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

The exception is the 'Search Dictionary' button on the home page, which serves as the app's main call to action button.

The upvote and downvote buttons and the icons that they display also make their purpose clear to the user, as the colour green is
associated with approval, while red is associated with disapproval. Each term's score is shown in larger text so that the user is left in 
no doubt.

All delete actions initiated by the user bring up a confirmation box asking the user if they're sure they want to delete something in the
event they clicked the button mistakenly. The user can select cancel, which has the more neutral colour of grey, if they do not wish to
delete a piece of data.

The following fonts are used:

* Commissioner for main body of content, which gives the site a more informal but still informative feel
* Big Shoulders Inline Text for the jumbotron header, which gives a robust look, more associated with fitness
* Bodoni Moda for the Fitipedia brand logo
* Yusei Magic for the site information modal trigger, as it clearly stands out from the other text and is more likely to prompt a click
from the user

The navbar is fixed as content on pages, particularly the dictionary page, can be very long.

#### User Stories

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

#### Wireframes

I used [Wireframe.cc](https://wireframe.cc) to design wireframes for desktop/laptop and mobile devices. They can be viewed [here](libraries/wireframes/).

[Back to TOC](#table-of-contents)

### Features

#### Existing features

#### Features left to implement

* Pagination
* Limiting search results per page
* Filtering by first letter (0-9 + A-Z), each letter shown as a clickable link that would then filter
* Search suggestions based on user input (e.g. car --> cardio)
* One upvote/downvote per user per term
* Ability to view other user's profiles and their contribution history
* Ability to private message other users
* User points and tiered system based on engagement (number of entries made and upvotes received in their history)
* Ability to reset password if user forgets
* For security reasons, accounts created by admins for other users are forced to reset passwords when logging in for the first time
* E-mail confirmation when creating accounts, including activation link
* Automatic notifications and review requests for administrators if a term's score reaches -5
* New users would have their first 5 posts reviewed and approved by an admin

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
* [dnspython](https://dnspython.org): a DNS toolkit for Python
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
* [Am I responsive](https://ami.responsivedesign.is): for testing and screenshots of the website's responsive design

**Validators**
* [PEP8](http://pep8online.com/): Python
* [JSHint](https://jshint.com/): JavaScript
* [Jigsaw](https://jigsaw.w3.org/): CSS
* [W3C](https://validator.w3.org/): HTML

[Back to TOC](#table-of-contents)

### Data Structure

[Back to TOC](#table-of-contents)

### Testing

[Back to TOC](#table-of-contents)

### Deployment

[Back to TOC](#table-of-contents)

### Credits

[Back to TOC](#table-of-contents)


404 error, change return argument from username=username to username=session["user"]

bugfix upvoting/downvoting - redirect rather than render template

first term in list showing up in confirmation box rather than target term. Fixed by giving each modal div a unique id of id="{{ term._id }}" and setting href accordingly - href="#{{ term._id }}"

{% if session.user and session.user|lower != term.created_by|lower or session.user|lower == "admin"|lower %}
prevents users voting on their own content unless they are an admin.

CRUD colour code: C - green, R - teal, U - blue, D - red

Uncompliant lines were all if statements containing the or operator that meant the app would not run if the line was broken due to a syntax error.

`if session["user"] == term_creator or session["user"] == is_superuser:`

`if request.form.get("term_name").capitalize().strip() == current_term:`

Credit self in Gumroad