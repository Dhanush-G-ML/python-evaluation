# T15-E09 - tmp_path, monkeypatch and capsys
#
# Tests must not depend on files lying around, on your environment variables, on the network, or on what the program prints to the screen. pytest has built-in fixtures for all four.
#
# Part A - `tmp_path`. It is a fresh temporary folder (a `pathlib.Path`) for each test. Test:
#
# 1. `read_names` strips spaces around names (given).
# 2. `read_names` skips blank lines and lines starting with `#`.
# 3. `read_names` of a missing file raises `FileNotFoundError`.
# 4. `write_report(tmp_path / "out" / "deep" / "report.txt", ["Ravi", "Asha"])` creates the folders, returns 3 (lines written), and the file contains exactly `"Total: 2\n- Asha\n- Ravi\n"` (names sorted).
# 5. A report written by `write_report` can be read back with `read_names` (comments are not special here: `Total: 2`, `- Asha`, `- Ravi`).
#
# Part B - `monkeypatch` and `capsys` for the environment. `greet_user()` prints a greeting for the user in the environment variable `APP_USER`. `capsys.readouterr()` returns what was printed so far (`.out`, `.err`). Test that with `monkeypatch.setenv("APP_USER", "Asha")` it prints `Hello, Asha!` and that with `monkeypatch.delenv("APP_USER", raising=False)` it prints `Hello, guest!`.
#
# Part C - `monkeypatch.setattr` to replace a function. `weather_report(city)` calls `fetch_temperature(city)`, which always fails with `ConnectionError` here (it pretends to call a web service). Test:
#
# 1. Without any patching, `weather_report("Pune")` returns `"Pune: unavailable"` and prints the same line.
# 2. With `monkeypatch.setattr(file_report, "fetch_temperature", lambda city: temperature)` parametrized for `31.04`, `25` and `24.9`: the result is `Pune: 31.0 C (warm)`, `Pune: 25.0 C (warm)`, `Pune: 24.9 C (cool)`, and the printed output equals the result plus a newline.
# 3. A test that, without patching, `file_report.fetch_temperature("Pune")` still raises `ConnectionError`: monkeypatch changes are undone after every test.
#
# Patch the name where the code under test looks it up: `weather_report` calls `fetch_temperature` from its own module, so patch `file_report.fetch_temperature`.
#
# Behaviours to test
#
# | Fixture | What to check |
# |---------|---------------|
# | `tmp_path` | reading with blanks and comments, missing file, writing creates folders, exact file content |
# | `monkeypatch.setenv` / `delenv` | greeting uses the variable, default is `guest` |
# | `capsys` | what `print` wrote, compared with `capsys.readouterr().out` |
# | `monkeypatch.setattr` | the weather lines for warm, borderline and cool values, no real network use |
