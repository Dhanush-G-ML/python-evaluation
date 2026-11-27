# T03-E08 - Binary basics
#
# Work with binary files in the `output/` folder:
#
# 1. Write the 256 byte values `0..255` (`bytes(range(256))`) to `output/bytes.bin` and print the file size.
# 2. Write `read_in_chunks(path, size)`, a generator that yields chunks of at most `size` bytes. Print the list of chunk lengths for size 100.
# 3. Print the first 4 bytes as hex.
# 4. Write `sha256_of_file(path)` (read in chunks) and print the hash.
# 5. Write `copy_file(src, dst)` using chunks and print whether the hashes of source and copy are equal.
# 6. With `struct`, write `pack_ints(path, values)` (little-endian unsigned 32-bit) and `unpack_ints(path)`; pack `[1, 256, 65535]`, print the raw bytes and the unpacked list.
