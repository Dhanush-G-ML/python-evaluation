# T07-E05: Thermometer with properties
#
# Write a class `Thermometer(celsius=20.0)` that stores its temperature in a protected attribute `_celsius`.
#
# - `celsius` is a property. Its setter raises `ValueError("Temperature below absolute zero")` for values
#   below `-273.15`. The constructor must go through the same setter.
# - `fahrenheit` is a property with a setter (setting it updates the Celsius value).
# - `kelvin` is a **read-only** property rounded to 2 decimals. Assigning to it raises `AttributeError`.
# - A private counter `self.__reading_count` counts how many times the temperature has been set (including the
#   constructor). Expose it through a read-only property `reading_count`.
