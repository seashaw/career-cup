#!/usr/bin/env python3
"""
http://www.careercup.com/question?id=5654062512996352

Write a program that deletes every 5th byte from a file, but without using a
temporary file or allocating a buffer in the memory. For adjusting the size
of the file you may use the truncate function.
"""
byte_array = []
with open("file", "rb") as in_file:
    for i in range(len(in_file.peek())):
        if not i % 5 == 0:
            byte_array.append(in_file.read(1))
        in_file.seek(i)
with open("file", "wb") as out_file:
    for i in byte_array:
        out_file.write(i)
    out_file.write(b'\n')

"""
Solution uses a list to store bytes from file.
Is this considered a buffer?
"""
