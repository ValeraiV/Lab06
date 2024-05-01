from database.DB_connect import DBConnect
from model.retailers import Retailer
class Retailer_DAO:

    def get_retailer(self, retailers_map)-> set[Retailer]|None:  #il set rimuove i duplicati
        cnx = DBConnect.get_connection()

        if cnx is not None:
            cursor = cnx.cursor(dictionary = True)
            query = """select * from go_retailers"""
            cursor.execute(query)
            result = set()
            for row in cursor.fetchall():
                read_retailer = Retailer(row["Retailer_code"],
                                         row["Retailer_name"],
                                         row["Type"],
                                         row["Country"])

                result.add(read_retailer)
                retailers_map[read_retailer.retailer_code] = read_retailer
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None