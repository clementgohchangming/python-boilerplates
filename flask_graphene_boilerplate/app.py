from flask import Flask
from datetime import datetime
from common.logger import logger
import bjoern
from flask_graphql import GraphQLView
from graphql_api import public_schema

"""
Create the Flask app object. We pass in the python application module name as the import_name into Flask.

(Remove this in your project, this docstring is only for your information) 

Verbose Explanation:

__name__ is a special python variable hidden under the hood, and it is set automatically to the python module name
    - In this case, the python module name is the file itself (`app`), as this file is in the root directory, 
    and we are calling __name__ in this file (`app.py`). 
    - If we shift this file into a python package called `my_package`, then the python module name will be `my_package.test`
    - However, when we run this file, which we will
    - __name__ will be set to "__main__"
        
We pass in the python application module name as the import_name into Flask.
    - This import_name is used by Flask to find important files needed by the application
        - template files (.html)
        - static files (.gif, .img, etc)
        
For more information, visit:

1. Why do we pass __name__ to the Flask class?
- https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class#:~:text=If%20you%20call%20Flask(),which%20the%20module%20is%20located.

"""
app = Flask(__name__)

# get the service uptime
service_uptime: datetime = datetime.now()


@app.route('/healthcheck')
def healthcheck():
    """
    expose a healthcheck route.

    (Remove this in your project, this docstring is only for your information)

    Verbose Explanation:
    users can make requests to this route to check if your application is alive.
    """
    uptime_in_seconds = (datetime.now() - service_uptime).total_seconds()
    logger.info(f"healthcheck successful! uptime in seconds: {uptime_in_seconds} seconds")
    return {'uptime': f"{uptime_in_seconds} seconds"}


def graphql_service():
    # add the graphql view function to a new route
    app.add_url_rule("/graphql", view_func=GraphQLView.as_view('graphql', schema=public_schema, graphiql=True))
    logger.info("service started!")

    """
    Bring up the flask server, exposing it at port 5000
    
    (Remove this in your project, this docstring is only for your information) 
    
    Verbose Explanation:
    We require a webserver, a webserver gateway interface (WSGI), and a webserver gateway interface application (WSGI application) to bring up a 
    functional python backend application.
    
    1. Webserver
    - A computer software and underlying hardware that accepts requests from clients via data transfer protocols such as HTTP, HTTPS, or other protocols.
    - Common webservers: Apache, NGINX, IIS
    
    2. Webserver Gateway Interface (WSGI)
    - The interface between the webserver and our python application (WSGI application)
    
    3. Webserver Gateway Interface (WSGI) Application
    - Our python application. 
    - Common WSGI applications: Flask, Django
    
    Diagram of     
    Webserver <-> Webserver Gateway Interface (Bjoern) <-> Webserver Application (Flask)
    
    For more information, refer to this youtube video below
    1. CoderZWorld: What is the need of WSGI in Python ?
    - https://www.youtube.com/watch?v=8bCwDpsVYmE
    """
    bjoern.run(app, "0.0.0.0", 5000)


if __name__ == "__main__":
    graphql_service()
