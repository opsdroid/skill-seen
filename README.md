# opsdroid skill seen

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to record when it last saw each user and report the values.

## Requirements

 * A database must be configured to persist the data

## Configuration

This module requires no configuration.

## Usage

_This module updates a list of usernames with a timestamp every time a message is parsed._

### `when did you last see <user>?`

Responds with the last time opsdroid saw the user.

> user: when did you last see john?
>
> opsdroid: I last saw john 7 minutes ago

## License

GNU General Public License Version 3 (GPLv3)
