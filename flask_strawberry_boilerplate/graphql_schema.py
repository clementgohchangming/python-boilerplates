from typing import List, Dict
import strawberry


@strawberry.type
class Fruit:
    name: str
    color: str


@strawberry.type
class Query:
    @strawberry.field
    def fruits(self) -> List[Fruit]:
        return [
            Fruit(
                name="Banana",
                color="Yellow"
            ),
        ]


schema = strawberry.Schema(query=Query)
