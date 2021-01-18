# **[Fitipedia!](https://fitipedia.herokuapp.com)**

## The free online fitness dictionary

![](libraries/readme_images/site_responsiveness.png)


404 error, change return argument from username=username to username=session["user"]

bugfix upvoting/downvoting - redirect rather than render template

first term in list showing up in confirmation box rather than target term. Fixed by giving each modal div a unique id of id="{{ term._id }}" and setting href accordingly - href="#{{ term._id }}"

{% if session.user and session.user|lower != term.created_by|lower or session.user|lower == "admin"|lower %}
prevents users voting on their own content unless they are an admin.

CRUD colour code: C - green, R - teal, U - blue, D - red

Uncompliant lines were all if statements containing the or operator that meant the app would not run if the line was broken due to a syntax error.

`if session["user"] == term_creator or session["user"] == is_superuser:`

`if request.form.get("term_name").capitalize().strip() == current_term:`
