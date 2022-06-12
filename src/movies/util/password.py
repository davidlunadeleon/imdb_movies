import hashlib
import os


def hash(value: str, salt: bytes = os.urandom(32)) -> bytes:
    hashed_password = hashlib.pbkdf2_hmac("sha256", value.encode("utf-8"), salt, 100000)
    return salt + hashed_password


def get_salt(value: bytes) -> bytes:
    return value[:32]


def compare(original: bytes, value: str) -> bool:
    salt = get_salt(original)
    return original == hash(value, salt)
