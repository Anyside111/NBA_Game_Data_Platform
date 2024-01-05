[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/b8Jjz3kB)

# OKC Technical Project Deliverable

### 1. Backend Engineering

* Architect and implement a normalized PostgreSQL database to store the data provided in `backend/raw_data`. All information from the original data should be accessible via the database.

* Write a brief description of your database architecture (<250 words). Feel free to provide a visual representation as an aide. Submit relevant responses in the `written_responses` folder provided.

* In the programming language of your choice, write a process to load the dataset into your PostgreSQL database. Ensure that this process can run repeatedly without duplicating or obscuring references in the database. Include the source code of your process in the `backend/scripts` folder. Note: You can feel free to utilize the power of Django models and migrations to achieve this step.

* After loading the data, export the state of your database using `pg_dump -U okcapplicant okc > dbexport.pgsql`. Include `dbexport.psql` in the `backend/scripts` folder.

* The skeleton of an API View `PlayerSummary` can be found in `backend/app/views/players.py`. Implement this API to return a player summary that mimics the structure of `backend/app/views/sample_response/sample_response.json`. Feel free to import additional modules/libraries in order to do this, but ensure that the `backend/requirements.txt` is updated accordingly. Viewing http://localhost:4200/player-summary-api allows you to see the output of your API, given the playerID parameter provided in the user input.

### 2. Frontend Engineering

* The `player-summary` component, which is viewable at http://localhost:4200/player-summary, makes a call to an API endpoint at `/api/v1/playerSummary/{playerID}` that returns player summary data. One component of the player summary data are the player's shots in each game, note that:

   * The shot's x and y coordinates are provided and are measured in feet
   * The location of each shot is relative to the center of the basket, per `court_diagram.jpg` in this repository

* Within the `player-summary` component found in `frontend/src/app/player-summary/`, create an interface that describes the player summary data returned from the API.

* Feel free to import additional modules of your choice, and design the interface however you wish. Just make sure that the `package.json` and `package-lock.json` are updated accordingly.


# Application Setup
In order to complete the Backend Engineering or Frontend Engineering deliverables, you will need to do all of the following setup items. Please follow the instructions below, from top to bottom sequentially, to ensure that you are set up to run the app. The app is run on an Angular frontend, Django backend, and a PostgreSQL database.

## Set up database
1. Download and install PostgreSQL from https://www.postgresql.org/download/
2. Ensure PostgreSQL is running, and in a terminal run
    ```
    createuser okcapplicant --createdb;
    createdb okc;
    ```
3. connect to the okc database to grant permissions `psql okc`
    ```
    create schema app;
    alter user okcapplicant with password 'thunder';
    grant all on schema app to okcapplicant;
    ```


## Backend

### 1. Install pyenv and virtualenv

Read about pyenv here https://github.com/pyenv/pyenv as well as info on how to install it.
You may also need to install virtualenv in order to complete step 2.

### 2. Installing Prerequisites
The steps below attempt to install Python version 3.10.1 within your pyenv environment. If you computer is unable to install this particular version, you can feel free to use a version that works for you, but note that you may also be required to update existing parts of the codebase to make it compatible with your installed version.
```
cd root/of/project
pyenv install 3.10.1
pyenv virtualenv 3.10.1 okc
pyenv local okc
eval "$(pyenv init -)" (may or may not be necessary)
pip install -r backend/requirements.txt
```

### 3. Starting the Backend
Start the backend by running the following commands
```
cd /path/to/project/backend
python manage.py runserver
```
The backend should run on http://localhost:8000/.


## Frontend

### 1. Installing Prerequisites
Install Node.js (16.x.x), then run the following commands
```
cd /path/to/project/frontend
# Install Angular-Cli
npm install -g @angular/cli@12.1.0 typescript@4.6.4 --force
# Install dependencies
npm install --force
```

### 2. Starting the Frontend
Start the frontend by running the following commands
```
cd /path/to/project/frontend
npm start
```
The frontend should run on http://localhost:4200/. Visit this address to see the app in your browser.


# SUBMISSION.md
Please fill out the SUBMISSION.md file to ensure we have your name attached to the project.


# Questions?

Email datasolutions@okcthunder.com
