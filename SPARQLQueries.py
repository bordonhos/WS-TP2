__author__ = '22208_65138'

from rdflib.graph import ConjunctiveGraph, Namespace, rdflib

def predicateCount (graph, namespace, predicate):
    ns = Namespace(namespace)
    qry = "SELECT (COUNT(pf:" + predicate + ") as ?pCount) " \
         " WHERE {" \
         "?s pf:" + predicate + " ?o ." \
         "    } "

    results = graph.query( qry, initNs={'pf':ns})
    return results

def listTypes (graph, namespace, type):
    ns = Namespace(namespace)
    qry = "SELECT ?Descricao ( Count (*) as ?count) " \
            " WHERE {" \
            " ?s pf:" + type + " ?Tipo . " \
            " ?Tipo pf:description ?Descricao ." \
            "}" \
            "GROUP BY ?Descricao " \
            "ORDER BY DESC (?count)"
    results = graph.query( qry, initNs={'pf':ns})
    return results


def accidentData (graph, namespace, accidentID):
    ns = Namespace(namespace)
    qry = 'SELECT ?idAcidente ?descVeiculo ?descCausa ?descHora ?descLocal (count (?idVitima) as ?nVitimas) ' \
    'WHERE{ ' \
    '?idAcidente pf:accidentID "' + accidentID + '"^^<http://www.w3.org/2001/XMLSchema#int>. ' \
    '?idAcidente pf:hasAccVehicle ?idtipoVeiculo. ' \
    '?idtipoVeiculo pf:description ?descVeiculo. ' \
    '?idAcidente pf:hasAccCause ?idCausa. ' \
    '?idCausa pf:description ?descCausa. ' \
    '?idAcidente pf:happenedDuring ?idHora. ' \
    '?idHora pf:description ?descHora. ' \
    '?idAcidente pf:happenedDuring ?idHora. ' \
    '?idHora pf:description ?descHora. ' \
    '?idAcidente pf:happenedInRoadNet ?idLocal. ' \
    '?idLocal pf:description ?descLocal. ' \
    '?idAcidente pf:hasVictim ?idVitima. ' \
    '}' \
    'GROUP BY ?idAcidente ?descVeiculo ?descCausa ?descHora ?descLocal'
    results = graph.query( qry, initNs={'pf':ns})
    return results

def  victimData (graph, namespace, victimID):
    ns = Namespace(namespace)
    qry = 'SELECT ?idVitima ?descIdade ?descVeiculo ?descVitima ?idAcidente ?objAcidente ' \
        'WHERE{ ' \
        '?idVitima pf:victimID "' + victimID + '"^^<http://www.w3.org/2001/XMLSchema#int>. ' \
        '?idVitima pf:hasVictimAge ?idtipoIdade. ' \
        '?idtipoIdade pf:description ?descIdade. ' \
        '?idVitima pf:inVehicle ?idtipoveiculo. ' \
        '?idtipoveiculo pf:description ?descVeiculo. ' \
        '?idVitima pf:hasVictimType ?idtipoVitima. ' \
        '?idtipoVitima pf:description ?descVitima. ' \
        '?idVitima pf:involvedIn ?idAcidente. ' \
        '?idAcidente pf:accidentID ?objAcidente.'\
        '}'
    results = graph.query( qry, initNs={'pf':ns})
    return results

def accidentVictimAge (graph, namespace, accidentID):
    ns = Namespace(namespace)
    qry = 'SELECT  ?vitima ?descIdade ' \
    'WHERE{ ' \
    '?idAcidente pf:accidentID "' + accidentID + '"^^<http://www.w3.org/2001/XMLSchema#int>. ' \
    '?idAcidente pf:hasVictim ?idVitima. ' \
    '?idVitima pf:victimID ?vitima. ' \
    '?idVitima pf:hasVictimAge ?idtipoIdade. ' \
    '?idtipoIdade pf:description ?descIdade. ' \
    '}'

    results = graph.query( qry, initNs={'pf':ns})
    return results

def accidentsByType (graph, namespace, predicate, value ):
    ns = Namespace(namespace)

    qry = 'SELECT  ?acidente ' \
        'WHERE{ ' \
        '?id pf:description "' + value +'". ' \
        '?idAcidente pf:' +predicate + ' ?id . ' \
        '?idAcidente pf:accidentID ?acidente . ' \
        '}'
    results = graph.query( qry, initNs={'pf':ns})
    return results

