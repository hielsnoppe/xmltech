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
SELECT ?studentName WHERE {
    ?mary ns0:name "Mary" ;
          ns0:duo ?student .
    ?student ns0:name ?studentName
}
""",

1.12: """
SELECT ?student WHERE {
    ?student ns0:duo student:2345678 .
}
""",

1.2: """
SELECT DISTINCT ?student ?name WHERE {
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

1.31: """
SELECT DISTINCT ?s1 ?s2 WHERE{
?s1 ns0:duo ?s2.
{
    {?s1 ns0:registered ?m} UNION
    {?s2 ns0:registered ?m}
}
?m ns0:formation <http://univ-fu.de/formation#m1if>
}
""",

2.1: """
SELECT ?name WHERE {
    ?course :name "XML" ;
            :teached_by ?teacher .
    ?teacher :name ?name
}
""",

2.2: """
SELECT ?name WHERE {
    ?course :name "XML" ;
            :prerequisites ?prereq .
    ?prereq :name ?name .
}
""",

2.3: """
SELECT ?name WHERE {
    ?first :teached_by ?teacher .
    ?second :teached_by ?teacher .
    ?teacher :name ?name .
    FILTER(?first != ?second) .
}
""",

2.4: """
SELECT ?name WHERE {
    ?first :teached_by ?teacher .
    ?second :teached_by ?teacher .
    ?student :registered_in ?first ;
             :registered_in ?second ;
             :name ?name .
    FILTER(?first != ?second) .
}
"""
}

query = preamble + queries[1.31]
print(query)
results = g.query(query)

for row in results:
    print("%s %s" % row)
    #print("%s" % row)
