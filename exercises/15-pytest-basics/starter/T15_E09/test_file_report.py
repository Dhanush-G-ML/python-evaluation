import pytest

import file_report
from file_report import greet_user, read_names, weather_report, write_report


def test_read_names_strips_spaces(tmp_path):
    names_file = tmp_path / "names.txt"
    names_file.write_text("  Asha \nRavi\n", encoding="utf-8")
    assert read_names(names_file) == ["Asha", "Ravi"]

# TODO: more tmp_path tests (blank lines, comments, missing file, write_report)
# TODO: monkeypatch.setenv / delenv tests for greet_user, using capsys
# TODO: monkeypatch.setattr tests for weather_report, using capsys
