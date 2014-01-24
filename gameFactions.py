'''
Created on Jan 16, 2014

@author: patrick
'''
import xmltodict, sys
from PyQt5 import QtCore, QtWidgets, uic

class Character(QtCore.QObject):
  
    def __init__(self, name, game, faction):
        
        super(Character, self).__init__()
        
        self._name = name
        self._game = game
        self._baseFaction = faction
    
    def typeInfo(self):
        return "CHAR"
    
    def name(self):
        return self._name

    def setName(self, name):
        self._name = name

    def game(self):
        return self._game

    def setGame(self, game):
        self._game = game

    def baseFaction(self):
        return self._baseFaction

    def setBaseFaction(self, faction):
        self._baseFaction = faction

class Warlock(Character):
    
    def __init__(self,data):
        super(Warlock, self).__init__(data['name'], "Hordes", data['baseFaction'])

        self._mkiicost = data['mkiicost']

        if 'otherVersionOf' in data.keys():
            self._otherVersionOf = data['otherVersionOf']
        else:
            self._otherVersionOf = self._name

        if 'sortString' in data.keys():
            self._sortString = data['sortString']
        else:
            self._sortString = self._name
            
        self._hitPoints = data['damageGrid']['hitPoints']
        
    def typeInfo(self):
        return "WARLOCK"
    
    def mkiicost(self):
        return self._mkiicost
    
    def otherVersionOf(self):
        return self._otherVersionOf
    
    def sortString(self):
        return self._sortString
    
    def hitPoints(self):
        return self._hitPoints
    
    def setMkiicost(self, cost):
        self._mkiicost =  cost
        
    def setOtherVersionOf(self,otherVersion):
        self._otherVersionOf = otherVersion
        
    def setSortString(self,sortString):
        self._sortString = sortString
        
    def setHitPoints(self,hitPoints):
        self._hitPoints = hitPoints
       

class MyTableModel(QtCore.QAbstractTableModel):

    sortRole   = QtCore.Qt.UserRole
    filterRole = QtCore.Qt.UserRole + 1
 
    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
 
    def columnCount(self, index):
        return len(self.columns)
 
    def rowCount(self, index):
        return len(self.rows)
 
    def data(self, index, role):
        if not index.isValid():
            return None

        char = self.rows[index.row()]
        typeInfo = char.typeInfo()

        if (role == QtCore.Qt.DisplayRole) or (role == QtCore.Qt.EditRole):
            if index.column() == 0:
                return char.name()
            
            if index.column() == 1:
                return typeInfo
            
            if typeInfo == "WARLOCK":
                if index.column() == 2:
                    return char.baseFaction()
                if index.column() == 3:
                    return char.mkiicost()
                if index.column() == 4:
                    return char.otherVersionOf()
                if index.column() == 5:
                    return char.sortString()
                if index.column() == 6:
                    return char.hitPoints()
                
        if role == MyTableModel.sortRole:
            return char.typeInfo()

        if role == MyTableModel.filterRole:
            return char.typeInfo()

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
 
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            char = self.rows[index.row()]
            typeInfo = char.typeInfo()
            
            if index.column() == 0:
                char.setName(value)
            
            if typeInfo == "WARLOCK":
                if index.column() == 2:
                    char.setBaseFaction(value)
                if index.column() == 3:
                    char.setMkiicost(value)
                if index.column() == 4:
                    char.setOtherVersionOf(value)
                if index.column() == 5:
                    char.setSortString(value)
                if index.column() == 6:
                    char.setHitPoints(value)
            
            self.dataChanged.emit(index, index)
            return True
        return False
 
    def insertRows(self,row,count,index):
        self.beginInsertRows(index,row,count)
        if 0 <= row < len(self.rows):
            self.rows.insert(row,["","","","","",""])
        self.endInsertRows()
        return True
    
#     def headerData(self, section, orientation, role):
#         if role == QtCore.Qt.DisplayRole:
#             if section == 0:
#                 return "Character Name"
#             else:
#                 return "Character Type"

        
base, form = uic.loadUiType("c://Work/eclipse/workspace/horde-calculator/charTable.ui")

class GameFaction(base,form):

    def __init__(self,fileName,parent=None):
        super(base, self).__init__(parent)
        self.setupUi(self)
        characterList = self.readFactionInformation(fileName)
        characters = [Warlock(char) for char in characterList]
        
        self._proxyModel = QtCore.QSortFilterProxyModel(self)
        
        """VIEW <------> PROXY MODEL <------> DATA MODEL"""

        self._model = MyTableModel(characters, ("Name","Type"))

        self._proxyModel.setSourceModel(self._model)
        self._proxyModel.setDynamicSortFilter(True)
        self._proxyModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self._proxyModel.setSortRole(MyTableModel.sortRole)
        self._proxyModel.setFilterRole(MyTableModel.filterRole)
        self._proxyModel.setFilterKeyColumn(0)
        
        self.charTable.setModel(self._proxyModel)

        self.uiFilter.textChanged.connect(self._proxyModel.setFilterRegExp)
        
        self.charTable.setSortingEnabled(True)
        

    def readFactionInformation(self,fileName):
        xmlToParse = open("c://Work/Hordes-Calc/" + fileName)
        xmlLines = xmlToParse.read()
        forceList = xmltodict.parse(xmlLines)['forceList']
        return forceList['warlock']
        '''
        for key in forceList.keys():
            print(key)
            print(forceList[key])
        #print(xmlLines)
        '''


if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    xmlToParse = open("c://Work/Hordes-Calc/Factions.xml")
    xmlLines = xmlToParse.read()
    factionList = xmltodict.parse(xmlLines)['factionList']
    gameFactions = []
    for faction in factionList['faction']:
        keys = faction.keys()
        factionName, factionFile, iconFile = [faction[x] for x in keys]
        gameFactions.append(GameFaction(factionFile))
        break
    gameFactions[0].show()

    sys.exit(app.exec_())
