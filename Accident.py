__author__ = '22208_65138'
import SPARQLQueries

class Accident():
    def Data (self, g, accidentId):
        results = SPARQLQueries.accidentData (g,"http://xmlns.com/gah/0.1/",accidentId)
        r = results.bindings[0]
        print ("Dados do acidente: " + accidentId)
        print ("Veiculo:" + str(r["?descVeiculo"]))
        print ("Causa:" + str(r["?descCausa"]))
        print ("Intervalo horário:" + str(r["?descHora"]))
        print ("Local:" + str(r["?descLocal"]))
        print ("Numero de Vitimas:" + str(r["?nVitimas"]))

#        if len (list) == 0:
#            return "Acidente não encontrado"


