from passlib.hash import pbkdf2_sha512


class Utlis:
    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.hash(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)
