# Movie Shelf - A Simple Movie Databasing Application

Basic steps to import flask and spool up a local hosted environment. 

Full CRUD functionality

### INSTALLING FLASK AND DEPENDENCIES

cd to project directory
```
$ pipenv shell
$ pipenv install flask
$ pipenv install Flask-SQLAlchemy
$ pipenv install Jinja2
$ pipenv install Flask-Table
$ pipenv install WTForms
```

### USING CURRENT DATABASE FILE

In the Project Directory, start a python REPL:
```
$ >>> from app import db
```

### CREATE NEW DATABASE FILE

In the Project Directory, start a python REPL:
```
$ python --three
$ >>> from app import db
$ >>> db.create_all()
$ >>> import db_creator
$ >>> import db_setup
```

### SPOOLING UP LOCAL SERVER

Exit Repl and while in the pipenv shell:
```
$ python main.py
```

Application will be running on localhost:5001
