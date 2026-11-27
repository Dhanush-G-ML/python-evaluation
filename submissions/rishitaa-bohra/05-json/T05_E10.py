# T05-E10 - Challenge: flatten, diff and deep-merge configuration files
#
# Write four functions for nested dictionaries (lists and empty dictionaries are treated as plain values):
#
# - `flatten(data)` - one-level dictionary with dotted keys, for example `{"a": {"b": 1}}` becomes `{"a.b": 1}`.
# - `unflatten(flat)` - the reverse.
# - `diff(old, new)` - compare two nested dictionaries through their flattened form and return `{"added": {key: value}, "removed": {key: old_value}, "changed": {key: (old, new)}}` with keys sorted.
# - `deep_merge(base, override)` - new dictionary; nested dictionaries are merged recursively, any other value in `override` replaces the one in `base`; neither input may be changed.
#
# Main program with `data/config.json` (v1) and `data/config_v2.json` (v2): print `Flat keys: <n>`, the flat value of `server.timeouts.read`, `Round trip ok: <bool>` (`unflatten(flatten(v1)) == v1`), the diff as lines `added   <key> = <json value>`, `removed <key> (was <json value>)` and `changed <key>: <old json> -> <new json>` (added first, then removed, then changed), then merge `{"server": {"port": 9090, "timeouts": {"read": 60}}, "features": {"signup": False}}` into v1 and print `merged server:` and `merged features:` as JSON with sorted keys, and `v1 unchanged: <bool>`.
