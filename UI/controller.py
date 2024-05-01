import flet as ft
from model.model import Model
from UI.view import View
class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer_code = None

    def populate_dd_anno(self):
        anni = self._model.get_anno()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def read_anno(self, e):
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    def populate_dd_brand(self):
        brand = self._model.get_brand()
        for b in brand:
            self._view.dd_brand.options.append(ft.dropdown.Option(b[0]))
        self._view.update_page()

    def read_brand(self, e):
        if e.control.value == "None":
            self._brand = None
        else:
            self._brand = e.control.value

    def populate_dd_retailer(self):
        retailers = self._model.get_retailer()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(text=retailer.retailer_name,
                                                                     data = retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        if e.control.data is None:
            self._retailer_code = None
        else:
            self._retailer_code = e.control.data.retailer_code

    def handle_top_vedite(self, e):
        top_vendite = self._model.get_top_sales(self._anno, self._brand, self._retailer_code)
        self._view.lista_risultati.controls.clear()
        if len(top_vendite) == 0:
            self._view.lista_risultati.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.lista_risultati.controls.append(ft.Text(vendita))
        self._view.update_page()

    def handle_analizza_vendite(self, e):
        statistiche = self._model.get_sales_stats(self._anno, self._brand, self._retailer_code)
        self._view.lista_risultati.controls.clear()
        self._view.lista_risultati.controls.append(ft.Text("Statistiche vendite:"))
        self._view.lista_risultati.controls.append(ft.Text(f"Giro d'affari: {statistiche[0]}"))
        self._view.lista_risultati.controls.append(ft.Text(f"Numero vendite: {statistiche[1]}"))
        self._view.lista_risultati.controls.append(ft.Text(f"Numero retailers coinvolti: {statistiche[2]}"))
        self._view.lista_risultati.controls.append(ft.Text(f"Numero prodotti coinvolti: {statistiche[3]}"))
        self._view.update_page()