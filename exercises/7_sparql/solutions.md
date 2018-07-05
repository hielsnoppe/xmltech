# Assignment 7: SPARQL

## Exercise 1

### 1.

Which students have Mary as duo?

    SELECT ?p ?o WHERE {
        student:2345678 ?p ?o.
    }
    ORDER BY (?p)

    SELECT ?studentName WHERE {
        ?mary ns0:name "Mary" ;
              ns0:duo ?student .
        ?student ns0:name ?studentName
    }

Alternative solution

    SELECT ?student WHERE {
        ?student ns0:duo student:2345678 .
    }

### 2.

Which students are registered in UE (mif18, mif17, etc.) or formation http://univ-fu.de/formation#m1if?

    SELECT DISTINCT ?student ?name WHERE {
        ?student ns0:registered ?ue .
        ?student ns0:name ?name .
        ?ue ns0:formation formation:m1if
    }

### 3.

Which pairs of students are registered in the same UE?

    SELECT DISTINCT ?first ?second WHERE {
        ?first ns0:registered ?ue .
        ?second ns0:registered ?ue
    }
    """,

Alternative solution

    SELECT DISTINCT ?s1 ?s2 WHERE{
    ?s1 ns0:duo ?s2.
    {
        {?s1 ns0:registered ?m} UNION
        {?s2 ns0:registered ?m}
    }
    ?m ns0:formation <http://univ-fu.de/formation#m1if>
    }

## Exercise 2

In the following, a RDFS Schema is given.
Based on the given schema, define the following queries in SPARQL.
Please note, there is no namespace given, thus we use `:name-of-property`.

### 1.

The names of the teachers of the course "XML".

    SELECT ?name WHERE {
        ?course :name "XML" ;
                :teached_by ?teacher .
        ?teacher :name ?name
    }

### 2.

The prerequisites (course names) requested for the course "XML".

    SELECT ?name WHERE {
        ?course :name "XML" ;
                :prerequisites ?prereq .
        ?prereq :name ?name .
    }

### 3.

The names of teachers who teach two different courses.

    SELECT ?name WHERE {
        ?first :teached_by ?teacher .
        ?second :teached_by ?teacher .
        ?teacher :name ?name .
        FILTER(?first != ?second) .
    }

### 4.

The names of students taking two different courses of the same teacher.

    SELECT ?name WHERE {
        ?first :teached_by ?teacher .
        ?second :teached_by ?teacher .
        ?student :registered_in ?first ;
                 :registered_in ?second ;
                 :name ?name .
        FILTER(?first != ?second) .
    }
