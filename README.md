# CSEC: Web Division

## Requirements
 * python3
 * pip
 * python3-virtualenv (VirtualEnv)

## Set up virtual environment
Set up your working directory and make sure you are cd into it.
```
python3 -m venv flask
source flask/bin/activate
pip install -r requirements.txt
```

## Set up the database
Run the following the commands to initialize our database
```
python3 ./db_create.py
python3 ./db_migrate.py
```

## Run the app
Make sure you are in the working directory and then do the following:
```
python3 ./run.py
```

The website will now be running at: http://localhost:5000
