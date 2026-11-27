# T09-E06: Walk a directory tree
#
# A folder is modelled as a dictionary: values that are dictionaries are sub-folders and values that are integers
# are file sizes in bytes. Use the `TREE` below and write recursive functions:
#
# - `tree_lines(tree, depth=0)`: a list of lines for a printable tree. Folders end with `/`, files show their size in
#   brackets, and each level is indented by two spaces.
# - `total_size(tree)`: sum of all file sizes in the tree.
# - `count_files(tree)`: number of files.
# - `find_files(tree, extension, prefix="")`: list of full paths (joined with `/`, starting at the top folder name)
#   of files whose name ends with `extension`, in tree order.
# - `folder_depth(tree)`: number of folder levels; the top-level dictionary counts as one level and an empty folder as one level.
