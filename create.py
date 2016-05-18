from py2neo import authenticate, Graph, Node

authenticate("localhost:7474", "neo4j", "broccoli")

graph = Graph()

alice = Node("Person", name="Alice")
graph.create(alice)