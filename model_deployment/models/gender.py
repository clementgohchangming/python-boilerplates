from enum import Enum

import strawberry


@strawberry.enum
class Gender(str, Enum):
    male: str = "male"
    female: str = "female"