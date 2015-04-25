__author__ = '22208_65138'

import grafo
import Accident
import Victim
import ExtractGraph
import inferencerules
import rdflib
import converter
from rdflib import ConjunctiveGraph

#https://docs.python.org/2/tutorial/datastructures.html
def list(list):
    #TODO: Format print
    print(list)

#https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
def filter(element, list):
    return [item for item in list if element in item]


def exists(element, list):
    if any(element in tuple for tuple in list):
        return True
    return False

def readTuple():
    e1 = input('1º Elemento: ')
    if e1.strip() == "":
        e1 = None
    e2 = input('2º Elemento: ')
    if e2.strip() == "":
        e2 = None
    e3 = input('3º Elemento: ')
    if e3.strip() == "":
        e3 = None
    tuple = (e1,e2,e3)
    return tuple

def listDistinctValues (list):
    values = []
    for tuple in list:
        if not g.CleanUri (tuple[2]) in values:
            values.append( g.CleanUri (tuple[2]))
    for st in values:
        print (st)


def listaRegistos (list, tipo, campo):
#    dados = None;
    if tipo == 'acidentes':
        dados = Accident.Accident()
    elif tipo == 'vitimas':
        dados = Victim.Victim()
    key="X"
    while key != 'S' and key != 'N':
        key = input ("Deseja listar " + str(tipo) + " (S/N)?")
        if key == 'S':
            for c in list:
                print (dados.Data (g, c[campo]))


flag = True
g = converter

