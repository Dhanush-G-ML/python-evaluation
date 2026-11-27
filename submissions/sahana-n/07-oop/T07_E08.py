# T07-E08: Composition: cars and stacks
#
# Part A. Write `PetrolEngine` and `ElectricEngine`, each with `start()` and `refuel()` methods returning
# different strings (`"Petrol engine roars"` / `"Filling the tank"` and `"Electric motor hums"` / `"Charging the battery"`).
# Write `Car(model, engine)` which **has an** engine: `start()` and `refuel()` return `"<model>: <engine text>"`,
# and `swap_engine(new_engine)` replaces the engine at run time.
#
# Part B. Write `Stack` that stores items in a private list `_items` (composition) and offers only `push`, `pop`
# (raising `IndexError("pop from empty stack")` when empty), `peek` and `len()`. Also write `LeakyStack(list)`
# (inheritance) with a `push` method to see the difference: the leaky version exposes list methods such as `insert`.
