from typequery import GenericMethod

from models.login_expiry import LoginExpiry
from models.user_info import UserInfo

serialize = GenericMethod('serialize')


@serialize.of(bool)
@serialize.of(type(None))
@serialize.of(int)
@serialize.of(float)
@serialize.of(str)
def serialize(value, **kwargs):
    return value


@serialize.of(UserInfo)
def serialize(user_info, **kwargs):
    result = {
        'email': user_info.email,
        'name': user_info.name,
        'age': user_info.age,
    }
    return result


@serialize.of(LoginExpiry)
def serialize(login_expiry, **kwargs):
    result = {
        'email': login_expiry.email,
        'name': login_expiry.name,
        'uuid': login_expiry.uuid,
        'expiry': login_expiry.expiry,
    }
    return result
