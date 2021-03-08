import uuid
from models import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(128), unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128))
    mail_id = db.Column(db.String(128))
    password = db.Column(db.String(128))
    phone_number = db.Column(db.String(128))
    contact_type = db.Column(db.String(128))
    address = db.Column(db.String(512))

    def __init__(
            self,
            name,
            mail_id,
            password,
            phone_number,
            contact_type,
            address
    ):
        self.name = name
        self.mail_id = mail_id
        self.password = password
        self.phone_number = phone_number
        self.contact_type = contact_type
        self.address = address

    @staticmethod
    def create_user(
            name,
            mail_id,
            password,
            phone_number,
            contact_type,
            address
    ):
        user = User(
            name=name,
            mail_id=mail_id,
            password=password,
            phone_number=phone_number,
            contact_type=contact_type,
            address=address
        )
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_mail_id(mail_id):
        user = User.query.filter_by(mail_id=mail_id).first()
        return user
