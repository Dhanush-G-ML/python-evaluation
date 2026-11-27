# T06-E10 - Challenge: a tiny template engine
#
# Build a template renderer with `re.sub`. Placeholders look like `{{ name }}`, `{{ user.name }}` (dotted path into nested dictionaries), `{{ name|upper }}` (filters `upper`, `lower`, `title`), and `{{ name|default:text }}` (use `text` when the value is missing). Spaces inside the braces are allowed (`{{ plan | upper }}` works).
#
# Write `find_placeholders(template)` (list of the paths in order of appearance) and `render(template, context)` returning `(text, missing)`: placeholders whose path is missing and that have no `default` filter are left unchanged in the text and their paths are collected in `missing`. A falsy value such as `0` is a real value. Text produced by a replacement is not processed again.
#
# Main program: print the placeholders, the rendered text and the missing list for the template below.
