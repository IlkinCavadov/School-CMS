from pwdlib import PasswordHash


password_hasher = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    print(repr(hashed_password))
    print(type(hashed_password))
    return password_hasher.verify(password, hashed_password)