from panstora.models import (
    Item
)

from panstora.suggestions import (
    sendSuggestion
)


def getMostMatchingTags(base_item, items):
    ''' Basic matching - find one that matches the most tags '''
    stats = {}
    for item in items:
        stats[item] = reduce(tag in base_item.tags for tag in item.tags)
    return max(stats.iterkeys(), key=lambda k: stats[k])


def getSuggestion(base_item, mode=getMostMatchingTags):
    ''' Return the suggestion chosen by the given method '''
    return mode(base_item, Item.get_all())


def suggest(regid, base_item):
    ''' Send a suggestion to a user based on an item '''
    sug = getSuggestion(base_item)
    sug.suggType = None
    sendSuggestion(regid, sug)
