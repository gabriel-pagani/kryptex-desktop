from typing import Optional
from database.connection import execute_query


class User:
    def __init__(
        self, 
        id: int, 
        salt: bytes, 
        username: str,  
        master_password_hash: str
    ):
        self.id = id
        self.salt = salt
        self.username = username
        self.master_password_hash = master_password_hash

    @classmethod
    def get(cls, id: int) -> Optional['User']:
        try:
            response = execute_query(
                "SELECT * FROM users WHERE id = ?",
                (id,)
            )
            
            if response != []:
                return cls(
                    id=response[0][0], 
                    salt=response[0][1], 
                    username=response[0][2], 
                    master_password_hash=response[0][3]
                )
            return None

        except Exception as e:
            print(f"exception-on-get: {e}")
            return None
