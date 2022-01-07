import graphene


class User(graphene.ObjectType):
    user_name = graphene.NonNull(graphene.String, description='The user name')
