import re
import os
from sys import argv
from subprocess import call
import Lexer
import Parser

file_path = argv[1]

# Checks that file ends in ".q" extension
if(not re.search(".q$", file_path)):
  print(f"'{file_path}'' is not a valid Q file")
  exit()

# Checks that file exists
if(not os.path.exists(file_path)):
  print(f"File '{file_path}' could not be located")
  exit()

l = Lexer.lexer()
tokens = []

with open(file_path, "r") as src:
  for line in src:
    line = line.strip()
    l.input(line)
    while True:
      tok = l.token()
      if not tok:
        break      # No more input
      tokens.append(tok)

parsed_str = Parser.parse(tokens)

with open("./out.py", "w") as out:
  for ch in parsed_str:
    out.write(ch)

call(["python3", "out.py"])