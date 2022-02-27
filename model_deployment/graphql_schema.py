from typing import List, Dict

import joblib
import strawberry
from models.gender import Gender
from models.ticket_class import TicketClass
import pandas as pd

classifier = joblib.load('titanic_model.pkl')


@strawberry.input
class SurvivorInput:
    age: int
    gender: Gender
    ticket_class: TicketClass


@strawberry.type
class SurvivorOutput:
    age: int
    gender: Gender
    ticket_class: TicketClass
    survived: bool


@strawberry.type
class Query:
    @strawberry.field
    def survived(self, survivor: SurvivorInput) -> SurvivorOutput:

        survivor_json: Dict = {
            'age': survivor.age,
            'SECOND_CLASS': 1 if survivor.ticket_class == TicketClass.second_class else 0,
            'THIRD_CLASS': 1 if survivor.ticket_class == TicketClass.third_class else 0,
            'male': 1 if survivor.gender == Gender.male else 0,
        }

        survivor_df: pd.DataFrame = pd.DataFrame([survivor_json])
        prediction: bool = bool(classifier.predict(survivor_df)[0])

        return SurvivorOutput(
            age=survivor.age,
            gender=survivor.gender,
            ticket_class=survivor.ticket_class,
            survived=prediction
        )


schema = strawberry.Schema(query=Query)
