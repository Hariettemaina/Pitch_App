## PROJECT  NAME 
 - PITCH-APP 

## AUTHOR 
 - Hariette Maina

 ## DESCRIPTION 
 - This is a Python-Flask Application that allows users to create one minute pitch. You only have 60 seconds to impress someone. 1 minute can make or break you.
- The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

 ## BDD(Behaviour Driven Development)

  

 # Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg lauradoe``|
| Password  | Account password, ``eg laura23``|

# Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg lauradoe``|
| Email  | User email, ``eg jjune@testmail.com``|
| Password  | Account password, ``eg 12345``|
| Confirm Password  | Account password, ``eg laura23``|

# Pitches inputs

| Inputs | Description  |
|---|---|
|  Heading | Pitch description eg; ``pickup lines``  |
|  Pitch text| The actual pitch body|
| Comment| A comment on the pitch|

## User Story

- Users can see the pitches other people have posted.

- Users can vote on the pitch they liked and give it a downvote or upvote.

- Users can sign in to leave a comment.

- Users can register on the website.

- Users can view the pitches they have created in their profile page..

- Users can comment on the different pitches and leave feedback. 

- Users can submit a pitch in any category. 

- Users can view the different categories. 

## Technologies used
* Python3
* Flask
* Html5
* Css3
* Bootstrap5


# Prerequisites

To work with ONE MINUTE PITCH App you need to have some few prerequisites.

- Python3.8

- pipenv

- Flask 

- Code/text editor

- Terminal

## Installations

The following command installs all the application requirements
>``pipenv lock -r > requirements.txt``

## Setup
 - Run "https://github.com/Hariettemaina/Pitch_App.git"
 

 - or download the zip file from github.

- After extracting the files, 

 1. Navigate to the project folder
 >`` cd Pitch-App.`` 

 2. Creating a virtual environment
 >``install pipenv.``

 3. Activating the virtual environment
 >``pipenv shell``

4. Running the application
>``python3 manage.py runserver``

5. Running tests

 > ``python3 manage.py test.``


**Adding dependencies**
- Install Flask
```bash
(virtual) $ pipenv install flask
```
- Install Bootstrap
```bash
(virtual) $ pipenv install flask-bootstrap
```
- Install Flask Script
```bash
(virtual) $ pipenv install flask-script
```
- Install Flask sqlalchemy
```bash
(virtual) $ pipenv install flask-sqlalchemy
```
- Install Flask psycopg2
```bash
(virtual) $ pipenv install psycopg2
```
- Install Flask psycopg2-binary
```bash
(virtual) $ pipenv install psycopg2-binary
```
- Install Flask gunicorn
```bash
(virtual) $ pipenv install gunicorn
```
- Install Flask flask-login
```bash
(virtual) $ pipenv install flask-login
```
- Install Flask flask-uploads
```bash
(virtual) $ pipenv flask-uploads
```
- Install Flask werkzeug
```bash
(virtual) $ pipenv install werkzeug==0.16.0
```
- Install Flask markupsafe
```bash
(virtual) $ pipenv install markupsafe==2.0.1
```
- Install Flask Flask Mail
```bash
(virtual) $ pipenv install Flask-Mail
```
- Install Flask Flask Migrate
```bash
(virtual) $ pipenv install Flask-Migrate ==2.7.0
```
- Install Flask Flask wtf
```bash
(virtual) $ pipenv install flask-wtf
```
- Install Flask Email validator
```bash
(virtual) $ pipenv install wtforms[email]
```
- Install Flask Dotenv
```bash
(virtual) $ pipenv install python-dotenv
```

**Migrate data** 
- To migrate data
```bash
(virtual) $python3 manage.py db init
```
```bash
(virtual) $python3 manage.py db migrate -m "Initial Migration"
```
```bash
(virtual) $python3 manage.py db upgrade
```


##  Development

### Want to contribute? Great!
# To fix a bug or enhance an existing module, follow these steps:
* Fork the repo
* Create a new branch ('git checkout -b improve-feature')
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes ('git commit -am 'Improve feature')
* Push to the branch ('git push origin improve-feature')
* Create a Pull Request

- https://pitchmaneno.herokuapp.com/


## Contacts 
 **hariettemaina@gmail.com**


## License
- MIT License Copyright (c) 2022 Faith Mwangi