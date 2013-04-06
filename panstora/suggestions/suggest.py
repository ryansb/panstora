'''
suggest looks in the database to find all items
 * Suggestion Logic
     * Creates list of items that have similar tags
     * Sorts by number of related tags
 * Returns top one
suggest calls sendSuggestion
'''

from panstora.models import (
    Base,
    User,
    Item,
    Tag
)

from panstora.suggestions import (
    sendSuggestion
)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getMostMatchingTags(base_item, db):
    x = []
    for tag in base_item.tag:
        x = db.query(Tag).filter_by(name=tag)
    return None


def getSuggestion(base_item, dbname="sqlite:////tmp/test.db", mode=getMostMatchingTags):
    # Set up the sqlite connection
    engine = create_engine(dbname)
    metadata = Base.metadata
    metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # Create the database
    db = Session()
    # Return the suggestion chosen by that particular method
    return mode(base_item, db)


def suggest(regid, base_item):
    sug = getSuggestion(base_item)
    sendSuggestion(regid, sug)
