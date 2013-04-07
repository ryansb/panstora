try:
    import os
    os.remove("/tmp/test.db")
except:
    pass

from panstora.models import *

import transaction

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
    i.put()
    it = Item.get_by_name(item['name'])
    for tag in item['tags']:
        if Tag.get_by_name(tag):
            it.tags.append(Tag.get_by_name(tag))
            continue
        t = Tag()
        t.name = tag
        it.tags.append(t)
        it.put()

users = json.loads(open('data/test_users.json').read())
for u in users:
    user = User(u['dev_id'])
    user.name = u['name']
    user.email = u['email']
    user.password = u['password']
    user.username = u['username']
    user.put()

DBSession.flush()
transaction.commit()
