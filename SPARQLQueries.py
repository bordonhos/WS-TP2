__author__ = '22208_65138'

from rdflib.graph import ConjunctiveGraph, Namespace

def predicateCount (graph, namespace, predicate):
    ns = Namespace(namespace)
    results = graph.query("""
                SELECT (COUNT(pf:accidentID) as ?pCount)
                WHERE{
                    ?s pf:accidentID ?o .
                }
                """, \
              initNs={'pf':ns})
    return results

def victimCount (graph, namespace, predicate):
    ns = Namespace(namespace)
    results = graph.query("""
                SELECT (COUNT(pf:victimID) as ?pCount)
                WHERE{
                    ?s pf:victimID ?o .
                }
                """, \
                          initNs={'pf':ns})
    return results

def listAccidentTypes (graph, namespace):
    ns = Namespace(namespace)
    results = graph.query("""
                    SELECT ?DescricaoTipoAcidente ( Count (*) as ?count)
                    WHERE{
                    ?s pf:hasAccType ?TipoAcidente .
                    ?TipoAcidente pf:description ?DescricaoTipoAcidente .
                    }
                    GROUP BY ?DescricaoTipoAcidente
                    ORDER BY DESC (?count)
                    """, \
                          initNs={'pf':ns})
    return results

def listAccidentCauses (graph, namespace):
    ns = Namespace(namespace)
    results = graph.query("""
                    SELECT ?DescricaoCausaAcidente ( Count (*) as ?count)
                    WHERE{
                    ?s pf:hasAccCause ?CausaAcidente .
                    ?CausaAcidente pf:description ?DescricaoCausaAcidente .
                    }
                    GROUP BY ?DescricaoCausaAcidente
                    ORDER BY DESC (?count)
                    """, \
                          initNs={'pf':ns})
    return results

def listVictimAges (graph, namespace):
    ns = Namespace(namespace)
    results = graph.query("""
                    SELECT ?FaixaEtaria  ( Count (*) as ?count)
                    WHERE{
                    ?s pf:hasVictimAge ?idFaixa .
                    ?idFaixa pf:description ?FaixaEtaria  .
                    }
                    GROUP BY ?FaixaEtaria
                    ORDER BY DESC (?count)
                    """, \
                          initNs={'pf':ns})
    return results

def accidentData (graph, namespace, accidentID):
    ns = Namespace(namespace)
    results = graph.query("""
                SELECT ?idAcidente ?descVeiculo ?descCausa ?descHora ?descLocal (count (?idVitima) as ?nVitimas)
                WHERE{
                ?idAcidente pf:accidentID ?acidente.
                ?idAcidente pf:hasAccVehicle ?idtipoVeiculo.
                ?idtipoVeiculo pf:description ?descVeiculo.
                ?idAcidente pf:hasAccCause ?idCausa.
                ?idCausa pf:description ?descCausa.
                ?idAcidente pf:happenedDuring ?idHora.
                ?idHora pf:description ?descHora.
                ?idAcidente pf:happenedDuring ?idHora.
                ?idHora pf:description ?descHora.
                ?idAcidente pf:happenedInRoadNet ?idLocal.
                ?idLocal pf:description ?descLocal.
                ?idAcidente pf:hasVictim ?idVitima.
                    FILTER (?acidente = 112)
                }
                GROUP BY ?idAcidente ?descVeiculo ?descCausa ?descHora ?descLocal
                    """, \
                          initNs={'pf':ns})
    return results