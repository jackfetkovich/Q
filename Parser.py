from Reserved import reserved as r

def parse(tokens):
  vars = {}
  parsed_str = ''
  for i in range(len(tokens)):

    # CHECKING FOR OUT STATEMENTS
    if tokens[i].type == "OUT":
      if tokens[i + 1].type == "LPAREN" and tokens[i+3].type == "RPAREN":
        if tokens[i+2].type == "STRING": 
          parsed_str += f"print('{tokens[i+2].value}')\n"
        elif tokens[i+2].type == "ID" and tokens[i+2].value in vars:
          parsed_str += f"print('{vars.get(tokens[i+2].value)}')\n"

    if tokens[i].type == "WHEREAS":
      if tokens[i+1].type == "ID" and tokens[i+2].type == "DEC" and (tokens[i+3].type == "NUMBER" or tokens[i+3].type == "STRING"):
        vars[tokens[i+1].value] = tokens[i+3].value

  return parsed_str
