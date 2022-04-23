from postgres_service.postgres_service import PostgresService
from abc import ABC
from typing import Generic, TypeVar, Optional

"""
Create a DBO (Database Object) generic type alias
"""
DBO = TypeVar["DBO"]


class DBOService(Generic[DBO], ABC):
    def __init__(self, postgres_service: PostgresService):
        self.postgres_service: PostgresService = postgres_service

    def create_table(self) -> None:
        """
        Creates a table for the DBO
        """
        pass

    def select_one(self, id: str) -> Optional[DBO]:
        """
        Read a DBO
        """
        pass

    def insert_one(self, dbo: DBO) -> None:
        """
        Insert a DBO
        """
        pass

    def update_one(self, dbo: DBO) -> None:
        """
        Update a DBO
        """
        pass

    def delete(self, id: str) -> None:
        """
        delete a DBO
        """
        pass
