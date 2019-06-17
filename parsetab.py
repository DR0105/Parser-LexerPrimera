
# parsetab.py
# This file is automatically generated. Do not edit.

_lr_method = 'LALR'

_lr_signature = '\x8d6\x93\xc7\x8cW\x12\x05V\x8d\xef\xde\x00w\xa5X'

_lr_action_items = {'DIVISION':([1,2,4,11,12,13,14,15,],[6,-7,-6,-5,-4,-8,6,6,]),'RPAREN':([1,2,4,8,11,12,13,14,15,],[-3,-7,-6,13,-5,-4,-8,-1,-2,]),'NUMBER':([0,3,6,7,9,10,],[2,2,2,2,2,2,]),'TIMES':([1,2,4,11,12,13,14,15,],[7,-7,-6,-5,-4,-8,7,7,]),'PLUS':([1,2,4,5,8,11,12,13,14,15,],[-3,-7,-6,9,9,-5,-4,-8,-1,-2,]),'LPAREN':([0,3,6,7,9,10,],[3,3,3,3,3,3,]),'MINUS':([1,2,4,5,8,11,12,13,14,15,],[-3,-7,-6,10,10,-5,-4,-8,-1,-2,]),'$end':([1,2,4,5,11,12,13,14,15,],[-3,-7,-6,0,-5,-4,-8,-1,-2,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,3,9,10,],[1,1,14,15,]),'expression':([0,3,],[5,8,]),'factor':([0,3,6,7,9,10,],[4,4,11,12,4,4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('expression',3,'p_expression_plus','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',5),
  ('expression',3,'p_expression_minus','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',9),
  ('expression',1,'p_expression_term','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',13),
  ('term',3,'p_term_times','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',17),
  ('term',3,'p_term_division','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',21),
  ('term',1,'p_term_factor','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',25),
  ('factor',1,'p_factor_num','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',29),
  ('factor',3,'p_factor_expr','C:\\Users\\DIEGO ROMERO\\Downloads\\lexer_parser-master\\parser_rules.py',33),
]