from model.sales import Sale
from database.DB_connect import DBConnect
class Sale_DAO:

    def get_anno(self) -> list[tuple[int]] | None:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """ select distinct year(gds.Date)
                    from go_daily_sales gds 
                    """

            cursor.execute(query)
            rows = cursor.fetchall()

            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None


    def get_filtered_sales(self, anno, brand, retailer_code) -> list[Sale]:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary = True)
            query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity AS Ricavo
                FROM go_daily_sales gds, go_retailers gr, go_products gp 
                WHERE gds.Retailer_code  = gr.Retailer_code  
                AND gds.Product_number = gp.Product_number 
                AND (YEAR(gds.Date)=COALESCE(%s,YEAR(gds.Date)))
                AND (gp.Product_brand =COALESCE(%s,gp.Product_brand))
                AND (gr.Retailer_code =COALESCE(%s,gr.Retailer_code))"""

            cursor.execute(query, (anno, brand, retailer_code,))
            result = []

            for row in cursor:
                result.append(Sale(row["Date"],
                                row["Quantity"],
                                row["Unit_price"],
                                row["Unit_sale_price"],
                                row["Retailer_code"],
                                row["Product_number"],
                                row["Order_method_code"]))

            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None