import collections
import re

Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])

class Scanner:

  def __init__(self, input):
    self.tokens = []
    self.current_token_number = 0
    for token in self.tokenize(input):
	    self.tokens.append(token)
 
  def tokenize(self, input_string):
    keywords = {'SubClassOf', 'EquivalentClasses', 'DisjointClasses', 'SameIndividual', 'DifferentIndividuals', 
                'ObjectIntersectionOf', 'ObjectUnionOf', 'ObjectComplementOf', 'ObjectOneOf', 'EOF'}
    token_specification = [
        ('DW',      r':'),              # dwukropek
        ('NO',      r'[(<]'),           # nawias otwarty
        ('NZ',      r'[)>]'),           # nawias zamknięty
        ('STRING',  r'[A-Za-z\d+]+'),   # nazwa, znak i liczba
        ('NL',      r'\n'),             # następna linia
        ('SKIP',    r'[ \t]'),          # spacja albo tabulator
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line_number = 1
    current_position = line_start = 0
    match = get_token(input_string)
    while match is not None:
        typ = match.lastgroup
        if typ == 'NL':
            line_start = current_position
            line_number += 1
        elif typ != 'SKIP':
            value = match.group(typ)
            if typ == 'STRING' and value in keywords:
                typ = value
            yield Token(typ, value, line_number, match.start()-line_start)
        current_position = match.end()
        match = get_token(input_string, current_position)
    if current_position != len(input_string):
        raise RuntimeError('Error: Nieoczekiwany znak %r w lini %d' % \
                              (input_string[current_position], line_number))
    yield Token('EOF', '', line_number, current_position-line_start)

  def next_token(self):
    self.current_token_number += 1
    if self.current_token_number-1 < len(self.tokens):
      return self.tokens[self.current_token_number-1]
    else:
      raise RuntimeError('Error: Nie ma więcej tokenów')

