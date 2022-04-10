# Introduction
# Installation
```
pip install pipenv
pipenv install --system
```

# Usages
### Pure django application
* start the django locally
```
git checkout master
python manage.py runserver
```
* Visit to the localhost:8000 on the browser

### Use with docker
* start the django locally with docker
```
git checkout docker-compose
docker compose up
```
* Visit to the localhost:10555 on the browser

### Use the example with django, postgreSQL, and docker
* Install PostgreSQL
* Create a database for POstgreSQL locally
```
psql
create database studentdb;
\c studentdb;
create user test with encrypted password 'password';
grant all privileges on database studentdb to test;

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


