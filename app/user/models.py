from app import db
from passlib.hash import pbkdf2_sha512

# Define base model
class Base(db.Model):
    __abstract__  = True
    idx = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

class User(Base):
    __tablename__ = 'user_tbl'
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    enckey = db.Column(db.String(256), nullable=False)
    wallet_pw = db.Column(db.String(256), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False, default=0)

    # Profile Image, text, location
    profile = db.Column(db.String(1000), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    profile_image_imgur = db.Column(db.String(100), nullable=True)
    profile_image_delete_hash = db.Column(db.String(100), nullable=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = pbkdf2_sha12.hash(password, rounds=8000, salt_size=12)
        self.enckey = md5(password).hexdigest()
        self.status = 0

    def verify(self, password):
        return pbkdf2_sha512.verify(password, self.password)

    def __repr__(self):
        return '<User %r>' % (self.username)
