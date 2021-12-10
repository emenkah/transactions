# Transaction Records System

This project reads in the contents of a JSON-file as a background process into a database. 
Date of birth values are transformed before storage for uniformity

When the process terminates prematurely (by anything, including a SIGTERM, power failure, what have you),  when process is resumed, writing resumes from where it left of. Duplicate entries from writing is prevented.


## Installation

## Setting Up locally without Docker

Requirement:
1. Python 3.
2. SQlite3 or Postgresql.
3. Django(Rest Framework)
4. Celery(python package is it's in requirement file)
5. Rabbitmq

Using Sqlite doesn't require much. It works out of the box. If you have a db preference, just ensure project is set to use your preferred database `finance/setting.py`. 


The project comes with a `requirements.txt` file that contains exactly the python packages and dependencies that the project needs.

To obtain and install them:

```bash
pip/pip3 install -r requirements.txt
```

If setting up for the first time, hence, your database is new, please run the following commands.


```bash
python manage.py makemigrations
python manage.py migrate
```
NB: Please note that project in the repo comes with migration files so you only need to run migrate and not makemigrations.  


When the above has been executed sucessfully, you can run the server now. 

### To Run

```bash
python manage.py runserver 
```

## Running with Docker
```bash
    docker build -t tagNameForDocker
    docker run take tagNameForDocker
```


## Trigger Function to start the read Process
Endpoint `/v0.5/transactions/read-data/`
Pay load:
{
    "file_path" : "data/smaller.json" 
}