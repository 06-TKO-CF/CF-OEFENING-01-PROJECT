import sqlite3

class Pakjesdienst:
    def __init__(self) -> None:
        '''
        constructor
        '''

        self._dbVerbinding = sqlite3.connect('data/verzendkosten.sqlite3')
        self._dbCursor = self._dbVerbinding.cursor()

    def categorieen(self) -> list:
        '''
        levert de gewichtën

        :return :list
        '''
        dbSql = '''
            SELECT *
            FROM categorie
        '''

        dbResultaat = self._dbCursor.execute(dbSql)

        return [dbRij[0] for dbRij in dbResultaat.fetchall()]
    
    def landen(self) -> list:
        '''
        levert een list met landen

        :return :list
        '''
        dbSql = '''
            SELECT *
            FROM land
        '''

        dbResultaat = self._dbCursor.execute(dbSql)

        return [dbRij[0] for dbRij in dbResultaat.fetchall()]
    
    def bereken(self, land:str, gewicht:str, verzekerd:bool) -> float:
        '''
        levert de kostprijs van de zending

        :param land: str
        :param gewicht: str
        :param verzekerd: bool
        :return :float
        '''
        dbSql = '''
            SELECT prijs
            FROM tarief
            WHERE landID = ?
              AND categorieID = ?
        '''

        dbKostprijs  = self._dbCursor.execute(dbSql, (land, gewicht)).fetchone()[0]
        dbKostprijs += 5 if verzekerd else 0
        
        return round(dbKostprijs, 2)
    