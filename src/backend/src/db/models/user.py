from tortoise import fields
from tortoise.models import Model

class User(Model):
    user_id = fields.BigIntField(pk=True)

    name = fields.CharField(64)
    username = fields.CharField(32, null=True)
    
    
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"