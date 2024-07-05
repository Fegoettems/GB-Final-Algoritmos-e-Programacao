from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.label = QLabel("Bem-vindo ao Sistema de Gerenciamento de Pedidos")
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        buttons_layout = QVBoxLayout()
        main_layout.addLayout(buttons_layout)

        self.button_order = QPushButton("Realizar Pedido")
        self.button_order.setFixedSize(500, 40)
        buttons_layout.addWidget(self.button_order)

        self.button_kitchen = QPushButton("Gerenciar Cozinha")
        self.button_kitchen.setFixedSize(500, 40)
        buttons_layout.addWidget(self.button_kitchen)

        self.button_report = QPushButton("Visualizar Relatórios")
        self.button_report.setFixedSize(500, 40)
        buttons_layout.addWidget(self.button_report)

        buttons_layout.setAlignment(Qt.AlignCenter)
