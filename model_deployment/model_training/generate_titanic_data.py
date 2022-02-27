from pathlib import Path
import sys

root_path: str = Path(__file__).resolve().parent.parent.as_posix()
sys.path.append(root_path)

import random
import pandas as pd
from typing import List, Dict
from models.gender import Gender
from models.ticket_class import TicketClass


def is_survived(gender: Gender, age: int, ticket_class: TicketClass) -> bool:
    if age < 18:
        return True

    if gender.male:
        return False
    else:
        if ticket_class == TicketClass.first_class or ticket_class == TicketClass.second_class:
            return True
        else:
            return False


if __name__ == "__main__":
    """
    This script generates sample training data for a random forest classifier to be trained on
    
    Contains:
    gender,age,ticket_class,survived
    
    rules:
    - if male, 
        - survived will be false regardless of ticket_class, unless age is less than 18
        
    - if female
        - survived will be true if ticker_class is at least 2nd class, or age is less than 18
    """
    list_of_passengers: List[Dict] = []
    possible_gender: List[str] = ["male", "female"]

    for i in range(0,10000):
        gender: Gender = random.choice(list(Gender))
        age: int = random.randint(0, 60)
        ticket_class: TicketClass = random.choice(list(TicketClass))
        survived: bool = is_survived(gender, age, ticket_class)

        list_of_passengers.append({
            "gender": gender,
            "age": age,
            "ticket_class": ticket_class,
            "survived": survived
        })

    df: pd.DataFrame = pd.DataFrame(list_of_passengers)

    df.to_csv("titanic.csv", index=False)



