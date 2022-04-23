from typing import Optional

from postgres_service.dbo_service import DBOService
from postgres_service.models.user import User


class UserService(DBOService[User]):

    def create_table(self) -> None:
        """
        Creates a table for the DBO
        """
        create_table_fragment: str = """
        CREATE TABLE users (
            ID INT
        )
        """

    def select_one(self, id: str) -> Optional[User]:
        """
        Read a DBO
        """
        with self.postgres_service.connector.cursor():


    def insert_one(self, dbo: User) -> None:
        """
        Insert a DBO
        """
        pass

    def update_one(self, dbo: User) -> None:
        """
        Update a DBO
        """
        pass

    def delete(self, id: str) -> None:
        """
        delete a DBO
        """
        pass