## About Me

Hi, I'm Mulajim Ali, a passionate **Full-Stack Developer** specializing in **Python (Flask/Django)**, **React.js**, and modern web development technologies.  
This project reflects my love for building simple, scalable, and efficient applications.  
Feel free to explore, fork, or contribute!

### Flask To-Do Application
A simple, lightweight, and efficient To-Do List Web Application built with Flask.
Manage your daily tasks easily — create, update, delete, and mark them as complete.

### Features
* Add new tasks
* Edit existing tasks
* Mark tasks as complete/incomplete
* Delete tasks
* Store tasks persistently (using SQLite)
* Error handling and validations

### Tech Stack
* **Backend:** Flask (Python micro-framework)
* **Database:** SQLite3

### Clone the Repository
    $ git clone https://github.com/mulajimaliofficial/flask-todo-app.git
    $ cd flask-todo-app

### Folder Structure
    flask-todo-app/
    │
    ├── app/
    │   └── __init__.py
    │   └── controllers.py
    │   └── forms.py
    │   └── models.py
    │   └── views.py
    │
    ├── instance/
    |   └── site.db
    │
    ├── migrations/
    │
    ├── run.py
    ├── .gitignore
    ├── requirements.txt
    ├── README.md


### Installation of virtualenv on windows
    $ pip install virtualenv

### Step to create virtualenv on windows
    $ python -m virtualenv env

### Step to activate virtualenv on windows
    $ source env/Scripts/activate

### step to install the requirements in virtualenv 
    $ pip install -r requirements.txt

### step to upgrade pip on windows
    $ python.exe -m pip install --upgrade pip


### steps to Database migrations
###### 1. Initialize migration
    $ flask db init

###### 2. Generate migration Scripts
    $ flask db migrate -m "Intial migration"

###### 3. Apply migrations
    $ flask db upgrade

### Run the application
    $ python run.py


### Below i am sharing the postman test image
****To register a user** <br /> <br /> ![register image](/media/register.png)

**To login user with their credentials** <br /> <br />![login image](/media/login.png)

**To refresh the user token** <br /> <br /> ![refresh image](/media/refresh.png)

**To logout the user** <br /> <br /> ![logout image](/media/logout.jpg)

**To get the todos** <br /> <br /> ![todos get image](/media/todo.png)

**To create the todos** <br /> <br /> ![todos create image](/media/create.png)

**To update the todos** <br /> <br /> ![todos update image](/media/update.png)

**To delete the todos** <br /> <br /> ![todos delete image](/media/delete.png)

**token in headers** <br /> <br /> ![token in header](/media/header.png)
