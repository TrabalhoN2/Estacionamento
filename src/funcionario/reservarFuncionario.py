# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './docs/funcionario/reservar_funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReservarVaga(object):
    def setupUi(self, ReservarVaga):
        ReservarVaga.setObjectName("ReservarVaga")
        ReservarVaga.resize(400, 600)
        ReservarVaga.setMinimumSize(QtCore.QSize(400, 600))
        ReservarVaga.setMaximumSize(QtCore.QSize(400, 600))
        ReservarVaga.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./docs/funcionario/imagens/seguro-de-automovel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReservarVaga.setWindowIcon(icon)
        ReservarVaga.setStyleSheet("background-color: rgb(242, 237, 237);\n"
"color: rgb(75, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(ReservarVaga)
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
        self.btnConfirmar.setGeometry(QtCore.QRect(120, 360, 161, 41))
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
        self.btnCancelar.setGeometry(QtCore.QRect(120, 410, 161, 41))
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
        self.numeroVaga.setGeometry(QtCore.QRect(40, 220, 321, 41))
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
        self.nomeCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.nomeCliente.setGeometry(QtCore.QRect(40, 120, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nomeCliente.setFont(font)
        self.nomeCliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 20px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.nomeCliente.setText("")
        self.nomeCliente.setObjectName("nomeCliente")
        self.placa = QtWidgets.QLineEdit(self.centralwidget)
        self.placa.setGeometry(QtCore.QRect(40, 170, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.placa.setFont(font)
        self.placa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"padding-left: 20px;\n"
"border-radius:10px;\n"
"color: rgb(75, 74, 74);")
        self.placa.setText("")
        self.placa.setObjectName("placa")
        self.dataReserva = QtWidgets.QDateEdit(self.centralwidget)
        self.dataReserva.setGeometry(QtCore.QRect(40, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataReserva.setFont(font)
        self.dataReserva.setStyleSheet("border-radius:10px;\n"
"background-color:white;\n"
"color: rgb(75, 74, 74);\n"
"padding-left: 20px;\n"
"text-align:center;")
        self.dataReserva.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 9, 14), QtCore.QTime(6, 0, 0)))
        self.dataReserva.setObjectName("dataReserva")
        self.intervaloReserva = QtWidgets.QComboBox(self.centralwidget)
        self.intervaloReserva.setGeometry(QtCore.QRect(210, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intervaloReserva.setFont(font)
        self.intervaloReserva.setStyleSheet("border-radius:10px;\n"
"background-color:white;\n"
"color: rgb(75, 74, 74);\n"
"padding-left: 20px;\n"
"text-align:center;")
        self.intervaloReserva.setObjectName("intervaloReserva")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        self.intervaloReserva.addItem("")
        ReservarVaga.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReservarVaga)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        ReservarVaga.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReservarVaga)
        self.statusbar.setObjectName("statusbar")
        ReservarVaga.setStatusBar(self.statusbar)

        self.retranslateUi(ReservarVaga)
        QtCore.QMetaObject.connectSlotsByName(ReservarVaga)

    def retranslateUi(self, ReservarVaga):
        _translate = QtCore.QCoreApplication.translate
        ReservarVaga.setWindowTitle(_translate("ReservarVaga", "Sistema de estacionamento -Reservar"))
        self.label.setText(_translate("ReservarVaga", "Reservar vaga"))
        self.btnConfirmar.setText(_translate("ReservarVaga", "Confirmar"))
        self.btnCancelar.setText(_translate("ReservarVaga", "Cancelar"))
        self.numeroVaga.setPlaceholderText(_translate("ReservarVaga", "Vaga"))
        self.numeroVaga.setItemText(0, _translate("ReservarVaga", "01"))
        self.numeroVaga.setItemText(1, _translate("ReservarVaga", "02"))
        self.numeroVaga.setItemText(2, _translate("ReservarVaga", "03"))
        self.numeroVaga.setItemText(3, _translate("ReservarVaga", "04"))
        self.numeroVaga.setItemText(4, _translate("ReservarVaga", "05"))
        self.numeroVaga.setItemText(5, _translate("ReservarVaga", "06"))
        self.numeroVaga.setItemText(6, _translate("ReservarVaga", "07"))
        self.numeroVaga.setItemText(7, _translate("ReservarVaga", "08"))
        self.numeroVaga.setItemText(8, _translate("ReservarVaga", "09"))
        self.numeroVaga.setItemText(9, _translate("ReservarVaga", "10"))
        self.numeroVaga.setItemText(10, _translate("ReservarVaga", "11"))
        self.numeroVaga.setItemText(11, _translate("ReservarVaga", "12"))
        self.numeroVaga.setItemText(12, _translate("ReservarVaga", "13"))
        self.numeroVaga.setItemText(13, _translate("ReservarVaga", "14"))
        self.numeroVaga.setItemText(14, _translate("ReservarVaga", "15"))
        self.numeroVaga.setItemText(15, _translate("ReservarVaga", "16"))
        self.numeroVaga.setItemText(16, _translate("ReservarVaga", "17"))
        self.numeroVaga.setItemText(17, _translate("ReservarVaga", "18"))
        self.numeroVaga.setItemText(18, _translate("ReservarVaga", "19"))
        self.numeroVaga.setItemText(19, _translate("ReservarVaga", "20"))
        self.nomeCliente.setPlaceholderText(_translate("ReservarVaga", "Nome do cliente"))
        self.placa.setPlaceholderText(_translate("ReservarVaga", "Placa"))
        self.intervaloReserva.setPlaceholderText(_translate("ReservarVaga", "Intervalo"))
        self.intervaloReserva.setItemText(0, _translate("ReservarVaga", "08:00 - 09:00"))
        self.intervaloReserva.setItemText(1, _translate("ReservarVaga", "09:00 - 10:00"))
        self.intervaloReserva.setItemText(2, _translate("ReservarVaga", "10:00 - 11:00"))
        self.intervaloReserva.setItemText(3, _translate("ReservarVaga", "11:00 - 12:00"))
        self.intervaloReserva.setItemText(4, _translate("ReservarVaga", "12:00 - 13:00"))
        self.intervaloReserva.setItemText(5, _translate("ReservarVaga", "13:00 - 14:00"))
        self.intervaloReserva.setItemText(6, _translate("ReservarVaga", "14:00 - 15:00"))
        self.intervaloReserva.setItemText(7, _translate("ReservarVaga", "15:00 - 16:00"))
        self.intervaloReserva.setItemText(8, _translate("ReservarVaga", "16:00 - 17:00"))
        self.intervaloReserva.setItemText(9, _translate("ReservarVaga", "17:00 - 18:00"))
        self.intervaloReserva.setItemText(10, _translate("ReservarVaga", "18:00 - 19:00"))
        self.intervaloReserva.setItemText(11, _translate("ReservarVaga", "19:00 - 20:00"))
        self.intervaloReserva.setItemText(12, _translate("ReservarVaga", "20:00 - 21:00"))
        self.intervaloReserva.setItemText(13, _translate("ReservarVaga", "21:00 - 22:00"))
        self.intervaloReserva.setItemText(14, _translate("ReservarVaga", "22:00 - 23:00"))
