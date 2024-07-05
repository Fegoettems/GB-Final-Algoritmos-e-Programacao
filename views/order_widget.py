from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QSpinBox, QPushButton, QMessageBox
from PySide6.QtCore import Signal
from models.data import menu

class OrderWidget(QWidget):
    order_added = Signal(dict)

    def __init__(self):
        super().__init__()
        order_layout = QVBoxLayout()
        self.setLayout(order_layout)

        self.label = QLabel("Realizar Pedido")
        order_layout.addWidget(self.label)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Item", "Preço", "Quantidade"])
        order_layout.addWidget(self.table)

        for item, price in menu.items():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(item))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(price)))
            quantity = QSpinBox()
            quantity.setRange(0, 100)
            self.table.setCellWidget(row_position, 2, quantity)

        self.line_edit_order_number = QLineEdit()
        self.line_edit_order_number.setPlaceholderText("Número de Pedido/Mesa")
        order_layout.addWidget(self.line_edit_order_number)

        self.button_add_order = QPushButton("Adicionar Pedido")
        order_layout.addWidget(self.button_add_order)
        self.button_return_menu = QPushButton("Voltar")
        order_layout.addWidget(self.button_return_menu)

        self.button_add_order.clicked.connect(self.add_order)

    def add_order(self):
        order_number = self.line_edit_order_number.text()
        if not order_number:
            QMessageBox.warning(self, "Erro", "Número do pedido/mesa é obrigatório!")
            return
        
        order = {"pedido": {}, "status": "Pedido", "Número do Pedido/Mesa": order_number}
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0).text()
            quantity = self.table.cellWidget(row, 2).value()
            if quantity > 0:
                order["pedido"][item] = quantity
        self.order_added.emit(order)
        self.clear_order_inputs()

    def clear_order_inputs(self):
        self.line_edit_order_number.clear()
        for row in range(self.table.rowCount()):
            self.table.cellWidget(row, 2).setValue(0)
