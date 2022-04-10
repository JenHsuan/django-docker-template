# Introduction
# Installation
```
pip install pipenv
pipenv install --system
```

# Usages
## 1. Use the example with django and postgreSQL locally
* Chekout git branch
```
git checkout docker-compose-postgresql
```
* Install PostgreSQL
* Create a database for POstgreSQL locally
```
psql
create database studentdb;
\c studentdb;
create user test with encrypted password 'password';
grant all privileges on database studentdb to test;

```
* Update Config/settings.py

```
import os
...
DATABASES = {
    'default': {
        ...
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("PORT")
    }
}
```

* Set env variables
```
export USER=<USER>
export PASSWORD=<PASSWORD>
export HOST=localhost
export PORT=5432
```
* Migrates
```
python manage.py migrate
```
* Insert test data
```
psql
\c studentdb;
insert into "firstapp_student" (first_name, last_name,test_score) values ('sean', 'hsieh', 100);
```

* Run the server
```
python manage.py runserver
```

* Visit http://localhost:8000/students/


## 2. Use the example with django and postgreSQL with Docker
* Chekout git branch
```
git checkout docker-compose-postgresql
```

* Insert test data
```
$ docker exec -it db bash
root:/# psql --username=test --dbname=studentdb
studentdb=/# insert into "firstapp_student" (first_name, last_name,test_score) values ('sean', 'hsieh', 100);
```

* Execute docker-compose
```
$ docker compose up
```

* Visit http://localhost:8000/students/


