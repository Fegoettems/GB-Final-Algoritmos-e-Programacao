from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView
from models.data import order_queue, delivered_orders

class KitchenWidget(QWidget):
    def __init__(self):
        super().__init__()

        kitchen_layout = QVBoxLayout()
        self.setLayout(kitchen_layout)

        self.label = QLabel("Gerenciar Cozinha")
        kitchen_layout.addWidget(self.label)

        self.table_orders = QTableWidget(0, 3)
        self.table_orders.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_orders.setHorizontalHeaderLabels(["Número do Pedido/Mesa", "Pedido", "Status"])
        kitchen_layout.addWidget(self.table_orders)

        self.button_prepare = QPushButton("Iniciar Preparação")
        kitchen_layout.addWidget(self.button_prepare)
        self.button_prepare.clicked.connect(self.prepare_order)

        self.button_complete = QPushButton("Marcar como Pronto")
        kitchen_layout.addWidget(self.button_complete)
        self.button_complete.clicked.connect(self.complete_order)

        self.button_return_menu = QPushButton("Voltar")
        kitchen_layout.addWidget(self.button_return_menu)

    def update_orders(self):
        self.table_orders.setRowCount(len(order_queue))
        for row, order in enumerate(order_queue):
            pedido_str = "\n".join([f"{item}: {quantity}" for item, quantity in order["pedido"].items()])
            self.table_orders.setItem(row, 0, QTableWidgetItem(order["Número do Pedido/Mesa"]))
            self.table_orders.setItem(row, 1, QTableWidgetItem(pedido_str))
            self.table_orders.setItem(row, 2, QTableWidgetItem(order["status"]))

    def prepare_order(self):
        for order in order_queue:
            if order["status"] == "Pedido":
                order["status"] = "Em Preparação"
                break
        self.update_orders()

    def complete_order(self):
        selected_row = self.table_orders.currentRow()
        if selected_row != -1 and order_queue[selected_row]["status"] == "Em Preparação":
            order_queue[selected_row]["status"] = "Entregue"
            delivered_orders.append(order_queue[selected_row])
            del order_queue[selected_row]
            self.update_orders()
        else:
            print("Selecione um pedido em preparação para marcar como pronto.")
