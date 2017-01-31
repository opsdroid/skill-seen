from opsdroid.matchers import match_regex
from datetime import datetime
from ago import human
import logging

def setup(opsdroid):
    logging.debug("Loaded seen module")

@match_regex(r'when did you last see (.*)\?')
async def last_seen(opsdroid, config, message):
    name = message.regex.group(1)
    seen = await opsdroid.memory.get("seen")
    if seen == None or name not in seen:
        await message.respond("I've never seen " + message.regex.group(1) + " before")
    else:
        await message.respond("I last saw " + message.regex.group(1) + " " + human(seen[name], precision=1))

@match_regex(r'.*')
async def update_seen(opsdroid, config, message):
    seen = await opsdroid.memory.get("seen")
    if seen == None:
        seen = {}
    seen[message.user] = datetime.now()
    await opsdroid.memory.put("seen", seen)
