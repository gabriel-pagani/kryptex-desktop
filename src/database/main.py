import os
from connection import execute_query


# execute_query(
#     "INSERT INTO users (username, master_password_hash, salt) VALUES (?, ?, ?)",
#     ("gabriel", "hash_fake_123", os.urandom(16))
# )

# execute_query(
#     "INSERT INTO password_types (name) VALUES (?)",
#     ("email",)
# )

# execute_query(
#     """
#     INSERT INTO passwords (user_id, type_id, service, login, iv, password_encrypted) VALUES (?, ?, ?, ?, ?, ?)
#     """,
#     (1, 1, "Gmail", "gabriel@gmail.com", b"iv", b"senha_criptografada")
# )

# execute_query(
#     "UPDATE passwords SET password_encrypted = ? WHERE id = ?",
#     (b"nova_senha_crip22tografada", 1)
# )

execute_query("DELETE FROM passwords WHERE id = ?", (1,))