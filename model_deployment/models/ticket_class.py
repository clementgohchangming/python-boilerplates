from enum import Enum
import strawberry


@strawberry.enum
class TicketClass(str, Enum):
    first_class: str = "FIRST_CLASS"
    second_class: str = "SECOND_CLASS"
    third_class: str = "THIRD_CLASS"