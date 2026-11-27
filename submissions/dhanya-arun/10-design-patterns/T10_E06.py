# T10-E06: Template Method: report job
#
# **Pattern: Template Method.** Write an abstract class `ReportJob` whose `run()` method is the template:
#
# 1. record `"load"` in the list `self.steps` and call `self.load()`;
# 2. record `"validate"` and call `self.validate(rows)`;
# 3. record `"format"` and call `self.format_rows(rows)`;
# 4. return the three parts joined by newlines: `self.header()`, the formatted body, `self.footer(rows)`.
#
# `run()` also clears `self.steps` when it starts. `load()` and `format_rows(rows)` are abstract. The hooks have defaults:
# `validate(rows)` returns the rows unchanged, `header()` returns `== <ClassName> ==`, and `footer(rows)` returns
# `(<n> rows)`.
#
# Subclasses:
#
# - `SalesReport`: loads `[("north", 120), ("south", -5), ("east", 80)]`; `validate` drops negative amounts;
#   `format_rows` gives one line per row with the region left-aligned in 6 characters and the amount right-aligned in 5;
#   `footer` returns `Total: <sum>`.
# - `UserReport`: loads `[("Ana", "ana@example.com"), ("Ben", "ben@example.com")]`; lines look like `Ana <ana@example.com>`;
#   `header` returns `-- Registered users --`; keeps the default `footer`.
