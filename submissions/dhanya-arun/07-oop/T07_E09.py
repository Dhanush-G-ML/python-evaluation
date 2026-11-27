# T07-E09: Payroll with abstract base classes
#
# Model a payroll system.
#
# - `Employee(ABC)` created with `name`. It declares an abstract property `kind` and an abstract method
#   `monthly_pay()`, and has a concrete `payslip()` returning `"<name> (<kind>): <pay to 2 decimals>"`.
# - `SalariedEmployee(name, annual_salary)`: kind `"salaried"`, pay is `annual_salary / 12`.
# - `HourlyEmployee(name, rate, hours)`: kind `"hourly"`. The first 160 hours are paid at `rate`; hours above 160
#   are paid at 1.5 times `rate`.
# - `CommissionEmployee(name, base, sales, rate)`: kind `"commission"`, pay is `base + sales * rate`.
# - `Payroll(employees)` with `total()` and `report()` (one payslip per line, then `TOTAL: <total to 2 decimals>`).
#
# Trying to instantiate `Employee` directly must raise `TypeError`; the driver prints a fixed message when it does.
