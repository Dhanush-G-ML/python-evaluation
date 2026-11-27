# T03-E10 - Challenge: rotating log file
#
# Write a class `RotatingLog(path, max_lines=10, backups=3)` with a method `write(line)`:
#
# - Each call appends `line` plus a newline to the log file `path`.
# - Before writing, if the file already holds `max_lines` lines, rotate: the current file becomes `<name>.1`, the old `.1` becomes `.2`, and so on. A file that would become `.<backups + 1>` is deleted. Then start a fresh log file.
# - When the object is created for an existing file, it must continue counting from the lines already there.
#
# Main program: empty the folder `output/rotation`, create `RotatingLog("output/rotation/app.log", max_lines=10, backups=3)`, write 45 lines `event 01` to `event 45`, then print for each file in the folder (sorted by name): the name (left-aligned width 10), the number of lines, the first line and the last line, in the format shown.
