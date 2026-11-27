# T05-E02 - Read a config file
#
# Load `data/config.json` with `json.load`. Write `get_nested(data, path, default=None)` that follows a dotted path such as `"server.timeouts.read"` and returns the value, or `default` when any step of the path is missing (also when a step is not a dictionary). A value of `False` or `0` is a real value and must be returned, not the default. Print each path in the list below as `<path> = <repr of value>`, using the default shown, then print the admins joined with `, ` and their count.
