from opsdroid.matchers import match_regex, match_always
from datetime import datetime
from ago import human
import logging

def setup(opsdroid):
    logging.debug("Loaded seen module")

@match_regex(r'when did you last see (?P<name>.*)\?')
async def last_seen(opsdroid, config, message):
    name = message.regex.group('name')
    seen = await opsdroid.memory.get("seen")
    if seen == None or name not in seen:
        await message.respond("I've never seen {} before".format(name))
    else:
        await message.respond("I last saw {} {}".format(name, human(seen[name], precision=1)))

@match_always
async def update_seen(opsdroid, config, message):
    seen = await opsdroid.memory.get("seen")
    if seen == None:
        seen = {}
    seen[message.user] = datetime.now()
    await opsdroid.memory.put("seen", seen)
