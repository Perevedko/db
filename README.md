[![Build Status](https://www.travis-ci.org/mini-kep/db.svg?branch=db-views)](https://www.travis-ci.org/mini-kep/db)


#### 1. What we are doing (intent):

- Implementation of POST method and GET method as descibed in spec with tests in a flask application.
- omitting security tokens in POST method

#### 2. What is wrong now (problems):
- we have some code for the app, but testing environment is wrong - the test app shoud be based on sqlite, not postgres.
postgres will be used as production environment on heroku. 

- there may be some wrong design decisions / omissions in application, must check whole code 

- general python code conventions (eg style of imports)

### 3. What we want (todo):

- [ ] change dev and test databases to sqlite
- [ ] cleaner test design (setup, call, result check separated + test class and nethod naming)
- [ ] Travis must pass on tests
- [ ] more standard/conventional approach for the flask app + comment on what desing decision are better
- [ ] style changes


------------------

From previous implementation:

> # Installation
> Some instructions to deploy

    ## Install posgresql:
    - sudo apt-get update
    - sudo apt-get install postgresql postgresql-contrib
    - sudo -u postgres psql
    - CREATE DATABASE <dbname>;
    - CREATE USER <user> WITH PASSWORD '<password>';
    - GRANT ALL PRIVILEGES ON DATABASE <dbname> TO <user>;

    ## Initiate new database from python console:
    - from application import init_db
    - init_db(config_name(optional)) / by default sets DevelopmentConfig
