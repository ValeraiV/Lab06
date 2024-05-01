from database.DB_connect import DBConnect

class DAO():

    def get_anno(self):
        return self.connection("""select distinct (year(gds.Date))
                                    from go_daily_sales gds 
                                    order by gds.`Date`
                                    """)
    def get_brand(self):
        return self.connection("""select distinct (gp.Product_brand)
                                    from go_products gp 
                                    """)

    def get_retailer(self):
        return self.connection("""select distinct (gr.Retailer_name), gr.Retailer_code 
                                    from go_retailers gr 
                                    """)

    def get_top_vendite(self):
        pass

    def connection(self, query):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor:
                result.append(row)
            cursor.close()
            cnx.close()
            return result
        else:
            print("Could not connect")
            return None

