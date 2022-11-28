from typing import Any
from utils import database
from models import promocodes

def get_database_table() -> str:
    return """CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    promocode_id INTEGER, FOREIGN KEY (promocode_id) REFERENCES promocodes(id)
)"""


class User:
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        if does_exist(user_id):
            create(user_id)

    def __query(self, field: str) -> Any:
        return database.fetch(f"SELECT {field} FROM users WHERE id = ?", (self.user_id,))

    def __update(self, field: str, value: Any) -> None:
        database.execute(f"UPDATE users SET {field} = ? WHERE id = ?", (value, self.user_id))

    @property
    def promocode(self) -> promocodes.Promocode:
        return promocodes.Promocode(self.__query("promocode"))
    @promocode.setter
    def promocode(self, value: promocodes.Promocode) -> None:
        self.__update("promocode", value.id)


def create(user_id: int) -> User:
    database.execute("INSERT INTO users VALUES (?, ?)", (user_id, None))
    return User(user_id)


def does_exist(user_id: int) -> bool:
    return database.fetch("SELECT id FROM users WHERE id = ?", (user_id,)) is not None