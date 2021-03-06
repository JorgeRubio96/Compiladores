
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'INT FLOAT STRING ID PLUS MINUS TIMES SLASH LPAREN RPAREN LCURL RCURL SEMICOLON COLON COMMA EQL NEG LSS GTR IFSYM ELSESYM PROGRAMSYM PRINTSYM VARSYM INTSYM FLOATSYMprogram \t: PROGRAMSYM ID SEMICOLON program1 bloqueprogram1\t: vars\n\t\t\t\t| epsilon vars \t\t: VARSYM vars1vars1 \t: vars2 COLON tipo SEMICOLON vars3vars2 \t: ID vars4vars3 \t: vars1\n\t\t\t\t| epsilonvars4 \t: COMMA vars2\n\t\t\t\t| epsilon tipo \t: INTSYM\n\t\t\t\t| FLOATSYMbloque \t: LCURL bloque1 RCURLbloque1 \t: estatuto bloque1\n\t\t\t\t| epsilonestatuto : asignacion\n\t\t\t\t| condicion\n\t\t\t\t| escrituraasignacion : ID EQL expresion SEMICOLONexpresion \t: exp expresion1expresion1 \t: epsilon\n\t\t\t\t\t| expresion2 expexpresion2 \t: LSS\n\t\t\t\t\t| GTR\n\t\t\t\t\t| NEGescritura \t\t: PRINTSYM LPAREN escritura1 RPAREN SEMICOLONescritura1 \t: escritura2 escritura3escritura2 \t: expresion\n\t\t\t\t\t| STRING escritura3 \t: COMMA escritura1\n\t\t\t\t\t| epsilonexp \t: termino exp1 exp1 \t: PLUS termino exp1\n\t\t\t\t| MINUS termino exp1\n\t\t\t\t| epsiloncondicion \t: IFSYM LPAREN expresion RPAREN bloque condicion1 SEMICOLONcondicion1\t: ELSESYM bloque\n\t\t\t\t\t| epsilontermino \t: factor termino1termino1 : TIMES factor termino1\n\t\t\t\t| SLASH factor termino1\n\t\t\t\t| epsilon factor\t: LPAREN expresion RPAREN\n\t\t\t\t| factor1 varcte factor1 : PLUS\n\t\t\t\t| MINUS\n\t\t\t\t| epsilon varcte \t: FLOAT\n\t\t\t\t| INT\n\t\t\t\t| IDepsilon :'
    
