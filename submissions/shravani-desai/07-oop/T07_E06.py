# T07-E06: Shapes: inheritance and polymorphism
#
# Build a small hierarchy:
#
# - `Shape(name)` with an `area()` method that raises `NotImplementedError("Subclasses must implement area()")`
#   and a `describe()` method returning `"<name> with area <area to 2 decimals>"`. `describe()` must call `self.area()`.
# - `Circle(radius)` named `"Circle"`.
# - `Rectangle(width, height, name="Rectangle")`.
# - `Square(side)` that **inherits from `Rectangle`** and is named `"Square"`; it must call `super().__init__`.
#
# Then use the shapes polymorphically: describe each one, find the biggest by area, and sort them.
