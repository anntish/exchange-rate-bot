from models.base_model import db
from models.user import User

db.create_tables([User], safe=True)
