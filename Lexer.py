from lib.plymaster.ply import lex

def lexer():
  tokens = ('NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV','RPAREN', 'LPAREN', 'RBRAC', 'LBRAC', 'STRING')
  t_DIV  = r'/'
  t_LPAREN  = r'\('
  t_RPAREN  = r'\)'
  t_RBRAC = r'\}'
  t_LBRAC  =r'\{'

  def t_NUMBER(t):
      r'\d+'
      t.value = int(t.value)
      return t


  def t_STRING(t):
    r'\".+\"'
    t.value = str(t.value[1:-1])
    return t

  def t_newline(t):
    r'\;'
    t.lexer.lineno += len(t.value)

  t_ignore  = ' \t'

  def t_error(t):
      print("Illegal character '%s'" % t.value[0])
      t.lexer.skip(1)

  return lex.lex()

