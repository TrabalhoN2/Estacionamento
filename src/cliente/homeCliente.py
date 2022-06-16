# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './docs/cliente/home_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeCliente(object):
    def setupUi(self, HomeCliente):
        HomeCliente.setObjectName("HomeCliente")
        HomeCliente.resize(1000, 650)
        HomeCliente.setMinimumSize(QtCore.QSize(1000, 650))
        HomeCliente.setMaximumSize(QtCore.QSize(1000, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./docs/cliente/../../../../../.designer/ES - projeto/img/seguro-de-automovel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HomeCliente.setWindowIcon(icon)
        HomeCliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(HomeCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-2, -5, 1001, 75))
        self.label.setStyleSheet("background-color: rgb(196, 196, 196);\n"
"color: rgb(75, 74, 74);\n"
"font: 24pt \"Segoe UI\";\n"
"padding: 10px;\n"
"border:none;")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 1001, 45))
        self.groupBox.setStyleSheet("background-color: rgb(166, 159, 159);\n"
"padding-inline:10px;\n"
"border:none;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btnVagas = QtWidgets.QPushButton(self.groupBox)
        self.btnVagas.setGeometry(QtCore.QRect(20, 0, 61, 41))
        self.btnVagas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVagas.setStyleSheet("color: rgb(75, 74, 74);\n"
"font: 14pt \"Segoe UI\";\n"
"text-align: left;")
        self.btnVagas.setObjectName("btnVagas")
        self.btnEstacionamento = QtWidgets.QPushButton(self.groupBox)
        self.btnEstacionamento.setGeometry(QtCore.QRect(90, 0, 161, 41))
        self.btnEstacionamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEstacionamento.setStyleSheet("color: rgb(75, 74, 74);\n"
"font: 14pt \"Segoe UI\";\n"
"text-align: left;")
        self.btnEstacionamento.setObjectName("btnEstacionamento")
        self.btnMinhaReserva = QtWidgets.QPushButton(self.groupBox)
        self.btnMinhaReserva.setGeometry(QtCore.QRect(250, 0, 161, 41))
        self.btnMinhaReserva.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMinhaReserva.setStyleSheet("color: rgb(75, 74, 74);\n"
"font: 14pt \"Segoe UI\";\n"
"text-align: left;")
        self.btnMinhaReserva.setObjectName("btnMinhaReserva")
        self.btnSair = QtWidgets.QPushButton(self.groupBox)
        self.btnSair.setGeometry(QtCore.QRect(400, 0, 41, 41))
        self.btnSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSair.setStyleSheet("color: rgb(75, 74, 74);\n"
"font: 14pt \"Segoe UI\";\n"
"text-align: left;")
        self.btnSair.setObjectName("btnSair")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 620, 1001, 31))
        self.label_2.setStyleSheet("background-color: rgb(196, 196, 196);\n"
"color: rgb(75, 74, 74);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.fundo = QtWidgets.QLabel(self.centralwidget)
        self.fundo.setGeometry(QtCore.QRect(10, 130, 941, 321))
        self.fundo.setText("")
        self.fundo.setPixmap(QtGui.QPixmap("./docs/cliente/imagens/carro.png"))
        self.fundo.setAlignment(QtCore.Qt.AlignCenter)
        self.fundo.setObjectName("fundo")
        HomeCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        HomeCliente.setMenuBar(self.menubar)

        self.retranslateUi(HomeCliente)
        QtCore.QMetaObject.connectSlotsByName(HomeCliente)

    def retranslateUi(self, HomeCliente):
        _translate = QtCore.QCoreApplication.translate
        HomeCliente.setWindowTitle(_translate("HomeCliente", "Sistema de estacionamento - Página Inicial"))
        self.label.setText(_translate("HomeCliente", "Sistema de estacionamento"))
        self.btnVagas.setText(_translate("HomeCliente", "Vagas"))
        self.btnEstacionamento.setText(_translate("HomeCliente", "Estacionamento"))
        self.btnMinhaReserva.setText(_translate("HomeCliente", "Minha Reserva"))
        self.btnSair.setText(_translate("HomeCliente", "Sair"))
        self.label_2.setText(_translate("HomeCliente", "Sistema de stacionamento"))
