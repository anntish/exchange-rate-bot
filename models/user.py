import peewee as pw
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    time = pw.DateTimeField(default=datetime.now)
    user_id = pw.IntegerField()
    request_text = pw.TextField()
    response_text = pw.TextField()
