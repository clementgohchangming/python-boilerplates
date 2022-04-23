import psycopg2


class PostgresService:
    """
    low-level service responsible for establishing a connector to a postgres database, and closing the connector when its no longer used.
    """

    def __init__(
        self,
        database: str = "postgres",
        user: str = "postgres",
        password: str = "postgres",
        host: str = "127.0.0.1",
        port: str = "5432",
    ):
        """
        Establish a postgres connector. the default user and password are in `postgres-docker-compose.yml`
        :param database: the postgres database name
        :param user: the postgres user to the postgres database
        :param password: the postgres user password
        :param host
        """
        self.connector: psycopg2.connection = psycopg2.connect(
            database=database, user=user, password=password, host=host, port=port
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Leaving contexts doesnt close the postgres connection
        """
        self.connector.close()
