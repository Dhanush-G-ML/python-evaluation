# T05-E07 - Custom JSON encoder and decoder
#
# `json.dumps` cannot handle `datetime`, `Decimal`, `set` or dataclass objects. Create:
#
# - a dataclass `Customer(name: str, vip: bool)`;
# - `class AppEncoder(json.JSONEncoder)` with a `default` method that converts `datetime` to its ISO text, `Decimal` to a string (so no precision is lost), a `set` to a sorted list, and a dataclass to a dictionary (`dataclasses.asdict`); everything else must still raise `TypeError` (call `super().default(o)`);
# - `encode(obj)` that dumps with this encoder and `sort_keys=True`;
# - `decode(text)` that uses `object_hook` to turn the `created` key back into a `datetime` and the `total` key back into a `Decimal`.
#
# Encode the record below, print the JSON text, decode it and print the type and value of `created`, `total`, `tags` and `customer`, and finally show that plain `json.dumps` fails (`Default encoder fails: <message>`).
