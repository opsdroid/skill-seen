from opsdroid.skills import match_regex
import logging

def setup(opsdroid):
    logging.debug("Loaded seen module")

@match_regex(r'when did you last see (.*)\?')
def last_seen(opsdroid, message):
    message.respond("Never seen " + message.regex.group(1) + " before")
