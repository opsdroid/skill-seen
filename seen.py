from opsdroid.skills import match_regex
import logging

def setup(opsdroid):
    logging.debug("Loaded seen module")

@match_regex(r'when did you last see (.*)\?')
def last_seen(opsdroid, message):
    print(message.regex)
    message.respond("Never seen "  + " before")
