# T10-E09: Command: text editor with undo and redo
#
# **Pattern: Command.** Build the core of a text editor.
#
# - `Editor` with a string attribute `text`, initially empty.
# - `InsertCommand(editor, position, text)` and `DeleteCommand(editor, start, end)` (deletes `text[start:end]`). Each has
#   `execute()` and `undo()`. A delete must remember the text it removed.
# - `MacroCommand(commands)` runs several commands as one; its `undo()` undoes them in reverse order.
# - `History` with:
#   - `run(command)`: executes the command, stores it, and **clears the redo stack**;
#   - `undo()`: undoes the most recent command; returns `True`, or `False` if there was nothing to undo;
#   - `redo()`: re-executes the most recently undone command; returns `True`, or `False` if nothing can be redone.
