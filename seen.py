from opsdroid.skills import match_regex
from datetime import datetime
import logging

def setup(opsdroid):
    logging.debug("Loaded seen module")

@match_regex(r'when did you last see (.*)\?')
def last_seen(opsdroid, message):
    name = message.regex.group(1)
    seen = opsdroid.memory.get("seen")
    if seen == None or name not in seen:
        message.respond("Never seen " + message.regex.group(1) + " before")
    else:
        message.respond("I last saw " + message.regex.group(1) + " on " + seen[name])

@match_regex(r'.*')
def update_seen(opsdroid, message):
    seen = opsdroid.memory.get("seen")
    if seen == None:
        seen = {}
    seen[message.user] = datetime.now()
    opsdroid.memory.put("seen", seen)
