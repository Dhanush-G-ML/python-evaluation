# T14-E04 - Log to a file and to the console at different levels
#
# Write `setup_logging(log_path)` that configures a logger named `tracker` (level `DEBUG`, `propagate = False`) with two handlers and returns the logger:
#
# - A `StreamHandler` on `sys.stdout`, level `WARNING`, format `%(levelname)s: %(message)s`.
# - A `FileHandler` for `log_path` (create the parent folder, mode `"w"`, UTF-8), level `DEBUG`, format `%(levelname)-8s | %(name)s | %(message)s`.
#
# Write `close_logging(logger)` that closes and removes the handlers, and `run_tasks(logger, tasks)` for a list of `(name, milliseconds, error)` tuples. For each task log `DEBUG` `starting task <name>`. If `error` is not `None`, log `ERROR` `task <name> failed: <error>` and go to the next task. Otherwise log `INFO` `task <name> finished in <ms> ms`, and if it took more than 500 ms also `WARNING` `task <name> was slow (<ms> ms)`. Return the number of failed tasks.
#
# ```python
# TASKS = [
#     ("import users", 120, None),
#     ("resize images", 740, None),
#     ("send emails", 90, "SMTP server timed out"),
#     ("build report", 300, None),
#     ("sync backups", 910, None),
# ]
# ```
#
# In the main program set up logging to `output/tracker.log`, run the tasks, close logging, print `Failed tasks: <n>`, then print `--- output/tracker.log ---` and the content of the file.
