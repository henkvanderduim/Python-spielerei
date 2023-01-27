import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"super_secret_password"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    iterations=100000,
    length=32,
    salt=salt,
    backend=default_backend(),
)
key = base64.urlsafe_b64encode(kdf.derive(password))
cipher = Fernet(key)

# Encrypt the file
with open("file.txt", "rb") as f:
    data = f.read()

cipher_text = cipher.encrypt(data)

with open("file.txt", "wb") as f:
    f.write(cipher_text)
