import sys
from typing import cast
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from src.windows.main_window_ui import Ui_MainWindow


class MapWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._init_ui()
        self._current_value = ""
        self._eval_value = ""

    def _init_ui(self) -> None:
        ...


