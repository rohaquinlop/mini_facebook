from neo4j import GraphDatabase
from db_config import driver

class PersonsRepository(object):

    def add_person(self, name, age):
        with driver.session() as session:
            result = session.run("CREATE (p:Person{name:'" + name + "', age:" + str(age) + "}) RETURN p.name as name, p.age as age").data()
            return result

    def get_all_persons(self):
        with driver.session() as session:
            result = session.run("MATCH (n:Person) RETURN n.name as name LIMIT 25").data()
            return result

    def get_person_by_name(self, name):
        with driver.session() as session:
            result = session.run("MATCH (p:Person{name:'{0}'}) RETURN p.name as name".format(name)).data()
            return result

    def get_friends(self, name):
        with driver.session() as session:
            result = session.run("MATCH (p:Person{name:'" + name + "'})-[:FRIEND]->(fof) RETURN fof.name as name, fof.age as age").data()
            return result

    def get_friends_from_my_friends(self, name):
        with driver.session() as session:
            result = session.run("MATCH (p:Person{name:'" + name + "'})-[:FRIEND]->(f)-[:FRIEND]->(fof) RETURN fof.name as name, fof.age as age").data()
            return result

    def delete_from_my_friends(self, name1, name2):
        with driver.session() as session:
            result = session.run("MATCH (p1:Person{name:'" + name1 + "'})-[f:FRIEND]->(p2:Person{name:'" + name2 + "'}) DELETE f").data()
            return result
    
    def make_friend(self, name1, name2):
        with driver.session() as session:
            result = session.run("MATCH (p1:Person{name:'" + name1 + "'})\nMATCH (p2:Person{name:'" + name2 + "'})\nCREATE (p1)-[:FRIEND]->(p2)").data()
            return result