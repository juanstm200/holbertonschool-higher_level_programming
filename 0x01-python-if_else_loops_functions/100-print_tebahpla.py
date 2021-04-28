#!/usr/bin/python3
for i in reversed(range(97, 123)):
  if i % 2:
    print(chr(i - 32), end='')
  else:
    print(chr(i), end='')
