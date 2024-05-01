from database.DB_connect import DBConnect
from model.products import Product

class Product_DAO():
    def get_product(self) -> set[Product]|None:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary = True)
            query = """ SELECT * FROM go_product"""
            cursor.execute(query)
            result = set()

            for row in cursor.fetchall():  #ci da delle tuple per ogni risultato della query
                result.add(Product(row["Product_number"],
                                   row["Product_line"],
                                   row["Product"],
                                   row["Product_brand"],
                                   row["Product_color"],
                                   row["Unit_cost"],
                                   row["Unit_price"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    def get_brand(self) -> list[tuple[str]]:
        cnx = DBConnect.get_connection()

        if cnx is not None:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT Product_brand
                    FROM go_products"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()

            return rows

        else:
            print("Errore nella connessione")
            return None