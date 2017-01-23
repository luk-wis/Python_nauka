# -*- coding: utf-8 -*-

"""
window in PyQt5.

author: Lukasz Wisniewski

last edited: 29 December 2016
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget,QTextEdit,
                             QLabel, QAction, QLineEdit, QGridLayout, QSlider, QLCDNumber, QComboBox, QFrame, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.Komponety()
        self.initUI()


    def initUI(self):
        self.resize(900, 600)
        self.move(300, 300)
        self.setWindowTitle('Aplikacja graficzna')
        self.setWindowIcon(QIcon('web.png'))
        self.Center()
        self.show()


    def Center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def wczytaj_obraz(self):
        fname = QFileDialog.getOpenFileName (self)
        self.setPixmap(QPixmap(fname))


    def Komponety(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        grid = QGridLayout()
        grid.setSpacing(20)

        lbl_filtr= QLabel('Filtr:', self)
        lbl_skala= QLabel('Skalowanie:', self)

        btn_otworz = QPushButton('Otwórz', self)
        btn_otworz.setToolTip('To jest przycisk do wczytania grafiki')
        btn_otworz.resize(btn_otworz.sizeHint())
        btn_otworz.clicked.connect(self.wczytaj_obraz)

        btn_zapisz = QPushButton('Zapisz', self)
        btn_zapisz.setToolTip('To jest przycisk do zapisu zmian w grafice')
        btn_zapisz.resize(btn_zapisz.sizeHint())
        # btn_otworz.clicked.connect(self.zapisz_obraz)

        btn_przywroc = QPushButton('Cofnij zmiany', self)
        btn_przywroc.setToolTip('To jest przycisk do przywrócenia grafiki do ustawień defaultowych')
        btn_przywroc.resize(btn_przywroc.sizeHint())

        combo_skaluj = QComboBox(self)
        combo_skaluj.setToolTip('To jest przycisk do skalowania obrazu')
        combo_skaluj.addItem('Rozm_Oryg')
        combo_skaluj.addItem("25%")
        combo_skaluj.addItem("50%")
        combo_skaluj.addItem('100%')
        combo_skaluj.addItem("200%")
        combo_skaluj.addItem("400%")


        combo_filtr = QComboBox(self)
        combo_filtr.setToolTip('To jest przycisk do zmiany filtru')
        combo_filtr.addItem('DEFAULT')
        combo_filtr.addItem("BLUR")
        combo_filtr.addItem("CONTOUR")
        combo_filtr.addItem("EMBOSS")

        # combo_filtr.activated[str].connect(self.onActivated)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged.connect(lcd.display)

        ramka_zdjecie = QFrame(self)
        ramka_zdjecie.setFrameShape(QFrame.StyledPanel)

        # assemble grid
        grid.addWidget(btn_otworz, 0, 1, 1, 2)
        grid.addWidget(btn_zapisz, 1, 1, 1, 2)
        grid.addWidget(ramka_zdjecie, 2, 0, 2, 4)
        grid.addWidget(lcd, 4, 0, 2, 1)
        grid.addWidget(sld, 5, 1, 1, 1)
        grid.addWidget(lbl_skala, 5, 2)
        grid.addWidget(combo_skaluj, 5, 3, 1, 1)
        grid.addWidget(lbl_filtr, 4, 2)
        grid.addWidget(combo_filtr, 4, 3)
        grid.addWidget(btn_przywroc, 6,2, 1, 2)

        self.setLayout(grid)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Zapisałeś zmiany? Jesteś pewny, że chcesz zamknąć?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())