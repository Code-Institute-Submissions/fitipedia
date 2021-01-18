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

o

[Back to top](#table-of-contents)

### Features

a

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

Future functionality: search suggestions based on user input, one upvote/downvote per user per term, ability to view user's profiles and their history, 'points' and tiered system given to users based on number of contributions made and upvotes received, ability to reset password, accounts created by administrators for other users are forced to reset passwords when first logging in, e-mail confirmation when creating accounts, including link to activate, filtering terms by first letter with each letter of the alphabet shown as a clickable link on the dict page that will filter terms with that first letter (first letter would act as categories, each one would have to be added to the database, just ran out of time to implement this), automatic review notification for admins if term score reaches -5

Credit self in Gumroad