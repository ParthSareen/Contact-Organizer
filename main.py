from neomodel import db
from node_definitions import Person, Company

try:
    db.set_connection('bolt://neo4j:test@localhost:7687')
except Exception as ex:
    print(ex)

Parth = Person(name='Parth').save()
