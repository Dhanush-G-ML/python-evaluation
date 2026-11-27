"""Read a JSON inventory file. This is the code under test: do not change it.

The file must hold a list of objects, each with "name" (text), "price" (a number or
a numeric string) and an optional "qty" (a whole number, default 0).
"""

import json
from pathlib import Path


def load_products(path):
    """Return a list of {"name": str, "price": float, "qty": int} dictionaries."""
    text = Path(path).read_text(encoding="utf-8")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON: {error.msg}") from error
    if not isinstance(data, list):
        raise ValueError("top level must be a list")
    products = []
    for index, record in enumerate(data, start=1):
        products.append(_clean_record(index, record))
    return products


def _clean_record(index, record):
    if not isinstance(record, dict):
        raise ValueError(f"record {index}: must be an object")
    for key in ("name", "price"):
        if key not in record:
            raise ValueError(f"record {index}: missing key '{key}'")
    name = str(record["name"]).strip()
    if not name:
        raise ValueError(f"record {index}: name is empty")
    try:
        price = float(record["price"])
    except (TypeError, ValueError):
        raise ValueError(f"record {index}: price is not a number") from None
    if price < 0:
        raise ValueError(f"record {index}: price cannot be negative")
    qty = record.get("qty", 0)
    if isinstance(qty, bool) or not isinstance(qty, int) or qty < 0:
        raise ValueError(f"record {index}: qty must be a whole number, 0 or more")
    return {"name": name, "price": price, "qty": qty}


def total_value(products):
    return round(sum(item["price"] * item["qty"] for item in products), 2)


def load_summary(path):
    products = load_products(path)
    return {
        "count": len(products),
        "units": sum(item["qty"] for item in products),
        "value": total_value(products),
    }
