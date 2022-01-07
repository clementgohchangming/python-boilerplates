"""
A dummy service-level model, representing a user
We will be returning this via the graphql api
"""
from pydantic import BaseModel


class User(BaseModel):
    name: str



