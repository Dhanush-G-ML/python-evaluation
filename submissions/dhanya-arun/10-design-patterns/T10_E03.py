# T10-E03: Strategy: report export formats
#
# **Pattern: Strategy.** Export rows (a list of dictionaries sharing the same keys) in different formats.
#
# - `export_csv(rows)`: header line of keys followed by one line per row, joined with `\n`, no trailing newline.
# - `export_json(rows)`: `json.dumps(rows)`.
# - `export_markdown(rows)`: a Markdown table with a header row, a `| --- | --- |` separator row and one line per row.
# - `STRATEGIES`: dictionary mapping `"csv"`, `"json"`, `"markdown"` to those functions.
# - `ReportExporter(strategy)` with a public attribute `strategy`, an `export(rows)` method that returns `""` for an empty
#   list and otherwise calls the strategy, and a class method `by_name(name)` that builds an exporter from `STRATEGIES`
#   (unknown names raise `ValueError(f"Unknown format: {name}")`).
#
# The driver switches strategy at run time and even passes a `lambda` as a strategy.
