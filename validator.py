from scanner import *
from parserr import *

# kod do walidacji
input_string = '''
EquivaleentClasses( :Sdjlfsjdl :A1 :Afsdfs )
'''

print(input_string)
scanner = Scanner(input_string)
print(scanner.tokens)

parserr = Parserr(scanner)
parserr.start()

# EquivalentClasses(
#    :ChildlessPerson 
#    ObjectIntersectionOf(
#      :Person 
#      ObjectComplementOf( :Parent )
#    ) 
# ) 
 
# EquivalentClasses(
#    :MyBirthdayGuests
#    ObjectOneOf( :Bill :John :Mary) 
# )

# SubClassOf( :Sdjlfsjdl :A1 :Afsdfs )