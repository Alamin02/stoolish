# Stoolish
This is a open source django project. 
Any user can register and give their profile link to recieve anonym message from friends or contacts.
This project is basically django coded form of once popular STULISH app.

A [Live Demo](https://stoolish.herokuapp.com) of this project is also available.

## How to install
First clone the repository and navigate to the cloned folder.

Make a virtual environment. If you are not familiar then you can follow these steps:

Install `virtualenv` with the command\
`pip install virtualenv`

Make a virtual enviroment using `virtualenv` using the command\
`virtualenv venv`

activate the virtual environment using\
`source venv/bin/activate`

Now that you have your virtual enviroment activated, install all the dependencies using\
`pip install requirements.txt`

Then make migrations\
`python manage.py makemigrations`

Now you are ready to go. Start the project with\
`python manage.py runserver`

Now you are ready to go! Enjoy!

If you want admin access you can create admin account using the following command\
`python manage.py createsuperuser`

Now you will see a prompt. fill up the informations and boom! You are an admin now!
Cheers!
