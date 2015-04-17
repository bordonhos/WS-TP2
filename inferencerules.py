__author__ = '22208_65138'

class InferenceRule:

    def getqueries(self):
        return None

    def maketriples(self, binding):
        return self._maketriples(**binding)


class DayTime(InferenceRule):
    def getqueries(self):
        happenedDuring = [('?roadaccident', 'http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#happenedDuring', '?happenedDuring')]
        return [happenedDuring]

    def _maketriples(self, happenedDuring, roadaccident):

        if happenedDuring == 'http://crashmap.okfn.gr/data/accidents/AccTime/T13-17':
            daytime = 'afternoon'
        elif happenedDuring == 'http://crashmap.okfn.gr/data/accidents/AccTime/T07-09' or happenedDuring == 'http://crashmap.okfn.gr/data/accidents/AccTime/T09-13' or happenedDuring == 'http://crashmap.okfn.gr/data/accidents/AccTime/T24-07':
            daytime = 'morning'
        elif happenedDuring == 'http://crashmap.okfn.gr/data/accidents/AccTime/T17-21' or happenedDuring == 'http://crashmap.okfn.gr/data/accidents/AccTime/T21-24':
            daytime = 'evening'
        else:
            daytime = 'unknown'
        print('Nova inferencia: ' + roadaccident + '  http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#dayTime  ' + daytime)
        return [(roadaccident,'http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#dayTime',daytime)]



class UnderagePassenger(InferenceRule):
    def getqueries(self):
        hasVictimType = [('?accidentvictim','http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimType','http://crashmap.okfn.gr/data/accidents/VictimType/Passenger')]
        hasVictimAge = [('?accidentvictim', 'http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge', 'http://crashmap.okfn.gr/data/accidents/VictimAge/Y0-17')]
        return [hasVictimType,hasVictimAge]

    def _maketriples(self, accidentvictim):

        underAge = 'UnderagePassenger'
        print('Nova inferencia: ' + accidentvictim + '  http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#UnderagePassanger  ' + underAge)
        return [(accidentvictim,'http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#UnderagePassanger', underAge)]
