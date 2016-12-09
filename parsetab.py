
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '7BA2D83AF885C8E7626F0CCB26873B35'
    
_lr_action_items = {'RBRACE':([26,28,30,31,47,49,57,68,],[37,-24,41,-21,-23,-20,-25,-22,]),'FILENAME':([0,],[2,]),'AUTHOR':([3,],[4,]),'COMMA':([28,31,43,48,57,68,],[39,42,50,58,-25,-22,]),'$end':([1,12,14,37,41,],[0,-2,-1,-19,-18,]),'LPAREN':([11,22,27,29,],[17,33,38,40,]),'ICONST':([6,18,19,33,35,38,39,40,42,45,50,52,54,55,58,62,69,],[7,27,29,43,44,46,27,48,29,55,60,55,55,-17,64,67,-14,]),'LBRACKET':([20,24,32,53,54,55,63,65,66,],[-8,35,-7,62,-16,-17,-15,-10,-9,]),'RPAREN':([25,46,59,60,64,],[36,57,65,66,68,]),'KCONST':([17,],[25,]),'INSTRUMENT':([5,],[6,]),'FCONST':([50,],[59,]),'SONG':([7,],[10,]),'NCONST':([16,20,23,51,65,66,],[22,22,22,-6,-10,-9,]),'LBRACE':([13,15,],[18,19,]),'STRUCTURE':([8,9,21,23,34,51,52,56,61,69,],[13,15,-3,-5,-4,-6,-13,-11,-12,-14,]),'SCONST':([2,4,],[3,5,]),'IMPROVISATION':([7,],[11,]),'COLON':([10,36,],[16,45,]),'RBRACKET':([44,67,],[51,69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'principal':([0,],[1,]),'degrees':([45,52,],[53,53,]),'repeatValuesImprovisation':([18,39,],[28,28,]),'repeatSong':([19,42,],[30,49,]),'improv':([7,],[8,]),'note':([16,20,23,],[20,20,20,]),'repeatImprovisation':([18,39,],[26,47,]),'notes':([16,20,23,],[24,32,24,]),'degreeLines':([45,52,],[56,61,]),'song':([7,],[9,]),'structureSong':([9,],[14,]),'structureImprovisation':([8,],[12,]),'notesLine':([16,23,],[23,23,]),'repeatValuesSong':([19,42,],[31,31,]),'degree':([45,52,54,],[54,54,63,]),'notesLines':([16,23,],[21,34,]),'degreeLine':([45,52,],[52,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> principal","S'",1,None,None,None),
  ('principal -> FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST song structureSong','principal',8,'p_principal','AnalizadorSintactico.py',38),
  ('principal -> FILENAME SCONST AUTHOR SCONST INSTRUMENT ICONST improv structureImprovisation','principal',8,'p_principal2','AnalizadorSintactico.py',47),
  ('song -> SONG COLON notesLines','song',3,'p_song','AnalizadorSintactico.py',57),
  ('notesLines -> notesLine notesLines','notesLines',2,'p_notesLines','AnalizadorSintactico.py',63),
  ('notesLines -> notesLine','notesLines',1,'p_notesLines2','AnalizadorSintactico.py',67),
  ('notesLine -> notes LBRACKET ICONST RBRACKET','notesLine',4,'p_notesLine','AnalizadorSintactico.py',72),
  ('notes -> note notes','notes',2,'p_notes','AnalizadorSintactico.py',79),
  ('notes -> note','notes',1,'p_notes2','AnalizadorSintactico.py',83),
  ('note -> NCONST LPAREN ICONST COMMA ICONST RPAREN','note',6,'p_note','AnalizadorSintactico.py',88),
  ('note -> NCONST LPAREN ICONST COMMA FCONST RPAREN','note',6,'p_note2','AnalizadorSintactico.py',103),
  ('improv -> IMPROVISATION LPAREN KCONST RPAREN COLON degreeLines','improv',6,'p_improv','AnalizadorSintactico.py',119),
  ('degreeLines -> degreeLine degreeLines','degreeLines',2,'p_degreeLines','AnalizadorSintactico.py',136),
  ('degreeLines -> degreeLine','degreeLines',1,'p_degreeLines2','AnalizadorSintactico.py',140),
  ('degreeLine -> degrees LBRACKET ICONST RBRACKET','degreeLine',4,'p_degreeLine','AnalizadorSintactico.py',145),
  ('degrees -> degree degree','degrees',2,'p_degrees','AnalizadorSintactico.py',151),
  ('degrees -> degree','degrees',1,'p_degrees2','AnalizadorSintactico.py',155),
  ('degree -> ICONST','degree',1,'p_degree','AnalizadorSintactico.py',160),
  ('structureSong -> STRUCTURE LBRACE repeatSong RBRACE','structureSong',4,'p_structureSong','AnalizadorSintactico.py',166),
  ('structureImprovisation -> STRUCTURE LBRACE repeatImprovisation RBRACE','structureImprovisation',4,'p_structureImprovisation','AnalizadorSintactico.py',170),
  ('repeatSong -> repeatValuesSong COMMA repeatSong','repeatSong',3,'p_repeatSong','AnalizadorSintactico.py',175),
  ('repeatSong -> repeatValuesSong','repeatSong',1,'p_repeat2Song','AnalizadorSintactico.py',179),
  ('repeatValuesSong -> ICONST LPAREN ICONST COMMA ICONST RPAREN','repeatValuesSong',6,'p_repeatValuesSong','AnalizadorSintactico.py',184),
  ('repeatImprovisation -> repeatValuesImprovisation COMMA repeatImprovisation','repeatImprovisation',3,'p_repeatImprovisation','AnalizadorSintactico.py',191),
  ('repeatImprovisation -> repeatValuesImprovisation','repeatImprovisation',1,'p_repeat2Improvisation','AnalizadorSintactico.py',195),
  ('repeatValuesImprovisation -> ICONST LPAREN ICONST RPAREN','repeatValuesImprovisation',4,'p_repeatValuesImprovisation','AnalizadorSintactico.py',200),
]
