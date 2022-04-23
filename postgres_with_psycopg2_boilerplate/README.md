# PostgreSQL with Python

## Python Version: 3.9 - Creating a virtual env and installing dependencies

```commandline
virtualenv venv -p $(which python3.9)
source venv/bin/activate
pip3 install -r requirements.txt
```

## Starting and stopping a local postgres service

Installing postgresql 

```commandline
brew install postgresql
```

To start the local postgres service:

```commandline
pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
```

To stop the local postgres service:

```commandline
pg_ctl -D /usr/local/var/postgres stop && brew services stop postgresql
```

## Starting and stopping a local postgres service with docker

To start the local postgres service as a docker container

```commandline
docker-compose -f postgres-docker-compose.yml up
```

To run the database, detached from your terminal window, specify the same command but with the `-d` flag

```commandline
docker-compose -f postgres-docker-compose.yml up -d
```

To stop the local postgres service as a docker container

```commandline
docker-compose -f postgres-docker-compose.yml down
```

## Sources:

1. Getting started with postgresql on macosx
- https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

2. Python PostgreSQL
- https://zetcode.com/python/psycopg2/