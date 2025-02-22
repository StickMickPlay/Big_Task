import sys

from PyQt6.QtWidgets import QApplication

from basic_main import MapWindow


def main():
    app = QApplication(sys.argv)
    ex = MapWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
