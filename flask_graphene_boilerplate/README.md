# Flask-Graphql Backend Boilerplate

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
(base) MacBook-Pro-2:python-boilerplates gohchangmingclement$ curl --request POST \
>   --url http://localhost:5000/graphql \
>   --header 'Content-Type: application/json' \
>   --data '{"query":"query GetUser($input: UserInput!) {\n\tusers(userInput: $input) {\n\t\tname\n\t}\n}","variables":{"input":{"name":"Eugene"}},"operationName":"GetUser"}'
{"data":{"users":{"name":"Eugene"}}
```
## This repository uses a couple of common libraries 

```requirements.txt
Flask==1.1.2                # Flask Backend Library
Flask-GraphQL==2.0.1        # Flask-GraphQL Interoperability Library
bjoern==2.0.5               # Webserver Gateway Interface Library, used to interface flask with webserver
graphql-core==2.3.2         # Graphql Core Library, used to easily create self-documenting backend servers
pydantic==1.6               # Type-safe model library. Asserts type safety of object fields to avoid type-related bugs
graphene-pydantic==0.1.0    # Interoperability Library between pydantic pydantic_models and graphene pydantic_models
python-json-logger==2.0.2   # Formats the logs from the python logger into a json object. Json logs are easier to parse and log in log monitoring systems
```