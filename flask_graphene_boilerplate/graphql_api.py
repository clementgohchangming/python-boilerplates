import graphene

from graphene_models.input_object_types import UserInput
from graphene_pydantic_models.junction_models import UserGrapheneModel
from pydantic_models.user import User


class Query(graphene.ObjectType):
    """
    Create a graphql Query object.

    It defines the available fields to the clients; each object property under it is a field.
    """

    """
    create a users field, which accepts a GraphQL Input Object, and returns a Pydantic-Graphql Object User
    We use the Pydantic-GraphQL Object instead of the corresponding graphql object directly,
    so pydantic can assert type safety of all fields in the model for us
    """
    users = graphene.Field(
        UserGrapheneModel,
        user_input=graphene.Argument(UserInput),
        description="Takes a user name from the client, and returns the same user back to the client. Dummy graphql field example."
    )

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_users(root, info, user_input: UserInput):
        return User(name=user_input.name)


public_schema = graphene.Schema(query=Query)