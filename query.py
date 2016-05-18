from py2neo import authenticate, Graph, Node

authenticate("localhost:7474", "neo4j", "broccoli")

graph = Graph()

result = graph.find_one("Person")
print result