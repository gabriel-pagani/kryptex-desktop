from typing import Optional
from datetime import datetime
from database.connection import execute_query


class PasswordHistory:
    def __init__(
        self,
        id: int,
        password_id: Optional[int],
        user_id: int,
        type_id: Optional[int],
        service: str,
        login: Optional[str],
        iv: bytes,
        encrypted_password: bytes,
        url: Optional[str],
        notes: Optional[str],
        changed_at: datetime,
    ):
        self.id = id
        self.password_id = password_id
        self.user_id = user_id
        self.type_id = type_id
        self.service = service
        self.login = login
        self.iv = iv
        self.encrypted_password = encrypted_password
        self.url = url
        self.notes = notes
        self.changed_at = changed_at

    @classmethod
    def get(cls, id: int) -> Optional['PasswordHistory']:
        try:
            response = execute_query(
                "SELECT * FROM password_history WHERE id = ?",
                (id,)
            )

            if response != []:
                return cls(
                    id=response[0][0],
                    password_id=response[0][1],
                    user_id=response[0][2],
                    type_id=response[0][3],
                    service=response[0][4],
                    login=response[0][5],
                    iv=response[0][6],
                    encrypted_password=response[0][7],
                    url=response[0][8],
                    notes=response[0][9],
                    changed_at=response[0][10],
                )
            return None

        except Exception as e:
            print(f"exception-on-get: {e}")
            return None
