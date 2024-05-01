import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None

        self.btn_top_vendite = None
        self.btn_analizza_vendite = None
        self.lista_risultati = None


    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.dd_anno= ft.Dropdown(hint_text="Filtro per anno",
                                   label="anno",
                                   options= [ft.dropdown.Option(key= "None",
                                                               text= "Nessun Filtro")],
                                   on_change=self._controller.read_anno)

        self._controller.populate_dd_anno()


        self.dd_brand = ft.Dropdown(hint_text="Filtro per brand",
                                    label="brand",
                                    options=[ft.dropdown.Option(key="None",
                                                                text = "Nessun Filtro")],
                                    on_change=self._controller.read_brand)

        self._controller.populate_dd_brand()

        self.dd_retailer = ft.Dropdown(hint_text="Filtro per retailer",
                                        label="retailer",
                                        options=[ft.dropdown.Option(key="None",
                                                                    text = "Nessun Filtro",
                                                                    data = None,
                                                                    on_click=self._controller.read_retailer)])
        self._controller.populate_dd_retailer()


        row1 = ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)

        self.btn_top_vendite = ft.ElevatedButton(text= "Top Vendite", on_click=self._controller.handle_top_vedite)
        self.btn_analizza_vendite = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handle_analizza_vendite)

        row2 = ft.Row([self.btn_top_vendite, self.btn_analizza_vendite],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        # List View where the reply is printed
        self.lista_risultati = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lista_risultati)
        self._page.update()


    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
