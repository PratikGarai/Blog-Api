from passlib.context import CryptContext

class Hash :
    def __init__(self):
        self.pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password : str):
        hashed_password = self.pwd_cxt.hash(password)
        return hashed_password

    def verify(self, hashed, plain) :
        return self.pwd_cxt.verify(plain, hashed)