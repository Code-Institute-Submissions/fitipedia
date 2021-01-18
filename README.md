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
click on the 'Click Here' text before browsing

The user can intuitively perform
all CRUD actions 
Each button is given a colour
depending on which part of the CRUD functionality it represents.

* **Create (C)** all buttons that add data to the website are **<span style="color:green">green</span>**
* **Read (R)** all buttons that locate and read data on the website are **<span style="color:teal">teal</span>**
* **Update (U)** all buttons that edit and update data on the website are **<span style="color:aqua">blue</span>**
* **Delete (D)** all buttons that remove data from the website are **<span style="color:red">red</span>**

The exception is the 'Search Dictionary' button on the home page, which serves as the app's main call to action button.

Colour coded by nature of data manipulation

#### User Stories

[Back to top](#table-of-contents)

### Features


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

[Back to top](#table-of-contents)

### Technologies Used

p

[Back to top](#table-of-contents)

### Data Structure

[Back to top](#table-of-contents)

### Testing

[Back to top](#table-of-contents)

### Deployment

[Back to top](#table-of-contents)

### Credits

[Back to top](#table-of-contents)


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