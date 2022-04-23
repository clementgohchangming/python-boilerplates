from postgres_service.models.user import User
from postgres_service.postgres_service import PostgresService

if __name__ == "__main__":
    postgres_service: PostgresService = PostgresService()

    user: User = User(name="Zheng Yang", email="zhengyanglim057@gmail.com")
    print(f"vars(user): {vars(user)}")