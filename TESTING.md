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

The code was passed through the [W3C](https://validator.w3.org/) validator. A number of unavoidable errors were found relating to Jinja templating characters, but there were no errors in the HTML itself.

![W3C Validation](/libraries/code_validation/html_validation_w3c.png)

![W3C Validation base.html errors](/libraries/code_validation/html_validation_w3c_base_template.png)

[Back to TOC](#table-of-contents)

### Responsiveness

[Back to TOC](#table-of-contents)

### Browser Compatibility

The application was tested in the following browsers:

* Google Chrome
* Mozilla Firefox
* Brave Browser
* Opera
* Safari

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