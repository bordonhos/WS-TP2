__author__ = '22208_65138'

class Accident():
    def Data (self, g, accidentId):
        list = g.search ((accidentId, None, None))
        if len (list) == 0:
            return "Acidente não encontrado"
        else:
            numVeiculos = 0
            numVitimas = 0
            st = "[id: " + g.CleanUri (accidentId)
            for tuple in list:
                if tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasAccVehicle":
                    numVeiculos = numVeiculos + 1
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictim":
                    numVitimas = numVitimas + 1
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasAccCause":
                    st = st + " | Causa:" + g.CleanUri (tuple[2])
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#happenedDuring":
                    st = st + " | Intervalo de tempo:" + g.CleanUri (tuple[2])
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#happenedInRoadNet":
                    st = st + " | Zona:" + g.CleanUri (tuple[2])


            st = st + " | Nº Veiculos: " + str(numVeiculos) + " | Nº Vitimas :" + str (numVitimas) + "]"
            return st

