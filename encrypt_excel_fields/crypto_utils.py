import base64
import hashlib
from cryptography.fernet import Fernet


def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_value(value, password):
    if value is None or str(value).strip() == "":
        return value

    key = generate_key(password)
    cipher = Fernet(key)

    return cipher.encrypt(str(value).encode()).decode()


def decrypt_value(value, password):
    if value is None or str(value).strip() == "":
        return value

    try:
        key = generate_key(password)
        cipher = Fernet(key)

        return cipher.decrypt(str(value).encode()).decode()

    except Exception:
        return value