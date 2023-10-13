from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase('database.pw')


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    time = pw.DateTimeField(default=datetime.now)
    user_id = pw.IntegerField()
    request_text = pw.TextField()
    response_text = pw.TextField()


db.create_tables([User], safe=True)
