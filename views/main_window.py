from PySide6.QtWidgets import QMainWindow
from .menu_widget import MenuWidget
from .order_widget import OrderWidget
from .kitchen_widget import KitchenWidget
from .report_widget import ReportWidget
from models.data import order_queue, delivered_orders

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciamento de Pedidos do Restaurante")
        self.resize(800, 600)

        self.menu_principal = MenuWidget()
        self.menu_pedido = OrderWidget()
        self.cozinha = KitchenWidget()
        self.menu_relatorio = ReportWidget()

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.menu_principal)
        self.menu_principal.button_order.clicked.connect(self.show_order)
        self.menu_principal.button_kitchen.clicked.connect(self.show_kitchen)
        self.menu_principal.button_report.clicked.connect(self.show_report)
        self.menu_pedido.button_return_menu.clicked.connect(self.show_menu)
        self.cozinha.button_return_menu.clicked.connect(self.show_menu)
        self.menu_relatorio.button_return_menu.clicked.connect(self.show_menu)

        self.menu_pedido.order_added.connect(self.add_order_to_queue)

    def show_order(self):
        self.setCentralWidget(self.menu_pedido)

    def show_kitchen(self):
        self.cozinha.update_orders()
        self.setCentralWidget(self.cozinha)

    def show_report(self):
        self.menu_relatorio.update_report(order_queue + delivered_orders)
        self.setCentralWidget(self.menu_relatorio)

    def show_menu(self):
        self.menuprincipal = MainWindow()
        self.setCentralWidget(self.menuprincipal)

    def add_order_to_queue(self, order):
        order_queue.append(order)
        print("Pedido adicionado:", order)
