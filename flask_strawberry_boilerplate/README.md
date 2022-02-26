# Flask-Graphql Backend Boilerplate (with Strawberry)

This repository contains a sample boilerplate for you to quickly bring up a python backend application.

##  Bringing up the application locally.

Step 1: Install all requirements into a virtual environment with `virtualenv`

```commandline
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Step 2: Bring up the python application

```commandline
python3 app.py
```

## Bringing up the application locally with docker

This repository contains a Dockerfile, which contains instructions to create a docker image.

This docker image then can be run to bring up the application, encapsulated in a docker container.

Step 1: To build a docker image with the Dockerfile, run the following command

This command builds a docker image with the Dockerfile in the current directory (`.`), with the tag `boilerplate`. 

This tag can later be used to refer to this docker image.

```commandline
docker build -t boilerplate .
```

Step 2: Use the docker image `boilerplate` to bring up the application. 

Expose the port 5000 on the docker container (same port on the docker container hosting the python application) to our localhost port 6000, so we can make requests to the python application on our local port 6000.

```commandline
docker run -p 6000:5000 -t boilerplate
```

## Making a request to healthcheck

We can either make a request as a client to our local python backend server via a `curl` GET request 

```commandline
(base) MacBook-Pro-2:python-boilerplates gohchangmingclement$ curl --request GET \
>   --url http://localhost:5000/healthcheck
{"uptime":"135.28324 seconds"}
```
or through an API design platform such as Insomnia
- https://insomnia.rest/download

## Making a request to our GraphQL Python Backend Server

```commandline
MacBook-Pro-2:python-boilerplates gohchangmingclement$ curl --request POST   --url http://localhost:6000/graphql   --header 'Content-Type: application/json'   --data '{"query":"query GetFruit {\n\tfruits {\n\t\tname\n\t\tcolor\n\t}\n}","variables":{"input":{"name":"Eugene"}},"operationName":"GetFruit"}'
{"data": {"fruits": [{"name": "Banana", "color": "Yellow"}]}}
```
## This repository uses a couple of common libraries 

```requirements.txt
Flask==1.1.4                # Flask Backend Library
bjoern==2.0.5               # Webserver Gateway Interface Library, used to interface flask with webserver
pydantic==1.6               # Type-safe model library. Asserts type safety of object fields to avoid type-related bugs
strawberry-graphql==0.95.0  # a GraphQL library compatible with the type-safety library pydantic
python-json-logger==2.0.2   # Formats the logs from the python logger into a json object. Json logs are easier to parse and log in log monitoring systems
markupsafe==2.0.1           # Forcibly use 2.0.1 for markupsafe. Fixes a compatibility issue from Flask 1.1.4, https://itsmycode.com/importerror-cannot-import-name-json-from-itsdangerous/
```