# T10-E01: Singleton: application configuration
#
# **Pattern: Singleton.** Write a class decorator `singleton(cls)` so that calling a decorated class always returns the
# same instance (the first call creates it; arguments of later calls are ignored). The decorator must also add a function
# attribute `reset()` that forgets the instance, which is useful in tests.
#
# Then write `AppConfig` decorated with `@singleton`:
#
# - `__init__(self, env="dev")` stores `env` and an empty dictionary `values`.
# - `set(key, value)` and `get(key, default=None)` read and write `values`.
#
# The driver shows two "different" constructions returning the same object, shared state, and what `reset()` does.
