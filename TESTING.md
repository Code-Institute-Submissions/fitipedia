# **[Fitipedia!](https://fitipedia.herokuapp.com)**

# Testing

This file documents the testing process of the project.

## Table of contents

* [Validation](#validation)
* [Responsiveness](#responsiveness)
* [Browser Compatibility](#browser-compatibility)
* [Testing User Stories](#testing-user-stories)
* [Issues and Bugs](#issues-and-bugs)

### Validation

[Back to TOC](#table-of-contents)

### Responsiveness

[Back to TOC](#table-of-contents)

### Browser Compatibility

[Back to TOC](#table-of-contents)

### Testing User Stories

[Back to TOC](#table-of-contents)

### Issues and Bugs

#### Bugs during testing


#### Bugs still to be fixed

[Back to TOC](#table-of-contents)

404 error, change return argument from username=username to username=session["user"]

bugfix upvoting/downvoting - redirect rather than render template

first term in list showing up in confirmation box rather than target term. Fixed by giving each modal div a unique id of id="{{ term._id }}" and setting href accordingly - href="#{{ term._id }}"

{% if session.user and session.user|lower != term.created_by|lower or session.user|lower == "admin"|lower %}
prevents users voting on their own content unless they are an admin.


`if session["user"] == term_creator or session["user"] == is_superuser:`

`if request.form.get("term_name").capitalize().strip() == current_term:`

[Back to README.md](README.md)