_lr_action_items = {'SLASH':([40,65,66,67,68,81,82,83,],[63,-49,-50,-48,-44,63,63,-43,]),'INTSYM':([14,],[27,]),'NEG':([38,40,45,61,62,65,66,67,68,70,71,81,82,83,84,85,91,92,93,94,],[60,-51,-51,-42,-39,-49,-50,-48,-44,-35,-32,-51,-51,-43,-51,-51,-41,-40,-33,-34,]),'VARSYM':([4,],[7,]),'MINUS':([33,34,35,40,43,45,56,58,59,60,61,62,63,64,65,66,67,68,72,73,77,81,82,83,84,85,91,92,],[44,44,44,-51,44,73,44,-24,-23,-25,-42,-39,44,44,-49,-50,-48,-44,44,44,44,-51,-51,-43,73,73,-41,-40,]),'LCURL':([4,5,6,8,10,36,51,52,53,54,88,],[-51,-2,-3,13,-4,-51,-8,-5,-7,13,13,]),'RPAREN':([37,38,40,45,47,48,49,50,55,57,61,62,65,66,67,68,69,70,71,76,78,80,81,82,83,84,85,87,91,92,93,94,],[54,-51,-51,-51,-28,-29,75,-51,-20,-21,-42,-39,-49,-50,-48,-44,83,-35,-32,-27,-31,-22,-51,-51,-43,-51,-51,-30,-41,-40,-33,-34,]),'SEMICOLON':([3,27,28,29,31,38,40,45,46,55,57,61,62,65,66,67,68,70,71,75,79,80,81,82,83,84,85,89,90,91,92,93,94,95,],[4,-11,-12,36,-13,-51,-51,-51,74,-20,-21,-42,-39,-49,-50,-48,-44,-35,-32,86,-51,-22,-51,-51,-43,-51,-51,-38,96,-41,-40,-33,-34,-37,]),'ELSESYM':([31,79,],[-13,88,]),'RCURL':([13,18,19,20,21,22,24,32,74,86,96,],[-51,31,-16,-15,-51,-17,-18,-14,-19,-26,-36,]),'FLOATSYM':([14,],[28,]),'PLUS':([33,34,35,40,43,45,56,58,59,60,61,62,63,64,65,66,67,68,72,73,77,81,82,83,84,85,91,92,],[42,42,42,-51,42,72,42,-24,-23,-25,-42,-39,42,42,-49,-50,-48,-44,42,42,42,-51,-51,-43,72,72,-41,-40,]),'LSS':([38,40,45,61,62,65,66,67,68,70,71,81,82,83,84,85,91,92,93,94,],[59,-51,-51,-42,-39,-49,-50,-48,-44,-35,-32,-51,-51,-43,-51,-51,-41,-40,-33,-34,]),'COLON':([9,11,16,17,30,],[14,-51,-10,-6,-9,]),'PRINTSYM':([13,19,21,22,24,74,86,96,],[26,-16,26,-17,-18,-19,-26,-36,]),'PROGRAMSYM':([0,],[2,]),'$end':([1,12,31,],[0,-1,-13,]),'STRING':([35,77,],[48,48,]),'TIMES':([40,65,66,67,68,81,82,83,],[64,-49,-50,-48,-44,64,64,-43,]),'GTR':([38,40,45,61,62,65,66,67,68,70,71,81,82,83,84,85,91,92,93,94,],[58,-51,-51,-42,-39,-49,-50,-48,-44,-35,-32,-51,-51,-43,-51,-51,-41,-40,-33,-34,]),'EQL':([25,],[34,]),'LPAREN':([23,26,33,34,35,43,56,58,59,60,63,64,72,73,77,],[33,35,43,43,43,43,43,-24,-23,-25,43,43,43,43,43,]),'ID':([2,7,13,15,19,21,22,24,33,34,35,36,39,41,42,43,44,56,58,59,60,63,64,72,73,74,77,86,96,],[3,11,25,11,-16,25,-17,-18,-51,-51,-51,11,-47,66,-45,-51,-46,-51,-24,-23,-25,-51,-51,-51,-51,-19,-51,-26,-36,]),'INT':([33,34,35,39,41,42,43,44,56,58,59,60,63,64,72,73,77,],[-51,-51,-51,-47,65,-45,-51,-46,-51,-24,-23,-25,-51,-51,-51,-51,-51,]),'FLOAT':([33,34,35,39,41,42,43,44,56,58,59,60,63,64,72,73,77,],[-51,-51,-51,-47,67,-45,-51,-46,-51,-24,-23,-25,-51,-51,-51,-51,-51,]),'IFSYM':([13,19,21,22,24,74,86,96,],[23,-16,23,-17,-18,-19,-26,-36,]),'COMMA':([11,38,40,45,47,48,50,55,57,61,62,65,66,67,68,70,71,80,81,82,83,84,85,91,92,93,94,],[15,-51,-51,-51,-28,-29,77,-20,-21,-42,-39,-49,-50,-48,-44,-35,-32,-22,-51,-51,-43,-51,-51,-41,-40,-33,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'vars':([4,],[5,]),'termino1':([40,81,82,],[62,91,92,]),'condicion1':([79,],[90,]),'termino':([33,34,35,43,56,72,73,77,],[45,45,45,45,45,84,85,45,]),'bloque':([8,54,88,],[12,79,95,]),'program1':([4,],[8,]),'tipo':([14,],[29,]),'exp1':([45,84,85,],[71,93,94,]),'estatuto':([13,21,],[21,21,]),'vars3':([36,],[52,]),'vars2':([7,15,36,],[9,30,9,]),'vars1':([7,36,],[10,53,]),'program':([0,],[1,]),'factor':([33,34,35,43,56,63,64,72,73,77,],[40,40,40,40,40,81,82,40,40,40,]),'expresion1':([38,],[55,]),'expresion2':([38,],[56,]),'epsilon':([4,11,13,21,33,34,35,36,38,40,43,45,50,56,63,64,72,73,77,79,81,82,84,85,],[6,16,20,20,39,39,39,51,57,61,39,70,78,39,39,39,39,39,39,89,61,61,70,70,]),'vars4':([11,],[17,]),'condicion':([13,21,],[22,22,]),'escritura1':([35,77,],[49,87,]),'escritura2':([35,77,],[50,50,]),'escritura3':([50,],[76,]),'varcte':([41,],[68,]),'expresion':([33,34,35,43,77,],[37,46,47,69,47,]),'bloque1':([13,21,],[18,32,]),'factor1':([33,34,35,43,56,63,64,72,73,77,],[41,41,41,41,41,41,41,41,41,41,]),'asignacion':([13,21,],[19,19,]),'exp':([33,34,35,43,56,77,],[38,38,38,38,80,38,]),'escritura':([13,21,],[24,24,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAMSYM ID SEMICOLON program1 bloque','program',5,'p_program','scanner_parser_ply.py',97),
  ('program1 -> vars','program1',1,'p_program1','scanner_parser_ply.py',101),
  ('program1 -> epsilon','program1',1,'p_program1','scanner_parser_ply.py',102),
  ('vars -> VARSYM vars1','vars',2,'p_vars','scanner_parser_ply.py',106),
  ('vars1 -> vars2 COLON tipo SEMICOLON vars3','vars1',5,'p_vars1','scanner_parser_ply.py',110),
  ('vars2 -> ID vars4','vars2',2,'p_vars2','scanner_parser_ply.py',113),
  ('vars3 -> vars1','vars3',1,'p_vars3','scanner_parser_ply.py',116),
  ('vars3 -> epsilon','vars3',1,'p_vars3','scanner_parser_ply.py',117),
  ('vars4 -> COMMA vars2','vars4',2,'p_vars4','scanner_parser_ply.py',120),
  ('vars4 -> epsilon','vars4',1,'p_vars4','scanner_parser_ply.py',121),
  ('tipo -> INTSYM','tipo',1,'p_tipo','scanner_parser_ply.py',124),
  ('tipo -> FLOATSYM','tipo',1,'p_tipo','scanner_parser_ply.py',125),
  ('bloque -> LCURL bloque1 RCURL','bloque',3,'p_bloque','scanner_parser_ply.py',128),
  ('bloque1 -> estatuto bloque1','bloque1',2,'p_bloque1','scanner_parser_ply.py',131),
  ('bloque1 -> epsilon','bloque1',1,'p_bloque1','scanner_parser_ply.py',132),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','scanner_parser_ply.py',135),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','scanner_parser_ply.py',136),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','scanner_parser_ply.py',137),
  ('asignacion -> ID EQL expresion SEMICOLON','asignacion',4,'p_asignacion','scanner_parser_ply.py',140),
  ('expresion -> exp expresion1','expresion',2,'p_expresion','scanner_parser_ply.py',143),
  ('expresion1 -> epsilon','expresion1',1,'p_expresion1','scanner_parser_ply.py',146),
  ('expresion1 -> expresion2 exp','expresion1',2,'p_expresion1','scanner_parser_ply.py',147),
  ('expresion2 -> LSS','expresion2',1,'p_expresion2','scanner_parser_ply.py',150),
  ('expresion2 -> GTR','expresion2',1,'p_expresion2','scanner_parser_ply.py',151),
  ('expresion2 -> NEG','expresion2',1,'p_expresion2','scanner_parser_ply.py',152),
  ('escritura -> PRINTSYM LPAREN escritura1 RPAREN SEMICOLON','escritura',5,'p_escritura','scanner_parser_ply.py',156),
  ('escritura1 -> escritura2 escritura3','escritura1',2,'p_escritura1','scanner_parser_ply.py',159),
  ('escritura2 -> expresion','escritura2',1,'p_escritura2','scanner_parser_ply.py',162),
  ('escritura2 -> STRING','escritura2',1,'p_escritura2','scanner_parser_ply.py',163),
  ('escritura3 -> COMMA escritura1','escritura3',2,'p_escritura3','scanner_parser_ply.py',167),
  ('escritura3 -> epsilon','escritura3',1,'p_escritura3','scanner_parser_ply.py',168),
  ('exp -> termino exp1','exp',2,'p_exp','scanner_parser_ply.py',171),
  ('exp1 -> PLUS termino exp1','exp1',3,'p_exp1','scanner_parser_ply.py',174),
  ('exp1 -> MINUS termino exp1','exp1',3,'p_exp1','scanner_parser_ply.py',175),
  ('exp1 -> epsilon','exp1',1,'p_exp1','scanner_parser_ply.py',176),
  ('condicion -> IFSYM LPAREN expresion RPAREN bloque condicion1 SEMICOLON','condicion',7,'p_condicion','scanner_parser_ply.py',180),
  ('condicion1 -> ELSESYM bloque','condicion1',2,'p_condicion1','scanner_parser_ply.py',184),
  ('condicion1 -> epsilon','condicion1',1,'p_condicion1','scanner_parser_ply.py',185),
  ('termino -> factor termino1','termino',2,'p_termino','scanner_parser_ply.py',188),
  ('termino1 -> TIMES factor termino1','termino1',3,'p_termono1','scanner_parser_ply.py',192),
  ('termino1 -> SLASH factor termino1','termino1',3,'p_termono1','scanner_parser_ply.py',193),
  ('termino1 -> epsilon','termino1',1,'p_termono1','scanner_parser_ply.py',194),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','scanner_parser_ply.py',198),
  ('factor -> factor1 varcte','factor',2,'p_factor','scanner_parser_ply.py',199),
  ('factor1 -> PLUS','factor1',1,'p_factor1','scanner_parser_ply.py',203),
  ('factor1 -> MINUS','factor1',1,'p_factor1','scanner_parser_ply.py',204),
  ('factor1 -> epsilon','factor1',1,'p_factor1','scanner_parser_ply.py',205),
  ('varcte -> FLOAT','varcte',1,'p_varcte','scanner_parser_ply.py',209),
  ('varcte -> INT','varcte',1,'p_varcte','scanner_parser_ply.py',210),
  ('varcte -> ID','varcte',1,'p_varcte','scanner_parser_ply.py',211),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','scanner_parser_ply.py',215),
]
