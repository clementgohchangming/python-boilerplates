from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str

    @property
    def domain(self):
        return self.email.split("@")[1]