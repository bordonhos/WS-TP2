__author__ = '22208_65138'

class Victim():
    def Data (self, g, victimId):
        list = g.search ((victimId, None, None))
        if len (list) == 0:
            return "Vitima não encontrada"
        else:
            numVeiculos = 0
            numVitimas = 0
            st = "[id: " + g.CleanUri (victimId)
            for tuple in list:
                if tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimType":
                    st = st + " | Tipo:" + g.CleanUri (tuple[2])
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge":
                    st = st + " | Faixa Etária:" + g.CleanUri (tuple[2])
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#inVehicle":
                    st = st + " | Veiculo:" + g.CleanUri (tuple[2])
                elif tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#involvedIn":
                    st = st + " | Acidente:" + g.CleanUri (tuple[2])

            return st
