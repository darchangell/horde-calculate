'''
Created on Jan 16, 2014

@author: patrick
'''
import xmltodict
       
class GameFaction():

    def __init__(self,fileName):
        #super(GameFaction.__init__(self,fileName))
        self.readFactionInformation(fileName)

    def readFactionInformation(self,fileName):
        xmlToParse = open("c://inetpub/wwwroot/warmachine/factions/" + fileName)
        xmlLines = xmlToParse.read()
        forceList = xmltodict.parse(xmlLines)['forceList']
        for key in forceList.keys():
            print(key)
        #print(xmlLines)
        

xmlToParse = open("c://inetpub/wwwroot/warmachine/factions/Factions.xml")

#print(xmlToParse)
xmlLines = xmlToParse.read()
#print(xmlLines)
factionList = xmltodict.parse(xmlLines)['factionList']
gameFactions = []
for faction in factionList['faction']:
    keys = faction.keys()
    factionName, factionFile, iconFile = [faction[x] for x in keys]
    gameFactions.append(GameFaction(factionFile))
    break
