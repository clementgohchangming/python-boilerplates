from flask import Flask
from datetime import datetime
import bjoern
from common.logger import logger
from graphql_schema import schema
from strawberry.flask.views import GraphQLView

app = Flask(__name__)

server_uptime: datetime = datetime.now()

@app.route
def healthcheck():
    uptime_in_seconds: float = (datetime.now() - server_uptime).total_seconds()
    return {
        'uptime': f"{uptime_in_seconds} seconds"
    }


def graphql_service():
    app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema))
    logger.info("service started!")
    bjoern.run(app, "0.0.0.0", 5000)


if __name__ == "__main__":
    graphql_service()