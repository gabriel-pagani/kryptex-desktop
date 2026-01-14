from typing import Optional, List
from datetime import datetime
from database.connection import execute_query
from utils.cryptor import encrypt_data


class Password:
    def __init__(
        self,
        id: int,
        user_id: int,
        type_id: Optional[int],
        iv: bytes,
        encrypted_data: bytes,
        created_at: datetime,
        updated_at: Optional[datetime],
    ):
        self.id = id
        self.user_id = user_id
        self.type_id = type_id
        self.iv = iv
        self.encrypted_data = encrypted_data
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create(
        cls,         
        user_id: int,
        user_key: bytes,
        data: dict,
        type_id: Optional[int] = None,
    ) -> Optional['Password']:
        try:
            associated_data = f'user_id:{user_id};'.encode()
            iv, encrypted_data = encrypt_data(user_key, data, associated_data)
            
            response = execute_query(
                "INSERT INTO passwords (user_id, type_id, iv, encrypted_data) VALUES (?, ?, ?, ?) RETURNING *",
                (user_id, type_id, iv, encrypted_data)
            )

            if response != []:
                return cls(
                    id=response[0][0],
                    user_id=response[0][1],
                    type_id=response[0][2],
                    iv=response[0][3],
                    encrypted_data=response[0][4],
                    created_at=response[0][5],
                    updated_at=response[0][6],
                )
            return None
            
        except Exception as e:
            print(f"exception-on-create: {e}")
            return None

    @classmethod
    def get(cls, id: int) -> Optional['Password']:
        try:
            response = execute_query(
                "SELECT * FROM passwords WHERE id = ?",
                (id,)
            )

            if response != []:
                return cls(
                    id=response[0][0],
                    user_id=response[0][1],
                    type_id=response[0][2],
                    iv=response[0][3],
                    encrypted_data=response[0][4],
                    created_at=response[0][5],
                    updated_at=response[0][6],
                )
            return None

        except Exception as e:
            print(f"exception-on-get: {e}")
            return None

    @classmethod
    def get_all_by_user(cls, user_id: int) -> List['Password']:
        try:
            response = execute_query(
                "SELECT * FROM passwords WHERE user_id = ?",
                (user_id,),
            )

            passwords = []
            if response:
                for row in response:
                    passwords.append(
                        cls(
                            id=row[0],
                            user_id=row[1],
                            type_id=row[2],
                            iv=row[3],
                            encrypted_data=row[4],
                            created_at=row[5],
                            updated_at=row[6],
                        )
                    )
            return passwords

        except Exception as e:
            print(f"exception-on-get-all: {e}")
            return []

    def update(
        self,
        user_key: bytes,
        type_id: Optional[int] = None,
        data: Optional[dict] = None,
    ) -> bool:
        try:
            if data:
                associated_data = f'user_id:{self.user_id};'.encode()
                iv, encrypted_data = encrypt_data(user_key, data, associated_data)

            fields = list()
            values = list()
            
            if type_id is not None:
                fields.append("type_id = ?")
                values.append(None if type_id == 0 else type_id)
            if data:
                fields.append("iv = ?")
                values.append(iv)

                fields.append("encrypted_data = ?")
                values.append(encrypted_data)
            
            if not fields:
                return False

            values.append(self.id)
            execute_query(
                f"UPDATE passwords SET {', '.join(fields)} WHERE id = ?", 
                tuple(values)
            )
            
            self.type_id = type_id if type_id else self.type_id
            self.iv = iv if iv else self.iv
            self.encrypted_data = encrypted_data if encrypted_data else self.encrypted_data

            return True

        except Exception as e:
            print(f"exception-on-update: {e}")
            return False

    def delete(self) -> bool:
        try:
            if not self.id:
                return False
            
            execute_query(
                "DELETE FROM passwords WHERE id = ?",
                (self.id,)
            )
            
            return True

        except Exception as e:
            print(f"exception-on-delete: {e}")
            return False
