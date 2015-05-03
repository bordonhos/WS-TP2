__author__ = '22208_65138'

import Accident
import Victim
import SPARQLQueries

from rdflib import ConjunctiveGraph

flag = True
_graph = ConjunctiveGraph()

#https://docs.python.org/2/tutorial/datastructures.html

def isFileLoaded():
    if len(_graph) == 0:
        print ('O gráfico ainda não foi carregado')
        return False
    return True

while flag:
    print('\n --=== MENU ===--')
    print('1 - Carregar Ficheiro') #Carraga o ficheiro
    print('2 - Dados Gerais') #informação geral sobre os dados
    print('3 - Procurar Acidente/Vitima') # pesquisar dados de determinado acidente
    print('4 - Consultas') #algumas consultas sobre os dados
    print('5 - Inferências')
    print('X - Terminar')
    n = input('Opção: ')
    if n.strip().upper() == 'X':
        flag = False
    if n.strip() == '1':
        _graph.parse("Dados\\roadaccidents.nt", format="nt")
    if n.strip() == '2' and isFileLoaded():
        if(isFileLoaded()):
            key = 'Z';
            while key.upper() != 'X':
                print('\n --=== Listar ===--')
                print('1 - Número Total de Acidentes')
                print('2 - Número de Vitimas')
                print('3 - Tipos de Acidentes')
                print('4 - Causas de Acidentes')
                print('5 - Faixas etárias')
                print('X - Menu anterior')
                key = input('Opção: ')
                if key == '1':
                    results = SPARQLQueries.predicateCount (_graph,"http://xmlns.com/gah/0.1/","accidentID")
                    for r in results:
                        acc = r[0]
                    print ('Existiram ' + str(acc) + ' acidentes');
                if key == '2':
                    results = SPARQLQueries.predicateCount (_graph,"http://xmlns.com/gah/0.1/","victimID")
                    for r in results:
                        acc = r[0]
                    print ('Existiram ' + str(acc) + ' Vitimas');
                if key == '3':
                    results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccType")
                    print ("Os tipos de acidentes que existem são:")
                    print ("Tipo de acidente  --> Número de acidentes")
                    print ("-------------------------------------------")
                    for r in results:
                        print (r[0] +" --> " + r[1])
                if key == '4':
                    results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccCause")
                    print ("As causas de acidentes existentes são:")
                    print ("Causas de acidente  --> Número de acidentes")
                    print ("-------------------------------------------")

                    for r in results:
                        print (r[0] +" --> " + r[1])
                if key == '5':
                    results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasVictimAge")
                    print ("Faixa etária das vitimas --> Número de Vitimas")
                    print ("-------------------------------------------")
                    for r in results:
                        print (r[0] +" --> " + r[1])
    if n.strip() == '3' and isFileLoaded():
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Pesquisar ===--')
            print('1 - Acidente')
            print('2 - Vitima')
            print('X - Voltar')
            key = input('Opção: ')
            if key == '1':
                id = input ("Introduza o id do Acidente: ")
                acc = Accident.Accident()
                acc.Data(_graph,id)
            if key == '2':
                id = input ("Introduza o id da Vitima: ")
                acc = Victim.Victim()
                acc.Data(_graph,id)
    if n.strip() == '4' and isFileLoaded():
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Consultar ===--')
            print('1 - Idade das vitimas de um acidente')
            print('2 - Acidentes por Causa')
            print('3 - Vitimas envolvidas em acidentes com determinados veiculos')
            print('4 - Condutores menores de idade')
            print('X - Menu anterior')
            key = input('Opção: ')

            if key == '1':
                acc = input ("Introduza o id do acidente: ")
                results = SPARQLQueries.accidentVictimAge(_graph,"http://xmlns.com/gah/0.1/", acc)
                if len (results.bindings) == 0:
                    print ("Acidente não encontrado")
                else:
                    print ("Esse acidente teve " + str(len (results.bindings)) + " vitimas:")
                    for c in results.bindings:
                        print ("A vitima " +c["?vitima"] + " na faixa etária " +  c["?descIdade"])

            if key == '2':
                results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccCause")
                i=1
                for r in results:
                    print ("[" + str (i)+ "]: " + r[0])
                    i = i + 1

                acc = input ("Introduza o número correspondente à Causa pretendida: ")
                results = SPARQLQueries.accidentsByType(_graph,"http://xmlns.com/gah/0.1/","hasAccCause", results.bindings[int(acc)-1]["?Descricao"])
                print ("Existem " + str(len(results.bindings)) + " acidentes")
                if input ("Deseja listar os acidentes (S/N)?").upper() == "S":
                    acc = Accident.Accident()
                    for r in results:
                        acc.Data(_graph,r[0])

            if key == '3':
                results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccVehicle")
                i=1
                for r in results:
                    print ("[" + str (i)+ "]: " + r[0])
                    i = i + 1

                vit = input ("Introduza o número correspondente ao veiculo pretendido: ")
                results = SPARQLQueries.accidentsByType(_graph,"http://xmlns.com/gah/0.1/","hasAccVehicle", results.bindings[int(vit)-1]["?Descricao"])
                print ("Existem " + str(len(results.bindings)) + " vitimas")
                if input ("Deseja listar as vitimas (S/N)?").upper() == "S":
                    vit = Victim.Victim()
                    for r in results:
                        victID = r[0]
                        vit.Data(_graph,victID)

            if key == '4':
                results = SPARQLQueries.underageDriver(_graph,"http://xmlns.com/gah/0.1/")
                print ("Existem " + str(len(results.bindings)) + " condutores menores de idade")
                if input ("Deseja listar as vitimas (S/N)?").upper() == "S":
                    vit = Victim.Victim()
                    for r in results:
                        victID = r[0]
                        vit.Data(_graph,r[0])
    if n.strip() == '5' and isFileLoaded():
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Inferências ===--')
            print('1 - Altura do dia em que ocorreu o acidente')
            print('2 - Vitimas menores de idade (passageiros)')
            print('X - Menu anterior')
            key = input('Opção: ')
            if key == '1':
                result = SPARQLQueries.constructDayTime(_graph,"http://xmlns.com/gah/0.1/")
                count = SPARQLQueries.DayTimeCount(_graph,"http://xmlns.com/gah/0.1/")
                for c in count:
                    acc = c[0]
                print (str(acc) + ' inferências aplicadas!')
                if input ("Deseja listar as inferências aplicadas (S/N)?").upper() == "S":
                    dayTimeSelect = SPARQLQueries.DayTimeResult(_graph,"http://xmlns.com/gah/0.1/")
                    for r in dayTimeSelect:
                        print(str(r[0])[26:] + " DayTime " + str(r[1])[26:])
            elif key == '2':
                result = SPARQLQueries.constructUnderagePassenger(_graph,"http://xmlns.com/gah/0.1/")
                for triple in result:
                    _graph.add(triple)
                count = SPARQLQueries.UnderagePassengerCount(_graph,"http://xmlns.com/gah/0.1/")
                for c in count:
                    acc = c[0]
                print (str(acc) + ' inferências aplicadas!')
                if input ("Deseja listar as inferências aplicadas (S/N)?").upper() == "S":
                    for triple in result:
                        print(str(triple[0])[26:] + " " + str(triple[1])[25:] + " " + str(triple[2])[26:])



