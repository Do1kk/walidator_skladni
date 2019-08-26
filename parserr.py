class Parserr:

  ##### Nagłówek parsera #####
  def __init__(self, scanner):
    self.next_token = scanner.next_token
    self.token = self.next_token()

  def take_token(self, token_typ):
    if self.token.typ != token_typ:
      self.error('Oczekiwany token: %(wsad1)s, Otrzymany token: %(wsad2)s' % {'wsad1': token_typ, 'wsad2': self.token.typ})
    if token_typ != 'EOF':
      self.token = self.next_token()

  def error(self, msg):
    raise RuntimeError('Parserr error, %s' % msg)

  ##### Parser #####

  # Symbol startu
  def start(self):
    # start -> Axioms EOF
    if self.token.typ == 'EOF' or self.token.typ == 'STRING' or self.token.typ == 'SubClassOf' or self.token.typ == 'EquivalentClasses' or self.token.typ == 'DisjointClasses' or self.token.typ == 'SameIndividual' or self.token.typ == 'DifferentIndividuals':
      self.Axioms()
      self.take_token('EOF')
    else:
      self.error("Epsilon nie jest dozwolony")
    
  def Axioms(self):
    # <Axioms> ::= <Axiom> | <Axioms> <AxiomOrNull>
    if self.token.typ == 'SubClassOf' or self.token.typ == 'EquivalentClasses' or self.token.typ == 'DisjointClasses' or self.token.typ == 'SameIndividual' or self.token.typ == 'DifferentIndividuals':
      self.Axiom()
      self.Axioms()
    else:
      pass
  
  def Axiom(self):
    # <Axiom> ::= <SubClassOf> | <EquivalentClasses> | <DisjointClasses> | <Assertion>
    if self.token.typ == 'SubClassOf':
      self.SubClassOf()
    elif self.token.typ == 'EquivalentClasses':
      self.EquivalentClasses()
    elif self.token.typ == 'DisjointClasses':
      self.DisjointClasses()
    elif self.token.typ == 'SameIndividual' or self.token.typ == 'DifferentIndividuals':
      self.Assertion()
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def SubClassOf(self):
    # <SubClassOf> ::= 'SubClassOf' <NO> <ClassExpression> <ClassExpression> <NZ>
    if self.token.typ == 'SubClassOf':
      self.take_token('SubClassOf')
      self.take_token('NO')
      self.ClassExpression()
      self.ClassExpression()
      self.take_token('NZ')
      print("SubClassOf OK")
    else:
      self.error("Błąd składni")
  
  def EquivalentClasses(self):
    # <EquivalentClasses> ::= 'EquivalentClasses' <NO> <ClassExpression> <ClassExpression> <multiClassExpression> <NZ>
    if self.token.typ == 'EquivalentClasses':
      self.take_token('EquivalentClasses')
      self.take_token('NO')
      self.ClassExpression()
      self.ClassExpression()
      self.multiClassExpression()
      self.take_token('NZ')
      print("EquivalentClasses OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def DisjointClasses(self):
    # <DisjointClasses> ::= 'DisjointClasses' <NO> <ClassExpression> <ClassExpression> <multiClassExpression> <NZ>
    if self.token.typ == 'DisjointClasses':
      self.take_token('DisjointClasses')
      self.take_token('NO')
      self.ClassExpression()
      self.ClassExpression()
      self.multiClassExpression()
      self.take_token('NZ')
      print("DisjointClasses OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def Assertion(self):
    # <Assertion> ::= <SameIndividual> | <DifferentIndividuals>
    if self.token.typ == 'SameIndividual':
      self.SameIndividual()
    elif self.token.typ == 'DifferentIndividuals':
      self.DifferentIndividuals()
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def SameIndividual(self):
    # <SameIndividual> ::= 'SameIndividual' <NO> <Individual> <Individual> <multiIndividual> <NZ>
    if self.token.typ == 'SameIndividual':
      self.take_token('SameIndividual')
      self.take_token('NO')
      self.Individual()
      self.Individual()
      self.multiIndividual()
      self.take_token('NZ')
      print("SameIndividual OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def DifferentIndividuals(self):
    # <DifferentIndividuals> ::= 'DifferentIndividuals' <NO> <Individual> <Individual> <multiIndividual> <NZ>
    if self.token.typ == 'DifferentIndividuals':
      self.take_token('DifferentIndividuals')
      self.take_token('NO')
      self.Individual()
      self.Individual()
      self.multiIndividual()
      self.take_token('NZ')
      print("DifferentIndividuals OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def ClassExpression(self):
    # <ClassExpression> ::= <ObjectIntersectionOf> | <ObjectUnionOf> | <ObjectComplementOf> | <ObjectOneOf> | <Individual>
    if self.token.typ == 'ObjectIntersectionOf':
      self.ObjectIntersectionOf()
    elif self.token.typ == 'ObjectUnionOf':
      self.ObjectUnionOf()
    elif self.token.typ == 'ObjectComplementOf':
      self.ObjectComplementOf()
    elif self.token.typ == 'ObjectOneOf':
      self.ObjectOneOf()
    elif self.token.typ == 'DW':
      self.Individual()
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def ObjectIntersectionOf(self):
    # <ObjectIntersectionOf> ::= 'ObjectIntersectionOf' <NO> <ClassExpression> <ClassExpression> <multiClassExpression> <NZ> 
    if self.token.typ == 'ObjectIntersectionOf':
      self.take_token('ObjectIntersectionOf')
      self.take_token('NO')
      self.ClassExpression()
      self.ClassExpression()
      self.multiClassExpression()
      self.take_token('NZ')
      print("ObjectIntersectionOf OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def ObjectUnionOf(self):
    # <ObjectUnionOf> ::= 'ObjectUnionOf' <NO> <ClassExpression> <ClassExpression> <mutiClassExpression> <NZ> 
    if self.token.typ == 'ObjectUnionOf':
      self.take_token('ObjectUnionOf')
      self.take_token('NO')
      self.ClassExpression()
      self.ClassExpression()
      self.multiClassExpression()
      self.take_token('NZ')
      print("ObjectUnionOf OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def ObjectComplementOf(self):
    # <ObjectComplementOf> ::= 'ObjectComplementOf' <NO> <ClassExpression> <NZ> 
    if self.token.typ == 'ObjectComplementOf':
      self.take_token('ObjectComplementOf')
      self.take_token('NO')
      self.ClassExpression()
      self.take_token('NZ')
      print("ObjectComplementOf OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def ObjectOneOf(self):
    # <ObjectOneOf> ::= 'ObjectOneOf' <NO> <Individual> <multiIndividual> <NZ> 
    if self.token.typ == 'ObjectOneOf':
      self.take_token('ObjectOneOf')
      self.take_token('NO')
      self.Individual()
      self.multiIndividual()
      self.take_token('NZ')
      print("ObjectOneOf OK")
    else:
      self.error("Epsilon nie jest dozwolony")
  
  def AxiomOrNull(self):
    # <AxiomOrNull> ::= <Axiom> | E 
    if self.token.typ == 'SubClassOf' or self.token.typ == 'EquivalentClasses' or self.token.typ == 'DisjointClasses' or self.token.typ == 'SameIndividual' or self.token.typ == 'DifferentIndividuals':
      self.Axiom()
      print("AxiomOrNull OK")
    else:
      pass
  
  def multiClassExpression(self):
    # <multiClassExpression> ::= E | <ClassExpression> <multiClassExpression>
    if self.token.typ == 'ObjectIntersectionOf' or self.token.typ == 'ObjectUnionOf' or self.token.typ == 'ObjectComplementOf' or self.token.typ == 'ObjectOneOf' or self.token.typ == 'DW':
      self.ClassExpression()
      self.multiClassExpression()
      print("multiClassExpression OK")
    else:
      pass
  
  def multiIndividual(self):
    # <multiIndividual> ::= E | <Individual> <multiIndividual>
    if self.token.typ == 'DW':
      self.Individual()
      self.multiIndividual()
      print("multiIndividual OK")
    else:
      pass

  def Individual(self):
    # <Individual> ::= <DW> <STRING>
    if self.token.typ == 'DW':
      self.take_token('DW')
      self.take_token('STRING')
      print("Individual OK")
    else:
      self.error("Epsilon nie jest dozwolony")
