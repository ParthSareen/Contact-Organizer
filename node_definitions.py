from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, Relationship, db)

try:
    db.set_connection('bolt://neo4j:test@localhost:7687')
except Exception as ex:
    print(ex)

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    
    knows = RelationshipTo('Person', 'KNOWS')

class Company(StructuredNode):
    uid = StringProperty(unique_index=True)

