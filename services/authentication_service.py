from helpers.exceptions import UserNotFoundException

from models.user import User


class AuthenticationService:

    @classmethod
    def signup(cls, payload):
        name = payload.get('name')
        mail_id = payload.get('mail_id')
        phone_number = payload.get('phone_number')
        password = payload.get('password')

        User.create_user(
            name=name,
            mail_id=mail_id,
            password=password,
            phone_number=phone_number,
            contact_type="STAFF",
            address="address"
        )

    @classmethod
    def sign_in(cls, payload):
        mail_id = payload.get('mail_id')
        password = payload.get('password')
        user = User.get_user_by_mail_id(mail_id=mail_id)

        if user.password != password:
            raise UserNotFoundException(message="User Not Found ..!!!!")

        response = {
            "user_id": user.id
        }

        return response
