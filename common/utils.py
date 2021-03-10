from passlib.hash import pbkdf2_sha512


class Utlis:
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in Utlis.ALLOWED_EXTENSIONS

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.hash(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)
