import peewee as pw

db = pw.SqliteDatabase('test_3.pw')


class BaseModel(pw.Model):
    class Meta:
        database = db
