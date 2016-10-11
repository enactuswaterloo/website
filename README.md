# Enactus Waterloo

Maintained by: Bilal Akhtar, Mohamed Moussa, Bo Peng

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Pip](https://pip.pypa.io/en/stable/index.html) (`python get-pip.py`)

## Installation

Type the following commands into your terminal to get set up. When installing the Django stuff, it may require admin access, so just type `sudo` before the commands.

#### Clone & Install
* Clone the Enactus Waterloo respository: `git clone https://github.com/enactuswaterloo/website.git`
* Go into the directory: `cd website`
* Copy enactuswaterloo/local_settings.py.sample to enactuswaterloo/local_settings.py
* (Optional but highly recommended) Install and activate virtualenv
  1. `pip install virtualenv` (you might have to prefix this command with sudo)
  1. `virtualenv env`
  1. `source env/bin/activate` (you will have to run this command from the folder every time you run the server)
* Install Django: `pip install Django`
* Install Bootstrap, CKEditor, TinyMCE & Pillow:
  1. `pip install django-bootstrap3`
  1. `pip install django-ckeditor`
  1. `pip install django-tinymce`
  1. `pip install Pillow`
* Migrate: `python manage.py migrate`

## Running

#### Create admin
* Run this command and follow the prompts: `python manage.py createsuperuser`

#### Running the server
* If you use virtualenv: `source env/bin/activate`
* `python manage.py runserver`
* Website will be launched at http://localhost:8000/

## Developing and Releasing
Read this article for git branching model: http://nvie.com/posts/a-successful-git-branching-model/

1. Pull the latest changes from the master branch
1. Create a new branch for your feature off of develop
1. Submit a pull request from your new branch to develop
1. Once your pull request is reviewed, merge it to develop and delete the branch
