from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView
from models.data import menu

class ReportWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Relatórios de Faturamento")
        layout.addWidget(self.label)

        self.label_total_revenue = QLabel("Faturamento Total: R$ 0.00")
        layout.addWidget(self.label_total_revenue)

        self.table_items_sold = QTableWidget(0, 2)
        self.table_items_sold.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_items_sold.setHorizontalHeaderLabels(["Item", "Quantidade Vendida"])
        layout.addWidget(self.table_items_sold)

        self.button_return_menu = QPushButton("Voltar")
        layout.addWidget(self.button_return_menu)

    def update_report(self, orders):
        total_revenue = 0
        items_sold = {item: 0 for item in menu.keys()}
        for order in orders:
            for item, quantity in order["pedido"].items():
                total_revenue += menu[item] * quantity
                items_sold[item] += quantity
        
        self.label_total_revenue.setText(f"Faturamento Total: R$ {total_revenue:.2f}")

        self.table_items_sold.setRowCount(len(items_sold))
        for row, (item, quantity) in enumerate(items_sold.items()):
            self.table_items_sold.setItem(row, 0, QTableWidgetItem(item))
            self.table_items_sold.setItem(row, 1, QTableWidgetItem(str(quantity)))
