# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './docs/funcionario/realizarCadastro_funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadastrarCliente(object):
    def setupUi(self, CadastrarCliente):
        CadastrarCliente.setObjectName("CadastrarCliente")
        CadastrarCliente.resize(1000, 650)
        CadastrarCliente.setMinimumSize(QtCore.QSize(1000, 650))
        CadastrarCliente.setMaximumSize(QtCore.QSize(1000, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./docs/funcionario/imagens/seguro-de-automovel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CadastrarCliente.setWindowIcon(icon)
        CadastrarCliente.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.centralwidget = QtWidgets.QWidget(CadastrarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.nome_completo = QtWidgets.QLineEdit(self.centralwidget)
        self.nome_completo.setGeometry(QtCore.QRect(340, 140, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nome_completo.setFont(font)
        self.nome_completo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.nome_completo.setText("")
        self.nome_completo.setObjectName("nome_completo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 1001, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(75, 74, 74);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 190, 21, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./docs/funcionario/imagens/carteira-de-identidade.png"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 140, 21, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./docs/funcionario/imagens/user16.png"))
        self.label_2.setObjectName("label_2")
        self.telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.telefone.setEnabled(True)
        self.telefone.setGeometry(QtCore.QRect(340, 290, 321, 41))
        self.telefone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.telefone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.telefone.setObjectName("telefone")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 290, 21, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./docs/funcionario/imagens/telefone.png"))
        self.label_4.setObjectName("label_4")
        self.placa = QtWidgets.QLineEdit(self.centralwidget)
        self.placa.setGeometry(QtCore.QRect(340, 240, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.placa.setFont(font)
        self.placa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.placa.setText("")
        self.placa.setObjectName("placa")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 240, 21, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./docs/funcionario/imagens/placa-de-carro.png"))
        self.label_5.setObjectName("label_5")
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setGeometry(QtCore.QRect(340, 480, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSalvar.setFont(font)
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalvar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 119, 218);\n"
"border: none;\n"
"border-radius:10px;")
        self.btnSalvar.setObjectName("btnSalvar")
        self.cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.cpf.setGeometry(QtCore.QRect(340, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cpf.setFont(font)
        self.cpf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.cpf.setText("")
        self.cpf.setObjectName("cpf")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 400, 321, 21))
        self.label_6.setStyleSheet("color: rgb(75, 74, 74);\n"
"font: 600 12pt \"Segoe UI\";\n"
"\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.vip = QtWidgets.QRadioButton(self.centralwidget)
        self.vip.setGeometry(QtCore.QRect(350, 430, 171, 20))
        self.vip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vip.setStyleSheet("color: rgb(75, 74, 74);")
        self.vip.setObjectName("vip")
        self.naoVip = QtWidgets.QRadioButton(self.centralwidget)
        self.naoVip.setGeometry(QtCore.QRect(350, 450, 201, 20))
        self.naoVip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.naoVip.setStyleSheet("color: rgb(75, 74, 74);")
        self.naoVip.setObjectName("naoVip")
        self.endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.endereco.setEnabled(True)
        self.endereco.setGeometry(QtCore.QRect(340, 340, 321, 41))
        self.endereco.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 40px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.endereco.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.endereco.setObjectName("endereco")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 340, 21, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./docs/funcionario/imagens/endereco.png"))
        self.label_7.setObjectName("label_7")
        self.cpf.raise_()
        self.nome_completo.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.telefone.raise_()
        self.label_4.raise_()
        self.placa.raise_()
        self.label_5.raise_()
        self.btnSalvar.raise_()
        self.label_6.raise_()
        self.vip.raise_()
        self.naoVip.raise_()
        self.endereco.raise_()
        self.label_7.raise_()
        CadastrarCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CadastrarCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        CadastrarCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CadastrarCliente)
        self.statusbar.setObjectName("statusbar")
        CadastrarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(CadastrarCliente)
        QtCore.QMetaObject.connectSlotsByName(CadastrarCliente)

    def retranslateUi(self, CadastrarCliente):
        _translate = QtCore.QCoreApplication.translate
        CadastrarCliente.setWindowTitle(_translate("CadastrarCliente", "Sistema de estacionamento - Finalizando Cadastro"))
        self.nome_completo.setPlaceholderText(_translate("CadastrarCliente", "Nome completo"))
        self.label.setText(_translate("CadastrarCliente", "Finalizando Cadastro"))
        self.telefone.setPlaceholderText(_translate("CadastrarCliente", "Telefone"))
        self.placa.setPlaceholderText(_translate("CadastrarCliente", "Placa do carro"))
        self.btnSalvar.setText(_translate("CadastrarCliente", "Salvar"))
        self.cpf.setPlaceholderText(_translate("CadastrarCliente", "CPF"))
        self.label_6.setText(_translate("CadastrarCliente", "Deseja tornar-se cliente VIP?"))
        self.vip.setText(_translate("CadastrarCliente", "Tornar-se cliente VIP"))
        self.naoVip.setText(_translate("CadastrarCliente", "Não se tornar cliente VIP"))
        self.endereco.setPlaceholderText(_translate("CadastrarCliente", "Endereço"))