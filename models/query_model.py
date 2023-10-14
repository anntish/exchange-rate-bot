from datetime import datetime
import peewee as pw

db = pw.SqliteDatabase('database.pw')


class BaseModel(pw.Model):
    """
    Класс BaseModel. Базовый класс, создающий соединение с базой данных.
    """
    class Meta:
        database = db


class Query(BaseModel):
    """
    Класс User. Хранит информацию о пользователе и его запросах.
    """
    time = pw.DateTimeField(default=datetime.now)
    user_id = pw.IntegerField()
    request_text = pw.TextField()
    response_text = pw.TextField()


db.create_tables([Query], safe=True)
