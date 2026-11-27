# T07-E03: Employee class and static methods
#
# Write a class `Employee` with:
#
# - a class attribute `company = "Acme"`;
# - a class attribute `headcount = 0` that increases by one every time an employee is created;
# - an `__init__(name, role, salary)` that stores the three values;
# - a class method `from_string(text)` that builds an employee from text like `"Ben, Tester, 4200"`
#   (strip spaces, convert salary to `int`) and must work with subclasses (use `cls`);
# - a static method `is_working_day(day)` that takes a `datetime.date` and returns `True` for Monday to Friday.
#
# The driver (which uses `from datetime import date`) also shows what happens when you assign `company` on the class versus on one instance.
