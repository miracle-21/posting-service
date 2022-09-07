import re

from django.core.exceptions import ValidationError

# 비밀번호는 6자 이상, 숫자 1개 이상 포함되어야 함
PASSWORD_REGEX = '(?=.*\d)[A-Za-z\d$@^!%*#?&]{6,}$'

def validate_password(value):
    if not re.match(PASSWORD_REGEX,value):
        raise ValidationError('invalid password')
