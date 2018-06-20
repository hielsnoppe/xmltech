# Assignment 8: SPARQL on Knowledge Graphs

## Exercise 1: SPARQL on DBpedia

[DBpedia](http://dbpedia.org/sparql)

See also [How to reference a page that contains parenthesis in SPARQL](https://stackoverflow.com/questions/31384952/how-to-reference-a-page-that-contains-parenthesis-in-sparql) on StackOverflow

### 1

    SELECT ?iri WHERE {
        ?iri rdf:type <http://dbpedia.org/ontology/Restaurant>
    }
    LIMIT 100


### 2

    SELECT ?label WHERE {
        <http://dbpedia.org/resource/Da_Vinci_(restaurant)> rdfs:label ?label .
        FILTER (lang(?label) = 'en')
    }


### 3

    SELECT ?label WHERE {
        ?chef
            rdf:type <http://dbpedia.org/ontology/Chef> ;
            rdfs:label ?label .
        FILTER (lang(?label) = 'en')
    }
    LIMIT 100


### 4

    SELECT DISTINCT ?prop WHERE {
        <http://dbpedia.org/resource/Da_Vinci_(restaurant)> ?prop ?p
    }

### 5

    SELECT ?s WHERE {
        <http://dbpedia.org/resource/Da_Vinci_(restaurant)>
            dbo:address ?address ;
            dbp:city/rdfs:label ?city ;
            dbp:country/rdfs:label ?country .

        FILTER (lang(?address) = 'en')
        FILTER (lang(?city) = 'en')
        FILTER (lang(?country) = 'en')

        BIND(CONCAT(?address, " - ", ?city, " - " , ?country) as ?s)
    }

## Exercise 2: SPARQL on LinkedMDB

[LinkedMDB](http://data.linkedmdb.org/snorql)

### 1

    SELECT ?title WHERE {
        ?movie a movie:film ;
            dc:date "1989-03-24" ;
            dc:title ?title .
    }

### 2

    SELECT ?title WHERE {
        ?movie a movie:film ;
            dc:title ?title ;
            movie:actor ?actor .
        ?actor movie:actor_name "Jane Fonda" .
    }

## Exercise 3: SPARQL on Wikidata

[WikiData](https://query.wikidata.org/)

### a

    SELECT ?item WHERE {
        ?item ?label "window"@en .
    }

Results

* http://www.wikidata.org/entity/Q35473
* http://www.wikidata.org/entity/Q387318
* http://www.wikidata.org/entity/Q835016
* http://www.wikidata.org/entity/Q1361753

### b

    SELECT DISTINCT ?property ?value WHERE {
        wd:Q35473 ?property ?value .
    }
