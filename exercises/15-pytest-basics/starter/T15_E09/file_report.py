"""File, environment and printing helpers. This is the code under test: do not change it."""

import os
from pathlib import Path


def read_names(path):
    """Read a text file with one name per line. Blank lines and lines starting
    with # are ignored; spaces around names are removed."""
    names = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            names.append(line)
    return names


def write_report(path, names):
    """Write a small report (creating folders when needed) and return the line count."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"Total: {len(names)}"] + [f"- {name}" for name in sorted(names)]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


def greet_user():
    """Print a greeting for the user named in the APP_USER environment variable."""
    name = os.environ.get("APP_USER", "guest")
    print(f"Hello, {name}!")


def fetch_temperature(city):
    """Pretend to call a weather web service. It never works inside the exercises."""
    raise ConnectionError("network access is not available")


def weather_report(city):
    """Print and return a one-line weather report for the city."""
    try:
        temperature = fetch_temperature(city)
    except ConnectionError:
        line = f"{city}: unavailable"
    else:
        mood = "warm" if temperature >= 25 else "cool"
        line = f"{city}: {temperature:.1f} C ({mood})"
    print(line)
    return line
