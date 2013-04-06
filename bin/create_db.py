from panstora.models import Base, Item, Tag, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine("sqlite:////tmp/test.db")

metadata = Base.metadata
metadata.create_all(engine)

products = json.loads(open('data/test_products.json').read())

Session = sessionmaker(bind=engine)
db = Session()

for item in products:
    i = Item()
    i.name = item['name']
    i.description = item['description']
    i.price = item['price']
    i.rack = item['location']['rack']
    i.dept = item['location']['dept']
    for tag in item['tags']:
        if db.query(Tag).filter_by(name=tag).first():
            i.tags.append(db.query(Tag).filter_by(name=tag).first())
            db.add(i)
            db.commit()
            continue
        t = Tag()
        t.name = tag
        i.tags.append(t)
        db.add(t)
        db.add(i)
        db.commit()
    db.add(i)
    db.commit()

users = json.loads(open('data/test_users.json').read())
for u in users:
    user = User(u['dev_id'])
    user.name = u['name']
    user.email = u['email']
    user.password = u['password']
    user.username = u['username']
    db.add(user)
    db.commit()