while flag:
    print('\n --=== MENU ===--')
    print('1 - Carregar Ficheiro') #Carraga o ficheiro
    print('2 - Dados Gerais') #informação geral sobre os dados
    print('3 - Procurar Acidente/Vitima') # pesquisar dados de determinado acidente
    print('4 - Consultas') #algumas consultas sobre os dados
    print('5 - Aplicar Inferências')
    print('6 - Converter Dados') #Converter dados noutros formatos
    print('X - Terminar')
    n = input('Opção: ')
    if n.strip() == 'X':
        flag = False
    if n.strip() == '1':
        g.parse("Dados\\roadaccidents.nt")  #--> Working

        q.query ()
    if n.strip() == '2':
        key = 'Z';
        while key != 'X':
            print('\n --=== Listar ===--')
            print('1 - Número Total de Acidentes')
            print('2 - Número de Vitimas')
            print('3 - Numero de Acidentes com automóveis')
            print('4 - Causas de Acidentes')
            print('5 - Faixas etárias')
            print('6 - Zonas de Acidentes')
            print('X - Menu anterior')
            key = input('Opção')
            if key == '1':
                list = g.search((None, "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#accidentID", None));
                print ('Existiram ' + str(len (list)) + ' acidentes');
            if key == '2':
                list = g.search((None, "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#victimID", None));
                print ('Existiram ' + str(len (list)) + ' Vitimas');
            if key == '3':
                list = g.search((None, "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#inVehicle", "http://crashmap.okfn.gr/data/accidents/AccVehicle/Car"));
                print ('Existiam ' + str(len (list)) + ' acidentes com automóveis');
            if key == '4':
                list = g.search ((None,"http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasAccCause", None))
                listDistinctValues (list)
            if key == '5':
                list = g.search ((None,"http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge", None))
                listDistinctValues (list)
            if key == '6':
                list = g.search ((None,"http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#happenedInRoadNet", None))
                listDistinctValues (list)
    if n.strip() == '3':
        key = 'Z';
        while key != 'X':
            print('\n --=== Pesquisar ===--')
            print('1 - Acidente')
            print('2 - Vitima')
            print('X - Voltar')
            key = input('Opção: ')
            if key == '1':
                id = input ("Introduza o id do Acidente: ")
                acc = Accident.Accident()
                print (acc.Data(g,"http://crashmap.okfn.gr/data/accidents/RoadAccident/" + str(id)))
            if key == '2':
                id = input ("Introduza o id da Vitima: ")
                acc = Victim.Victim()
                print (acc.Data(g,"http://crashmap.okfn.gr/data/accidents/AccidentVictim/" + str(id)))
    if n.strip() == '4':
        key = 'Z';
        while key != 'X':
            print('\n --=== Consultar ===--')
            print('1 - Idade das vitimas de um acidente')
            print('2 - Tipo de veiculo e causa do acidente envolvendo uma vitima')
            print('3 - Acidentes envolvendo motas devido a excesso de velocidade')
            print('4 - Condutores menores de idade')
            print('X - Menu anterior')
            key = input('Opção')

            if key == '1':
                acc = input ("Introduza o id do acidente")
                list = g.query ([( "?subVitima", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge","?idade"),
                         ("?subVitima", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#involvedIn", "http://crashmap.okfn.gr/data/accidents/RoadAccident/"+str(acc))
                          ])
                if len (list) == 0:
                    print ("Acidente não encontrado")
                else:
                    print ("Esse acidente teve " + str(len(list)) + " vitimas:")
                    for c in list:
                        print ("A vitima " + g.CleanUri (c["subVitima"]) + " na faixa etária " +  g.CleanUri (c["idade"]))

            if key == '2':
                vit = input ("Introduza o id da vitima")
                list = g.query ([
                                 ("?subAcidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasAccCause","?causa"),
                                 ("http://crashmap.okfn.gr/data/accidents/AccidentVictim/" + str(vit), "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#involvedIn","?subAcidente")
                                ])
                if len (list) == 0:
                    print ("Vitima não encontrada")
                else:
                    print ("A causa desse acidente dessa vitima foi :")
                    for c in list:
                        print (g.CleanUri (c["causa"]))

                    list = g.search (("http://crashmap.okfn.gr/data/accidents/AccidentVictim/" + str(vit),"http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#inVehicle", None))
                    print ("O tipo de veiculo onde seguia era :")
                    for c in list:
                        print (g.CleanUri(c[2]))
            if key == '3':
                list = g.query ([( "?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasAccCause","http://crashmap.okfn.gr/data/accidents/AccCause/Speeding"),
                          ("?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasAccVehicle", "http://crashmap.okfn.gr/data/accidents/AccVehicle/Motorcycle")
                ])
                print ("Foram encontrados "  + str (len(list)) + " acidentes.");
                listaRegistos (list,"acidentes", "subacidente")

            if key == '4':
                list = g.query ([( "?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge","http://crashmap.okfn.gr/data/accidents/VictimAge/Y0-17"),
                                 ("?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimType", "http://crashmap.okfn.gr/data/accidents/VictimType/Driver")
                ])
                print ("Foram encontrados "  + str (len(list)) + " vitimas.")
                listaRegistos (list,"vitimas", "subacidente")
    if n.strip() == '5':
        dayTimeRule = inferencerules.DayTime()
        underageRule = inferencerules.UnderagePassenger()
        key = 'Z';
        while key != 'X':
            print('\n --=== Aplicar Inferências ===--')
            print('1 - Altura do dia em que ocorreu o acidente')
            print('2 - Vitimas menores de idade (passageiros)')
            print('X - Menu anterior')
            key = input('Opção')
            if key == '1':
                g.applyinference(dayTimeRule)
            elif key == '2':
                g.applyinference(underageRule)

    if n.strip() == '6':
        key = 'Z';
        while key != 'X':
            print('\n --=== Converter Ficheiro ===--')
            print('1 - CSV --> RDF/NT')
            print('2 - RDF/NT -->  RDF/N3')
            print('3 - RDF/NT --> RDF/XML')
            print('4 - RDF/NT --> SQLITE')
            print('X - Menu anterior')
            key = input('Opção')

            if key == '1':
                converter.ConvertCSVToTN ("Dados\\roadaccidents.csv","Dados\\roadaccidents.nt")
            if key == '2':
                converter.ConvertToRDFN3 ("Dados\\roadaccidents.nt", "Dados\\roadaccidents.n3")
            if key == '3':
                converter.ConvertToRDFXML ("Dados\\roadaccidents.nt","Dados\\roadaccidents.xml")
            if key == '4':
                converter.ConvertToSQLLITE ("Dados\\roadaccidents.nt","Dados\\roadaccidents.db")