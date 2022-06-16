# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './docs/funcionario/mudarStatusVaga_funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MudarStatusFuncionario(object):
    def setupUi(self, MudarStatusFuncionario):
        MudarStatusFuncionario.setObjectName("MudarStatusFuncionario")
        MudarStatusFuncionario.resize(400, 600)
        MudarStatusFuncionario.setMinimumSize(QtCore.QSize(400, 600))
        MudarStatusFuncionario.setMaximumSize(QtCore.QSize(400, 600))
        MudarStatusFuncionario.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./docs/funcionario/imagens/seguro-de-automovel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MudarStatusFuncionario.setWindowIcon(icon)
        MudarStatusFuncionario.setStyleSheet("background-color: rgb(242, 237, 237);\n"
"color: rgb(75, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(MudarStatusFuncionario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 431, 71))
        self.label.setStyleSheet("background-color: rgb(196, 196, 196);\n"
"color: rgb(75, 74, 74);\n"
"font: 24pt \"Segoe UI\";\n"
"padding: 10px;\n"
"border:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnConfirmar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfirmar.setGeometry(QtCore.QRect(120, 330, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnConfirmar.setFont(font)
        self.btnConfirmar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmar.setStyleSheet("background-color: rgb(53, 119, 218);\n"
"border: none;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(120, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setStyleSheet("background-color: #FF0505;\n"
"border: none;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.numeroVaga = QtWidgets.QComboBox(self.centralwidget)
        self.numeroVaga.setGeometry(QtCore.QRect(40, 140, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numeroVaga.setFont(font)
        self.numeroVaga.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numeroVaga.setStyleSheet("border-radius:10px;\n"
"background-color:white;\n"
"color: rgb(75, 74, 74);\n"
"padding-left: 20px;\n"
"text-align:center;")
        self.numeroVaga.setEditable(False)
        self.numeroVaga.setObjectName("numeroVaga")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.numeroVaga.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 321, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.vagaOcupada = QtWidgets.QRadioButton(self.centralwidget)
        self.vagaOcupada.setGeometry(QtCore.QRect(70, 230, 89, 20))
        self.vagaOcupada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vagaOcupada.setObjectName("vagaOcupada")
        self.vagaLivre = QtWidgets.QRadioButton(self.centralwidget)
        self.vagaLivre.setGeometry(QtCore.QRect(180, 230, 61, 20))
        self.vagaLivre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vagaLivre.setObjectName("vagaLivre")
        self.vagaReservada = QtWidgets.QRadioButton(self.centralwidget)
        self.vagaReservada.setGeometry(QtCore.QRect(260, 230, 101, 20))
        self.vagaReservada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vagaReservada.setObjectName("vagaReservada")
        MudarStatusFuncionario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MudarStatusFuncionario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MudarStatusFuncionario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MudarStatusFuncionario)
        self.statusbar.setObjectName("statusbar")
        MudarStatusFuncionario.setStatusBar(self.statusbar)

        self.retranslateUi(MudarStatusFuncionario)
        QtCore.QMetaObject.connectSlotsByName(MudarStatusFuncionario)

    def retranslateUi(self, MudarStatusFuncionario):
        _translate = QtCore.QCoreApplication.translate
        MudarStatusFuncionario.setWindowTitle(_translate("MudarStatusFuncionario", "Sistema de estacionamento - Mudar status da vaga"))
        self.label.setText(_translate("MudarStatusFuncionario", "Mudar status da vaga"))
        self.btnConfirmar.setText(_translate("MudarStatusFuncionario", "Confirmar"))
        self.btnCancelar.setText(_translate("MudarStatusFuncionario", "Cancelar"))
        self.numeroVaga.setPlaceholderText(_translate("MudarStatusFuncionario", "Vaga"))
        self.numeroVaga.setItemText(0, _translate("MudarStatusFuncionario", "01"))
        self.numeroVaga.setItemText(1, _translate("MudarStatusFuncionario", "02"))
        self.numeroVaga.setItemText(2, _translate("MudarStatusFuncionario", "03"))
        self.numeroVaga.setItemText(3, _translate("MudarStatusFuncionario", "04"))
        self.numeroVaga.setItemText(4, _translate("MudarStatusFuncionario", "05"))
        self.numeroVaga.setItemText(5, _translate("MudarStatusFuncionario", "06"))
        self.numeroVaga.setItemText(6, _translate("MudarStatusFuncionario", "07"))
        self.numeroVaga.setItemText(7, _translate("MudarStatusFuncionario", "08"))
        self.numeroVaga.setItemText(8, _translate("MudarStatusFuncionario", "09"))
        self.numeroVaga.setItemText(9, _translate("MudarStatusFuncionario", "10"))
        self.numeroVaga.setItemText(10, _translate("MudarStatusFuncionario", "11"))
        self.numeroVaga.setItemText(11, _translate("MudarStatusFuncionario", "12"))
        self.numeroVaga.setItemText(12, _translate("MudarStatusFuncionario", "13"))
        self.numeroVaga.setItemText(13, _translate("MudarStatusFuncionario", "14"))
        self.numeroVaga.setItemText(14, _translate("MudarStatusFuncionario", "15"))
        self.numeroVaga.setItemText(15, _translate("MudarStatusFuncionario", "16"))
        self.numeroVaga.setItemText(16, _translate("MudarStatusFuncionario", "17"))
        self.numeroVaga.setItemText(17, _translate("MudarStatusFuncionario", "18"))
        self.numeroVaga.setItemText(18, _translate("MudarStatusFuncionario", "19"))
        self.numeroVaga.setItemText(19, _translate("MudarStatusFuncionario", "20"))
        self.label_2.setText(_translate("MudarStatusFuncionario", "Status atual da vaga:"))
        self.vagaOcupada.setText(_translate("MudarStatusFuncionario", "Ocupada"))
        self.vagaLivre.setText(_translate("MudarStatusFuncionario", "Livre"))
        self.vagaReservada.setText(_translate("MudarStatusFuncionario", "Reservada"))
