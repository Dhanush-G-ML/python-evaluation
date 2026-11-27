# Define greet(name) to return a greeting in the format "Hello, Ada!".
# When the file runs as a script, print the greeting for "Ada".


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Ada"))
