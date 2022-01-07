"""
Contains junction models between its corresponding graphene and pydantic counterparts
"""
from pathlib import Path
import sys
from pydantic_models.user import User

# appends the path to the root of the project, to the python path. this lets this file import files relative to root
sys.path.append(Path(__file__).resolve().parent.parent.as_posix())

from graphene_pydantic import PydanticObjectType


class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = User