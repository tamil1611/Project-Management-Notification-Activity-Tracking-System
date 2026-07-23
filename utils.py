from passlib.context import CryptContext

#password hashing configuration

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

#hash password

def hash_password(password:str):
    password=password[:72]
    return pwd_context.hash(password)

#verify password
def verify(plain_password:str,
                    hashed_password:str
):
    plain_password=plain_password[:72]
    return pwd_context.verify(
        plain_password,
        hashed_password
    )