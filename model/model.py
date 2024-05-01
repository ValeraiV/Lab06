from database.products_DAO import Product_DAO
from database.sales_DAO import Sale_DAO
from database.retailers_DAO import Retailer_DAO

from model.sales import Sale
from model.retailers import Retailer
from model import sales


class Model:
    def __init__(self):
        self._sales_DAO = Sale_DAO()
        self._products_DAO = Product_DAO()
        self._retailers_DAO = Retailer_DAO()
        self.retailers_map = {}


    def get_anno(self):
        return self._sales_DAO.get_anno()

    def get_brand(self):
        return self._products_DAO.get_brand()

    def get_retailer(self)  -> set[Retailer]:
        return self._retailers_DAO.get_retailer(self.retailers_map)


    def get_top_sales(self, anno, brand, retailer_code) -> list[Sale]:
        filtered_sales = self._sales_DAO.get_filtered_sales(anno, brand, retailer_code)
        filtered_sales.sort(reverse=True)
        return filtered_sales[0:5]


def get_sales_stats(self, anno, brand, retailer_code):
        filtered_sales = self._sales_DAO.get_filtered_sales(anno, brand, retailer_code)
        ricavo_totale = sum([sales.ricavo for sales in filtered_sales])
        retailers_involved = set([sales.retailer_code for sales in filtered_sales])
        product_involved = set([sales.product_number for sales in filtered_sales])
        return ricavo_totale, len(filtered_sales), len(retailers_involved), len(product_involved)