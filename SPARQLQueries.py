__author__ = '22208_65138'

from rdflib.graph import ConjunctiveGraph, Namespace

def predicateCount (graph, namespace, predicate):
    ns = Namespace(namespace)
    results = graph.query("""
                PREFIX pf: <http://xmlns.com/gah/0.1/>
                SELECT pf:accidentID (COUNT(?p) as ?pCount)
                WHERE{
                    ?s pf:accidentID  ?o.
                }GROUP BY ?p
                """)
    #, \
    #          initNs={'pf':ns})
    print (results)

def predicateCount1 (graph, namespace, predicate):
    ns = Namespace(namespace)
    results = graph.query("""
                SELECT (COUNT(?p) as ?pCount)
                WHERE{
                    ?s ?p  ?o.
                }GROUP BY ?p
                """)
    #, \
    #          initNs={'pf':ns})
    print (results)




