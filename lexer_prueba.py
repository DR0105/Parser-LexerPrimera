import lexer_rules
from ply.lex import lex
lexer = lex(module=lexer_rules)
f= open ('operaciones.txt','r')
o=f.read()
f.close()
oper=o.splitlines()
i=0
while i<len(oper):
   lexer.input(oper[i])
   token = lexer.token()
   while token is not None:
       print token.type, token.value
       token = lexer.token()
   i=i+1
