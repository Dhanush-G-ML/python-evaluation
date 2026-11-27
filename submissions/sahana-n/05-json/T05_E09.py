# T05-E09 - Challenge: validate JSON against a hand-written schema
#
# Write `validate(data, schema, path="")` that returns a list of error strings (empty when valid). A schema is built from:
#
# - a Python type (`str`, `int`, `bool`, `float`) - the value must be of that type; a `bool` is not accepted where `int` is expected;
# - a dictionary of `key: schema` - the value must be an object; every key is required unless wrapped in `Optional`; extra keys are allowed;
# - a list with one element, `[schema]` - the value must be an array and every item must match;
# - `Optional(schema)` (a small class you write) - the key may be missing or `null`.
#
# Error format: `<path>: missing`, `<path>: expected <type>, got <type>` (type names such as `str`, `int`, `NoneType`), `<path>: expected object, got <type>`, `<path>: expected array, got <type>`. Paths look like `data[6].address.city`; for the root use `(root)`.
#
# Validate `data/users_api.json` against the schema below, print `Errors found: <n>` and each error as ` - <error>`, then print the result for one good user document and for the non-object value `[1, 2]`.
