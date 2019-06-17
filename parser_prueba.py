import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)
f= open ('operaciones.txt','r')
o=f.read()
f.close()
oper=o.splitlines()
i=0
while i<len(oper):
   print(oper[i]),
   print "= ",
   print(parser.parse(oper[i], lexer))
   i=i+1

