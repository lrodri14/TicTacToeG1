from django.db import models

class MySQLBooleanField(models.Field):
    def db_type(self, connection):
        return 'bit(1)'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return bool(int.from_bytes(value, byteorder='big'))

    def to_python(self, value):
        if value is None:
            return value
        return bool(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return value.to_bytes(1, byteorder='big') if value else b'\x00'
