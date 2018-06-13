import rdflib
import rdfextras
rdfextras.registerplugins()

filename = "exercise1.rdf"

g = rdflib.Graph()
g.parse(filename)

preamble = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ns0: <http://univ-fu.de#>
PREFIX ue: <http://univ-fu.de/ue#>
PREFIX formation: <http://univ-fu.de/formation#>
PREFIX student: <http://univ-fu.de/student#>
"""

queries = {

0: """
SELECT ?p ?o WHERE {
    student:2345678 ?p ?o.
}
ORDER BY (?p)
""",

1.1: """
SELECT ?s WHERE {
    ?s ns0:duo student:2345678 .
}
""",

1.2: """
SELECT ?student ?name WHERE {
    ?student ns0:registered ?ue .
    ?student ns0:name ?name .
    ?ue ns0:formation formation:m1if
}
""",

1.3: """
SELECT DISTINCT ?first ?second WHERE {
    ?first ns0:registered ?ue .
    ?second ns0:registered ?ue
}
""",

2.1: """

""",

2.2: """
""",

2.3: """
""",

2.4: """
"""
}

query = preamble + queries[1.3]
print(query)
results = g.query(query)

for row in results:
    print("%s %s" % row)