def underageDriver(graph, namespace):
    ns = Namespace(namespace)

    qry = """
            SELECT  ?victimID
            WHERE{
            ?accidentVictim pf:victimID ?victimID.
            ?accidentVictim pf:hasVictimAge <http://ws_22208_65138.com/VictimAge/Y0-17> .
            ?accidentVictim pf:hasVictimType <http://ws_22208_65138.com/VictimType/Driver> .
            }
            """
    results = graph.query( qry, initNs={'pf':ns})
    return results

def happenedDuring(graph, namespace):
    ns = Namespace(namespace)
    results = graph.query("""
                SELECT ?roadaccident ?happenedDuring
                WHERE{
                ?roadaccident pf:happenedDuring ?happenedDuring.
                } 
                    """, \
                          initNs={'pf':ns})
    return results

def hasVictimUnderage(graph, namespace):
    ns = Namespace(namespace)

    results = graph.query("""
                SELECT ?accidentvictim
                WHERE{
                ?accidentvictim pf:hasVictimType <http://ws_22208_65138.com/VictimType/Passenger> .
                ?accidentvictim pf:hasVictimAge <http://ws_22208_65138.com/VictimAge/Y0-17> .
                }
                    """, initNs={'pf': ns})

    return results

def addDayTime(graph, namespace):
    ns = Namespace(namespace)

    queryAfternoon = """
        CONSTRUCT {
            ?roadaccident <http://xmlns.com/gah/0.1/DayTime> <http://ws_22208_65138.com/DayTime/afternoon>
        }
        WHERE {
            ?roadaccident pf:happenedDuring <http://ws_22208_65138.com/AccTime/T13-17> .
        }
        """

    queryMorning = """
        CONSTRUCT {
            ?roadaccident <http://xmlns.com/gah/0.1/DayTime> <http://ws_22208_65138.com/DayTime/morning>
        }
        WHERE {
            {
                ?roadaccident pf:happenedDuring <http://ws_22208_65138.com/AccTime/T07-09> .
            }
            UNION
            {
                ?roadaccident pf:happenedDuring <http://ws_22208_65138.com/AccTime/T09-13> .
            }
            UNION
            {
                ?roadaccident pf:happenedDuring <http://ws_22208_65138.com/AccTime/T24-07> .
            }
        }
        """

    queryEvening = """
        CONSTRUCT {
            ?roadaccident <http://xmlns.com/gah/0.1/DayTime> <http://ws_22208_65138.com/DayTime/evening>
        }
        WHERE {
            {
                ?roadaccident pf:happenedDuring <http://ws_22208_65138.com/AccTime/T17-21> .
            }
            UNION
            {
                ?roadaccident pf:happenedDuring <http://ws_22208_65138.com/AccTime/T21-24> .
            }
        }
        """

    result = graph.query(queryAfternoon,initNs={'pf':ns})
    for triple in result:
        graph.add(triple)
    result = graph.query(queryMorning,initNs={'pf':ns})
    for triple in result:
        graph.add(triple)
    result = graph.query(queryEvening,initNs={'pf':ns})
    for triple in result:
        graph.add(triple)


def addVictimUnderage(graph, namespace):

    ns = Namespace(namespace)
    results = graph.query(
    """CONSTRUCT {
    ?accidentvictim <http://xmlns.com/gah/0.1/UnderagePassenger> <http://ws_22208_65138.com/isUnderagePassenger>
    }
    WHERE{
    ?accidentvictim pf:hasVictimType <http://ws_22208_65138.com/VictimType/Passenger> .
    ?accidentvictim pf:hasVictimAge <http://ws_22208_65138.com/VictimAge/Y0-17> .
    }
    """, initNs={'pf': ns})

    #.serialize(format="xml")

    #(rdflib.term.URIRef('http://ws_22208_65138.com/AccidentVictim/459'),) http://xmlns.com/gah/0.1/UnderagePassenger http://ws_22208_65138.com/isUnderagePassenger

    return results

def UnderagePassengerCount (graph, namespace, predicate):
    qry = "SELECT  (COUNT(?s) as ?pCount) " \
            " WHERE {?s <http://xmlns.com/gah/0.1/UnderagePassenger> <http://ws_22208_65138.com/isUnderagePassenger> . } "
    results = graph.query(qry)
    return results

def DayTimeCount (graph):
    qry = "SELECT  (COUNT(*) as ?pCount) " \
          " WHERE {?s <http://xmlns.com/gah/0.1/DayTime> ?daytime . } "
    results = graph.query(qry)
    return results




