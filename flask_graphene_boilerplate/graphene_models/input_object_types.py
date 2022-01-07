import graphene

"""
Contains all graphql input object types
"""


class UserInput(graphene.InputObjectType):
    name = graphene.NonNull(graphene.String,
                            description='The user name')