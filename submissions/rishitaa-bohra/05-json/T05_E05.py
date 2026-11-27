# T05-E05 - Read an API-style response
#
# `data/users_api.json` imitates the response of a web API: `status`, paging fields and a `data` list of users. Some users have no `address` key, some have `address.city` set to `null`, `last_login` can be `null`, and one user has a `null` email. `data/users_api_error.json` imitates an error response.
#
# Write `extract_users(response)` that returns `response["data"]` when `status` is `"ok"` and otherwise raises `ValueError("API error: <message>")` (use `unknown error` when there is no message). Write `users_table(users)` returning one flat dictionary per user with `id`, `name`, `city` (`"unknown"` when the address or city is missing or null), `domain` (the part of the email after `@`, or `"unknown"` when the email is missing or `null`) and `active`.
#
# Print: `status: <status>, page <page>, total <total>`; the first 8 users as `id` (width 3, right-aligned), a space, `name` (left-aligned width 8), a space, `city`; `Active: <n> of <total>`; `Without a city: <n>`; the e-mail domains with counts (most common first, ties alphabetical) as `  <domain>: <n>`; and finally what happens with the error response (`Error response -> <message>`).
